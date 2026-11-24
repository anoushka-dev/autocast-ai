# Data Quality Report — Ember Monthly EV Sales
 
Generated from `notebooks/01_data_exploration.ipynb` on [date].
 
## Coverage
 
- Overall date range: 2005-01-01 → 2026-10-01
- Countries: 59
- Regions: 2
- Data frequency: Monthly
- Latest observation (top 10 markets): 2026-10-01
- Countries ending before 2026-10-01: 30
 
## Series Inventory
 
- Total country-drivetrain series: 316
- Structurally absent (excluded): **12** — see list below
- Reporting zeros (flagged, retained): **66**
- <24 observations (insufficient for lag-12 modeling): **4** — see list below
 
### Structurally Absent Series (excluded from modeling)
 
             Area                Drivetrain
37         Canada          Battery electric
38         Canada                    Diesel
39         Canada                    Hybrid
40         Canada                     Other
41         Canada                    Petrol
42         Canada            Plug-in hybrid
62         Cyprus                     Other
233       Romania            Plug-in hybrid
251  South Africa          Battery electric
252  South Africa  Combustion (unspecified)
253  South Africa                    Hybrid
254  South Africa            Plug-in hybrid
 
### Series with <24 Observations
 
             Area                Drivetrain  n_obs
251  South Africa          Battery electric     14
252  South Africa  Combustion (unspecified)     14
253  South Africa                    Hybrid     14
254  South Africa            Plug-in hybrid     14
 
## Known Anomalies
 
- **Germany BEV structural break, Dec 2023 → Jan 2024.** Registrations fell from 104,325 to 18,136 — the German Umweltbonus termination on 17 Dec 2023 caused a pull-forward. Models must either exclude 2023-12 from training or use an event dummy.
- **Series start dates vary widely.** Germany BEV starts 2017-01; overall dataset starts 2005-01. Features must not assume uniform history.
- **Membership columns** (`EU member`, `OECD member`, `G20 member`, `G7 member`, `ASEAN member`) are stored as `object` dtype — convert to bool before modeling.
 
## Known Limitations (from Ember's methodology)
 
- Series start dates vary from 2005 to 2024 by country.
- Smaller EU markets start in 2023.
- Latest available month differs by country — publishers release data 2–6 weeks after month-end.
- National registrations ≠ dealer sales ≠ inventory requirements.
 
## Attached Artifacts
 
- `data/sample/ember_series_quality_summary.csv` — per-series observation counts, first/last dates, non-zero counts. Size: 16,636 bytes. Committed to repo.