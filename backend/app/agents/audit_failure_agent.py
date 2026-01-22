class AuditFailureAgent:
    """
    SIMULATION MODE Audit / Failure Node Agent
    """

    def audit(self, evidence_score, conflict_level, coverage):
        """
        Decides whether to allow escalation or cap action.
        """

        if evidence_score < 0.4:
            return {
                "status": "fail",
                "reason": "Insufficient evidence confidence"
            }

        if conflict_level == "high":
            return {
                "status": "fail",
                "reason": "High evidence conflict detected"
            }

        return {
            "status": "pass"
        }
