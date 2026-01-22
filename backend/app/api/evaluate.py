from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

from backend.app.agents.evidence_scoring_agent import EvidenceScoringAgent
from backend.app.agents.retrieval_agent import RetrievalAgent
from backend.app.agents.audit_failure_agent import AuditFailureAgent
from backend.app.agents.risk_evaluation_agent import RiskEvaluationAgent
from backend.app.agents.recommendation_agent import RecommendationAgent
from backend.app.agents.ui_formatter_agent import UIFormatterAgent


# ----------------
# Router
# ----------------
router = APIRouter(tags=["Evaluation"])


# ----------------
# Request Schema
# ----------------
class EvaluateRequest(BaseModel):
    location: str
    query: str
    threat_id: str = "T-001"


# ----------------
# Agents
# ----------------
retrieval = RetrievalAgent()
scoring = EvidenceScoringAgent()
audit = AuditFailureAgent()
risk_eval = RiskEvaluationAgent()
recommend = RecommendationAgent()
formatter = UIFormatterAgent()


# ----------------
# Endpoint
# ----------------
@router.post("/evaluate")
def evaluate_threat(payload: EvaluateRequest):
    evidence = retrieval.retrieve(
        query_text=payload.query,
        location=payload.location
    )

    score_result = scoring.score(evidence)

    audit_result = audit.audit(
        evidence_score=score_result["evidence_score"],
        conflict_level=score_result["conflict_level"],
        coverage=score_result["coverage"]
    )

    if audit_result["status"] == "fail":
        return {
            "status": "monitoring",
            "reason": audit_result["reason"],
            "confidence": score_result["evidence_score"]
        }

    rank = risk_eval.evaluate(
        evidence_score=score_result["evidence_score"]
    )

    recommendation = recommend.recommend(
        rank=rank,
        confidence=score_result["evidence_score"]
    )

    return formatter.format(
        threat_id=payload.threat_id,
        location=payload.location,
        rank=rank.value,
        confidence=score_result["evidence_score"],
        recommendation=recommendation["recommendation"].value,
        reason=recommendation["reason"],
        status="Monitoring"
    )
