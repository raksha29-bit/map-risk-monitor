class UIFormatterAgent:
    """
    SIMULATION MODE UI Formatter Agent
    Converts internal decision output into UI-ready JSON
    """

    def format(
        self,
        threat_id: str,
        location: str,
        rank: str,
        confidence: float,
        recommendation: str,
        reason: str,
        status: str
    ) -> dict:
        return {
            "threat_id": threat_id,
            "location": location,
            "rank": rank,
            "confidence": confidence,
            "recommendation": recommendation,
            "reason": reason,
            "status": status
        }
