from typing import List, Dict, Any


class EvidenceScoringAgent:
    """
    SIMULATION MODE Evidence Scoring Agent
    """

    def score(self, evidence):
        """
        Returns deterministic, demo-safe scoring.
        """

        return {
            "evidence_score": 0.72,
            "conflict_level": "low",
            "coverage": "partial"
        }

