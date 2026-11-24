# AutoCast AI — Architecture
 
## Layers
 
1. **Data ingestion** (`scripts/download_data.py`, `scripts/validate_data.py`)
2. **ML training** (Colab notebooks 01–05) → exported artifact
3. **Backend API** (Flask + SQLite) → loads artifact, serves predictions
4. **Frontend** (React + Vite + Recharts) → consumes API
 
## Data Flow
 
Ember CSV
  → validate_data.py → data/processed/registrations.parquet
  → Colab feature engineering → chronological split
  → train Naïve / RF / XGBoost → evaluate (MAE, RMSE, WAPE)
  → export models/autocast_global_v1.joblib + models/metadata/global_model_v1.json
  → Flask loads artifact → /api/forecast/generate
  → React dashboard
 
## Critical Rules
 
- **One pipeline, two callers.** Feature engineering is a single Python module. Training calls it; Flask inference calls it. Never reimplement lags or encoders in the backend.
- **No training during API requests.** The backend only calls `pipeline.predict()`.
- **Synthetic inventory is separate.** Inventory demo data lives in its own table and never feeds the forecast model.
- **Aggregates are dashboard-only.** `World` and regional rows never enter the training table.
 
## Artifact Boundary
 
| Artifact | Location | Committed? |
|---|---|---|
| Raw Ember CSV | `data/raw/` | No (re-downloadable) |
| Processed parquet | `data/processed/` | No (regenerable) |
| Sample quality CSV | `data/sample/` | Yes (small) |
| Model `.joblib` | `models/` | No — GitHub Release or HF |
| Model metadata JSON | `models/metadata/` | Yes (small, textual) |