# AutoCast AI
 
Global automotive registration forecasting and market intelligence.
 
## Quick Start
 
### Backend
    cd backend
    pip install -r requirements.txt
    python app.py
 
### Frontend
    cd frontend
    npm install
    npm run dev
 
### Data
See `docs/dataset_sources.md`. Raw data is not committed; run `python scripts/download_data.py`.
 
### Model
See `models/metadata/global_model_v1.json` for artifact details. Trained in Colab notebooks 01–05.
 
## Documentation
- `docs/dataset_sources.md` — data contract and attribution
- `docs/data_quality.md` — coverage and missingness report
- `docs/architecture.md` — system layers and rules
- `docs/api_documentation.md` — endpoint reference (Phase 3)
- `docs/model_card.md` — model details (Phase 2)