'''from fastapi import FastAPI

# import routers
from backend.app.api import ingest, evaluate, history, simulate, risk

# import startup logic
from backend.app.core.startup import initialize_system


app = FastAPI(
    title="Map-Based Risk & Crisis Monitoring System",
    version="0.1.0"
)

app.include_router(ingest.router, prefix="/api")
app.include_router(evaluate.router, prefix="/api")
app.include_router(history.router, prefix="/api")
app.include_router(simulate.router, prefix="/api")
app.include_router(risk.router, prefix="/api")

@app.on_event("startup")
def startup_event():
    initialize_system()

@app.get("/")
def health_check():
    return {
        "status": "ok",
        "message": "System running"
    }'''
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime

router = APIRouter(tags=["Ingestion"])


class IngestRequest(BaseModel):
    source: str
    value: Any
    location: str
    reliability: float
    timestamp: Optional[datetime] = None
    metadata: Optional[Dict[str, Any]] = None


@router.post("/ingest")
def ingest_signal(payload: IngestRequest):
    """
    Ingest incoming signals (AQI, weather, water level, etc.)
    """

    # ✅ Pydantic v2 method
    data = payload.model_dump()

    # fallback timestamp
    if data["timestamp"] is None:
        data["timestamp"] = datetime.utcnow()

    return {
        "status": "ingested",
        "source": data["source"],
        "location": data["location"],
        "timestamp": data["timestamp"].isoformat(),  # ✅ safe JSON
        "reliability": data["reliability"],
    }
