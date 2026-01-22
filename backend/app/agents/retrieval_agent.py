from typing import List, Dict, Any


class RetrievalAgent:
    """
    SIMULATION MODE Retrieval Agent
    (Heavy dependencies removed for hackathon stability)
    """

    def __init__(self):
        pass

    def retrieve(
        self,
        query_text: str,
        location: str,
        hours_back: int = 24,
        limit: int = 10
    ) -> List[Dict[str, Any]]:
        """
        Returns simulated evidence.
        Interface is identical to real retrieval,
        so downstream agents remain unchanged.
        """

        return [
            {
                "source": "SIMULATED_SIGNAL",
                "location": location,
                "text": query_text,
                "timestamp": "recent",
                "reliability": 0.85,
                "similarity_score": 0.82
            }
        ]
