# Crisis Monitoring System using Multimodal AI & Vector Memory

## Overview
The **Crisis Monitoring System** is a decision-support platform designed to help humans understand and contextualize emerging crises such as air quality deterioration, flooding risk, heat stress, and similar societal or environmental threats.

Instead of relying solely on threshold-based alerts, the system focuses on **contextual intelligence** by combining multimodal evidence, vector-based memory, and AI-assisted reasoning. The goal is not to automate decisions, but to **augment human judgment** with interpretable, evidence-backed insights.

---

## Problem Statement
Crises rarely occur as sudden, isolated events. They evolve gradually through weak signals distributed across time, geography, and multiple data sources.

Most existing monitoring systems:
- Display raw metrics without context
- Operate in silos
- Provide alerts without historical or situational grounding

This makes it difficult for decision-makers to assess severity, urgency, or relevance.

The Crisis Monitoring System addresses this gap by organizing scattered signals into **contextual risk narratives**, enabling earlier and more informed responses.

---

## System Architecture

The system follows a **modular, layered architecture** designed for clarity, extensibility, and transparency.

### Core Layers
- **Data Ingestion Layer**  
  Accepts manual human reports and historical datasets.

- **Embedding Layer**  
  Converts heterogeneous inputs into semantic vector representations using transformer-based embedding models.

- **Vector Memory Layer (Qdrant)**  
  Stores embeddings of historical risk signals and manual evidence to enable semantic retrieval.

- **Reasoning Layer**  
  Uses retrieved context combined with rule-based logic to evaluate emerging risks.

- **Visualization Layer**  
  Presents contextualized risk information through a map-based frontend.

Each layer has a single responsibility, ensuring the system can evolve incrementally without redesign.

---

## Why Qdrant is Used
Qdrant serves as the **vector-based memory backbone** of the system.

### Current, Honest Usage
- A Qdrant client is configured in the backend
- Retrieval logic is implemented to query vector memory
- The system is architected around vector-based evidence retrieval
- Intended storage includes:
  - Historical risk signals
  - Manual human-reported evidence
  - Retrieved context for reasoning agents

### What Is Not Claimed
- No model training on Qdrant
- No heavy vector population demonstrated in the frontend
- No production-scale deployment claim

Qdrant is a **core architectural component**, even though full end-to-end persistence is still under development.

---

## Multimodal Strategy

### Data Types Used
The system currently operates on:
1. **Manual Human Reports (Crowdsourced Evidence)**  
   Qualitative observations such as unusual environmental conditions or local alerts.
2. **Historical Datasets (Simulated or Public)**  
   Quantitative data used to provide temporal and contextual grounding.

### Embeddings and Querying
- All inputs are converted into embeddings using transformer-based models.
- Embeddings map heterogeneous data into a shared semantic space.
- Vector similarity search is used to retrieve contextually relevant past evidence.

This allows the system to compare situations based on meaning rather than keywords or thresholds.

---

## Search, Memory, and Recommendation Logic

### Retrieval
- New evidence is embedded and queried against stored vectors in Qdrant.
- The most semantically similar past entries are retrieved as contextual memory.

### Memory Management
- Memory is **additive**, not destructive.
- New evidence enriches the vector store without overwriting past data.
- Retrieved memory can be reused across evaluations.

### Recommendations
- The system does not make autonomous decisions.
- Outputs are explanatory summaries highlighting:
  - Relevant past situations
  - Contextual factors
  - Interpretable risk signals
- Humans remain fully in the decision loop.

---

## Limitations
- Vector memory is not yet fully populated.
- End-to-end frontend querying of Qdrant-backed endpoints is not fully demonstrated.
- Data coverage is limited to available manual and historical inputs.

These limitations are acknowledged as part of a prototype-stage system.

---

## Ethics and Safety
- No personally identifiable information (PII) is ingested.
- Bias risks from incomplete data are mitigated through transparency and traceable evidence.
- The system is strictly advisory and does not perform autonomous decision-making.

Ethical design prioritizes safety, explainability, and responsible AI usage.

---

## Future Scope
Planned extensions include:
- Full vector persistence and live frontend integration
- Additional data modalities (e.g., sensor feeds, satellite imagery)
- Temporal reasoning agents for trend and scenario analysis
- Enhanced visualization for comparative and longitudinal insights

All future enhancements can be implemented without altering the core architecture.

---

## Tech Stack (Indicative)
- **Backend:** Python, FastAPI
- **Vector Store:** Qdrant
- **Embeddings:** Transformer-based embedding models
- **Frontend:** HTML / CSS / JavaScript (map-based visualization)
- **Architecture Style:** Modular, memory-driven AI system

---

## Project Status
This project is currently at **prototype stage**, focusing on architectural correctness, interpretability, and honest capability representation.

---

## License
This project is intended for educational and hackathon demonstration purposes.
