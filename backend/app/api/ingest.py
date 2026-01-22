from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional,Dict, Any
from datetime import datetime

# router
router = APIRouter(tags=["Ingestion"])


# ---------
# Schema
# ---------
class IngestRequest(BaseModel):
    source: str
    value: Any
    location: str
    reliability: float
    timestamp: Optional[datetime] = None

    metadata: Optional[Dict[str, Any]] = None 


# ---------
# Endpoint
# ---------
@router.post("/ingest")
def ingest_signal(payload: IngestRequest):
    """
    Ingests incoming signals (AQI, crowd, weather, patrol gaps, etc.)
    Data can be simulated or offline.
    """

    data = payload.dict()

    # fallback timestamp
    if data["timestamp"] is None:
        data["timestamp"] = datetime.utcnow()

    # 👉 later this goes to:
    # - Qdrant (embeddings + metadata)
    # - IngestionAgent
    # For now: stub response (hackathon-safe)

    return {
        "status": "ingested",
        "source": data["source"],
        "location": data["location"],
        "timestamp": data["timestamp"],
        "reliability": data["reliability"]
    }
