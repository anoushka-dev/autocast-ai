# Data Quality Report — Ember Monthly EV Sales
 
Generated from Colab notebook `01_data_exploration.ipynb` on [date].
 
## Coverage
 
- Total Rows: 46870
- Total Columns: 24
- Date range: 2005-01-01 00:00:00 to 2026-10-01 00:00:00
- Unique Areas: 61
- Aggregate Rows: 12778
- Countries with data: [n]
- Countries with latest observation in [most recent month]: [n]
- Countries whose latest observation is older than [month]: [list]
 
## Series Length Distribution
 
| Observations per series | Number of series |
|---|---|
| < 12 | [n] |
| 12–23 | [n] |
| 24–59 | [n] |
| 60+ | [n] |
 
## Structural Zeros vs Reporting Zeros
 
- Structurally absent series (all zeros): [n] — excluded from modeling
- Series with reporting zeros: [n] — retained, flagged
- Example structurally absent: [Country] — [Drivetrain]
- Example reporting zero: [Country] — [Drivetrain], zero in [months]
 
## Known Limitations
 
- Series start dates vary from 2005 to 2024 by country.
- Smaller EU markets start in 2023.
- Latest available month differs by country (publishers release 2–6 weeks after month-end).
- National registrations ≠ dealer sales ≠ inventory requirements.
 
## Attached Artifacts
 
- `data/sample/ember_series_quality_summary.csv` — per-series observation counts, first/last dates, non-zero counts.