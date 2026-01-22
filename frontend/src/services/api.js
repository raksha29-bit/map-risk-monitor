export const API_BASE = "http://localhost:8000/api";

export async function fetchLiveRisks() {
  const res = await fetch(`${API_BASE}/risk/live`);
  if (!res.ok) {
    throw new Error("Failed to fetch live risks");
  }
  return res.json();
}
