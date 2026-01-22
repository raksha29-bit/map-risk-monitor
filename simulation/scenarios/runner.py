import json
from pathlib import Path

from backend.app.agents.ingestion_agent import IngestionAgent
from backend.app.agents.retrieval_agent import RetrievalAgent
from backend.app.agents.evidence_scoring_agent import EvidenceScoringAgent
from backend.app.agents.audit_failure_agent import AuditFailureAgent
from backend.app.agents.risk_evaluation_agent import RiskEvaluationAgent
from backend.app.agents.recommendation_agent import RecommendationAgent
from backend.app.agents.ui_formatter_agent import UIFormatterAgent


def run_scenario(file_path: str):
    data = json.loads(Path(file_path).read_text())

    ingestion = IngestionAgent()
    retrieval = RetrievalAgent()
    scoring = EvidenceScoringAgent()
    audit = AuditFailureAgent()
    risk_eval = RiskEvaluationAgent()
    recommend = RecommendationAgent()
    formatter = UIFormatterAgent()

    # Ingest signals
    for s in data["signals"]:
        ingestion.ingest({
            "source": s["source"],
            "value": s["value"],
            "location": data["location"],
            "reliability": s["reliability"]
        })

    # Evaluate
    evidence = retrieval.retrieve(
        query_text=data["query"],
        location=data["location"]
    )

    score = scoring.score(evidence)
    audit_res = audit.audit(
        score["evidence_score"],
        score["conflict_level"],
        score["coverage"]
    )

    if audit_res["status"] == "fail":
        return {
            "status": "Monitoring",
            "reason": audit_res["reason"],
            "confidence": score["evidence_score"]
        }

    rank = risk_eval.evaluate(score["evidence_score"])
    rec = recommend.recommend(rank, score["evidence_score"])

    return formatter.format(
        threat_id="SIM-001",
        location=data["location"],
        rank=rank.value,
        confidence=score["evidence_score"],
        recommendation=rec["recommendation"].value,
        reason=rec["reason"],
        status="Monitoring"
    )


if __name__ == "__main__":
    result = run_scenario("simulation/scenarios/rising_aqi.json")
    print(json.dumps(result, indent=2))
