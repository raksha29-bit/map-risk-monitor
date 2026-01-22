import { useEffect, useState } from "react";
import { fetchLiveRisks } from "../services/api";

export default function ThreatSummary() {
  const [risks, setRisks] = useState([]);

  useEffect(() => {
    fetchLiveRisks()
      .then(setRisks)
      .catch((err) => console.error("Failed to load threats", err));
  }, []);

  // Fallback if no data yet (demo-safe)
  if (risks.length === 0) {
    return (
      <div className="panel">
        <h3>No active threats</h3>
        <p>Status: Monitoring</p>
      </div>
    );
  }

  // Show the most critical threat (top item)
  const threat = risks[0];

  return (
    <div className="panel">
      <h3>{threat.type}</h3>
      <p>Rank: {threat.level ?? "A"}</p>
      <p>Status: Active Monitoring</p>
      <p>{threat.description}</p>
    </div>
  );
}
