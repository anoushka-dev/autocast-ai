# Dataset Sources and Data Contract
 
## Primary Dataset: Ember Monthly EV Sales
 
| Field | Value |
|---|---|
| Publisher | Ember (ember-energy.org) |
| Source URL | https://ember-energy.org/data/monthly-ev-sales-data/ |
| File downloaded | monthly_ev_sales.csv |
| License | CC BY 4.0 — attribution required |
| Download date | [YYYY-MM-DD — the date you downloaded it] |
| Overall date range | 2005-01-01 → 2026-10-01 |
| Latest observation (top markets) | 2026-10-01 (Albania, Australia, India, Israel, Italy, Japan, Malaysia, Nepal, Netherlands, New Zealand) |
| Unique areas | 61 total |
| Countries | 59 |
| Regions | 2 |
| Data frequency | Monthly |
 
### Actual Schema (24 columns, verified)
 
| Column | Dtype | Notes |
|---|---|---|
| Area | object | Country/region name |
| ISO 3 code | object | ISO 3166 alpha-3 |
| Area type | object | 'Country or economy' or 'Region' |
| Date | datetime64 | First day of month |
| Data frequency | object | Verify: likely all 'Monthly' |
| Drivetrain | object | 10 unique values (8 individual + 2 aggregates) |
| Is aggregate drivetrain | bool | True for 'Electric vehicle (BEV+PHEV)' and 'All drivetrains' |
| Registrations | float64 | **Target variable** |
| Registrations YoY change | float64 | NaN for early months |
| Registrations YoY change (%) | float64 | NaN for early months |
| Share of registrations (%) | float64 | Within-country share |
| Year-to-date registrations | int64 | Cumulative |
| Year-to-date share of registrations (%) | float64 | |
| Rolling 3-month registrations | float64 | Bonus — not in original spec |
| Rolling 3-month share of registrations (%) | float64 | |
| Rolling 12-month registrations | float64 | |
| Rolling 12-month share of registrations (%) | float64 | |
| Continent | object | Bonus metadata |
| Ember region | object | Bonus metadata |
| EU member | object | **Needs conversion to bool** |
| OECD member | object | **Needs conversion to bool** |
| G20 member | object | **Needs conversion to bool** |
| G7 member | object | **Needs conversion to bool** |
| ASEAN member | object | **Needs conversion to bool** |
 
### Data Contract Rules
 
1. **Granularity:** one row per `(ISO 3 code, Date, Drivetrain)`.
2. **Primary key:** `(ISO 3 code, Date, Drivetrain)`. Duplicate count verified = [fill from cell 6].
3. **Target variable:** `Registrations`. NaN count = [fill from cell 5, expected 0].
4. **Aggregate exclusion:** rows where `Is aggregate drivetrain == True` (2,778 rows) are excluded from the training table and used only for share calculations.
5. **Training table size:** 34,092 rows across [fill from cell 2] country–drivetrain series.
6. **Never sum aggregates with individual drivetrains.** Never sum country rows with World or regional rows.
7. **Missing data policy:** absent drivetrains are set to zero by the publisher. Distinguish:
   - **Structural zero:** zero non-zero observations across entire history → exclude from modeling (12 series).
   - **Reporting zero:** at least one non-zero observation but zero in some months → retain, flag (66 series).
8. **Latest observation date varies by country.** Overall latest = 2026-10-01; [fill from cell 7] countries end before this.
9. **Membership flags** (`EU member`, etc.) must be converted from object to bool before modeling.
 
### Coverage Summary
 
- Training rows: 34,092
- Aggregate rows: 12,778
- Total country-drivetrain series: 316
- Structurally absent series: 12
- Series with reporting zeros: 66
- Series with <24 observations: 4
 
## Supporting Dataset: VehiclesDB (metadata only — not yet loaded)
 
[Keep the template from the previous message; this is Phase 0 optional.]
 
## Attribution Text (for UI footer)
 
> Registration data: Ember (ember-energy.org), CC BY 4.0.
> Vehicle metadata: VehiclesDB (vehiclesdb.com), CC BY 4.0.
> Inventory figures are synthetic demonstration data, not real dealer stock.