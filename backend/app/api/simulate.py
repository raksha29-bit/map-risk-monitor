from fastapi import APIRouter
from pydantic import BaseModel


# ----------------
# Router
# ----------------
router = APIRouter(tags=["Simulation"])


# ----------------
# Response Schema (optional but clean)
# ----------------
class SimulationResponse(BaseModel):
    query: str
    location: str


# ----------------
# Endpoint
# ----------------
@router.get("/simulate", response_model=SimulationResponse)
def simulate_scenario(name: str):
    """
    Returns predefined simulation scenarios
    for demo / hackathon use.
    """

    scenarios = {
        "rising_aqi": {
            "query": "AQI rising continuously",
            "location": "Zone 5"
        },
        "crowd_buildup": {
            "query": "Crowd density increasing",
            "location": "Zone 3"
        },
        "patrol_gap": {
            "query": "Patrol delays reported",
            "location": "Zone 7"
        }
    }

    if name not in scenarios:
        return {
            "query": "Unknown scenario",
            "location": "N/A"
        }

    return scenarios[name]
