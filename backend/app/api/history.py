from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict, Any

from backend.app.agents.memory_agent import MemoryAgent



# ----------------
# Router
# ----------------
router = APIRouter(tags=["History"])


# ----------------
# Schema
# ----------------
class HistoryRecord(BaseModel):
    decision: Dict[str, Any]


# ----------------
# Agent
# ----------------
memory = MemoryAgent()


# ----------------
# Endpoint
# ----------------
@router.post("/history")
def store_history(payload: HistoryRecord):
    memory.store_decision(payload.decision)
    return {"status": "stored"}
