from fastapi import APIRouter

router = APIRouter()

@router.get("/risk/live")
def get_live_risks():
    return [
        {
            "type": "Threat A-12",
            "level": "A",
            "description": "AQI rising rapidly",
            "lat": 26.21,
            "lon": 78.18
        },
        {
            "type": "Flood Watch",
            "level": "B",
            "description": "Water level increasing near river basin",
            "lat": 25.43,
            "lon": 81.84
        }
    ]
