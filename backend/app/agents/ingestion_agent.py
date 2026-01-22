from datetime import datetime
from typing import Dict, Any

from sentence_transformers import SentenceTransformer
from qdrant_client.models import PointStruct

from backend.app.core.qdrant_client import qdrant_client



class IngestionAgent:
    def __init__(self):
        # Lightweight embedding model
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.collection_name = "current_signals"

    def ingest(self, data: Dict[str, Any]) -> None:
        """
        Ingest a single signal into Qdrant.
        data example:
        {
            "source": "AQI_SENSOR",
            "value": "AQI 180",
            "location": "Zone 5",
            "reliability": 0.8
        }
        """

        text_for_embedding = f"{data['source']} {data['value']} at {data['location']}"
        vector = self.model.encode(text_for_embedding).tolist()

        point = PointStruct(
            id=f"{data['source']}_{datetime.utcnow().isoformat()}",
            vector=vector,
            payload={
                "source": data["source"],
                "value": data["value"],
                "location": data["location"],
                "reliability": data.get("reliability", 0.5),
                "timestamp": datetime.utcnow().isoformat()
            }
        )

        qdrant_client.upsert(
            collection_name=self.collection_name,
            points=[point]
        )
