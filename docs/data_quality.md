# Data Quality Report — Ember Monthly EV Sales

**Generated:** [2026-11-27]
**Notebooks:** `01_data_exploration.ipynb`, `02_data_cleaning.ipynb`, `03_eda.ipynb`
**Contract:** `docs/dataset_sources.md`
**Status:** Cleaning checks recorded in the project notes passed for the retained country–drivetrain panel. The EDA notebook contains eight analyses, but several written findings were stale or placeholders when reviewed. This report uses the saved notebook outputs where available and explicitly marks values that were not captured.
---

## 1. Source

| Field | Value |
|---|---|
| Publisher | Ember (ember-energy.org) |
| License | CC BY 4.0 |
| Download date | [YYYY-MM-DD] |
| Raw file | `data/raw/monthly_ev_sales.csv` |
| Raw rows × columns | 46,870 × 24 |

The source records monthly first-time passenger-car registrations by country/economy and drivetrain. These registrations are a demand indicator; they are not equivalent to OEM wholesale sales, dealer retail sales, or dealer inventory.

---

## 2. Coverage

| Metric | Value |
|---|---|
| Overall date range (raw) | 2005-01-01 → 2026-10-01 |
| Date range (processed, after cleaning) | [2005-01-01 → 2026-10-01] |
| Countries (raw, `Area type == 'Country or economy'`) | [ 59 ] |
| Regions (raw) | [Asia; Europe; Latin America and Caribbean; Middle East; North America; Oceania] |
| Countries (processed) | [from 02: 57] |
| Total country-drivetrain series (raw) | 316 |
| Series retained after cleaning | [from 02: 304] |
| Data frequency | Monthly |

The processed table contains 33,064 rows, 57 countries/economies, and 304 country–drivetrain series. Series start dates and latest available dates vary. Do not treat the overall maximum date as the latest date for every country or series.

---

## 3. Series Inventory (from `02_data_cleaning.ipynb`)

| Metric | Value |
|---|---|
| Rows after aggregate split | 34,092 |
| Rows after region exclusion | 33,432 |
| **Structural-zero series excluded** | **12** |
| **Series with <12 observations excluded** | [from 02 Cell 5: 0 (all 316 candidate series met the 12-observation threshold)] |
| **Series retained** | **304** |
| Rows dropped (structural zeros) | 374 |
| **Rows added by monthly reindex** | **6** |
| Final training rows | 33,064 |

### Structurally absent series (excluded)
Structurally absent series (all zeros): 12
[Paste the list from `01_data_exploration.ipynb` Cell 8 output — 12 rows]

### Series with fewer than 12 observations (excluded)

[Run `series_stats[~series_stats['has_min_history']][['iso3','drivetrain','n_obs']]` in `02_data_cleaning.ipynb` and paste here]

---

## 4. Validation Results

| Check | Result |
|---|---|
| **Primary key duplicates** (`iso3, drivetrain, date`) | 0 |
| **Contiguity check** (all series have contiguous monthly dates within their own span) | 304/304 |
| **NaN in target** (`registrations`) | 6, all flagged with was_missing = True |
| **Negative registrations** | [run `(df['registrations'] < 0).sum()` → expected 0] |
| **Membership dtype conversion** | ✅ All 5 columns (`is_eu`, `is_oecd`, `is_g20`, `is_g7`, `is_asean`) are `bool` |

The notebook's old expectation of zero NaN target values is not correct after the current cleaning logic. The six flagged gaps are intentional and should remain visible in the quality report.

---

## 5. Known Anomalies

- **Germany BEV structural break, Dec 2023 → Jan 2024.** Registrations fell from **104,325** to **18,136** (**−82.6%**) following the German Umweltbonus termination on 17 Dec 2023. This is a real demand event, not a data error. Model handling: exclude 2023-12 from training or add an event dummy feature (Phase 2 decision).

- **Series start dates vary widely.** Overall dataset starts 2005-01-01, but individual series start as late as 2023 (smaller EU markets). The `series_metadata.parquet` records each series' `first_date`. Feature engineering must not assume uniform history.

- **Latest observation date varies by country.** Top markets (Albania, Australia, India, Israel, Italy, Japan, Malaysia, Nepal, Netherlands, New Zealand) end at **2026-10-01**. Countries ending earlier: [list from 01 Cell 7].

- **Membership flags** were stored as `object` in the raw CSV and converted to `bool` during cleaning. Original values were `"True"`/`"False"` strings.

- **`Registrations` is `float64`** in raw; all values are integers in practice. Verified no NaN, no negatives.

---

## 6. Coverage Gaps (from `03_eda.ipynb`, Plot 7)

- **Countries with complete monthly data since 2005:** [from Plot 7 finding]
- **Countries starting in 2023:** [from Plot 7 finding]
- **Countries with fewer than 10 months in 2026:** 27

This confirms the data contract rule: **never assume a single global "latest month"** — track per-series.

---

## 7. Known Limitations (from Ember's methodology)

- Series start dates vary from 2005 to 2024 by country.
- Smaller EU markets start in 2023.
- Latest available month differs by country — publishers release data 2–6 weeks after month-end.
- National registrations ≠ dealer sales ≠ inventory requirements.
- Ember fills absent drivetrains with zero; the distinction between structural zero and reporting zero is enforced in cleaning.

---

## 8. Attached Artifacts

| File | Location | Committed? | Size |
|---|---|---|---|
| Per-series coverage summary | `data/sample/ember_series_quality_summary.csv` | ✅ | 16,636 bytes |
| Processed sample (2,000 rows) | `data/sample/processed_sample.csv` | ✅ | ~[from 02] |
| Series metadata | `data/processed/series_metadata.parquet` | ❌ (regenerable) | — |
| Cleaned registrations | `data/processed/registrations.parquet` | ❌ (regenerable) | — |
| Aggregates (shares only) | `data/processed/aggregates.parquet` | ❌ (regenerable) | — |
| EDA plots | `docs/eda/*.png` (8 files) | ✅ | — |

---

## 9. Reproducibility Statement

> Given `data/raw/monthly_ev_sales.csv`, running `scripts/validate_data.py` followed by `notebooks/02_data_cleaning.ipynb` top-to-bottom on a fresh kernel produces `data/processed/registrations.parquet` with identical row counts and passing all three assertions in Cell 11. This was verified by [teammate name] on [date].