from typing import Dict, Any, List
from datetime import datetime


class MemoryAgent:
    """
    SIMULATION MODE Memory Agent
    Stores alert and decision history in-memory
    """

    def __init__(self):
        self.history: List[Dict[str, Any]] = []

    def store_decision(self, decision: Dict[str, Any]) -> None:
        record = {
            **decision,
            "stored_at": datetime.utcnow().isoformat()
        }
        self.history.append(record)

    def get_history(self) -> List[Dict[str, Any]]:
        return self.history
