from enum import Enum


class ActionType(Enum):
    MONITOR = "Monitor"
    SOFT_ALERT = "Soft Alert"
    IMMEDIATE_ACTION = "Immediate Action"


class RecommendationAgent:
    """
    SIMULATION MODE Recommendation Agent
    """

    def recommend(self, rank, confidence: float):
        if rank.value in ["A", "S"]:
            return {
                "recommendation": ActionType.IMMEDIATE_ACTION,
                "reason": "High threat rank with significant delay risk"
            }

        if rank.value in ["B", "C"]:
            return {
                "recommendation": ActionType.SOFT_ALERT,
                "reason": "Moderate risk, early awareness advised"
            }

        return {
            "recommendation": ActionType.MONITOR,
            "reason": "Low risk, monitoring sufficient"
        }
