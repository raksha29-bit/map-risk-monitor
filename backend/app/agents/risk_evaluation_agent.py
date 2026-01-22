from enum import Enum


class ThreatRank(Enum):
    E = "E"
    D = "D"
    C = "C"
    B = "B"
    A = "A"
    S = "S"


class RiskEvaluationAgent:
    """
    SIMULATION MODE Risk Evaluation Agent
    """

    def evaluate(self, evidence_score: float) -> ThreatRank:
        if evidence_score >= 0.8:
            return ThreatRank.S
        if evidence_score >= 0.65:
            return ThreatRank.A
        if evidence_score >= 0.5:
            return ThreatRank.B
        if evidence_score >= 0.35:
            return ThreatRank.C
        return ThreatRank.D
