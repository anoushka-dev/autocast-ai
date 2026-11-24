# Dataset Sources and Data Contract
 
## Primary Dataset: Ember Monthly EV Sales
 
| Field | Value |
|---|---|
| Publisher | Ember (ember-energy.org) |
| Source URL | https://ember-energy.org/data/monthly-ev-sales-data/ |
| File downloaded | [exact filename from Colab, e.g. ember_monthly_ev_sales.csv] |
| License | CC BY 4.0 — attribution required |
| Download date | [YYYY-MM-DD] |
| Latest observation date (overall) | [max Date from Colab] |
| Earliest observation date | [min Date from Colab] |
| Countries covered | [nunique of Area where Area type == "Country or economy"] |
| Regions covered | [list EU, World, etc.] |
| Drivetrain categories | [list from Colab: Battery electric, Plug-in hybrid, ...] |
 
### Schema (actual, verified from Colab)
 
| Column | Dtype | Description |
|---|---|---|
| [paste actual column names and dtypes] | | |
 
### Data Contract Rules
 
1. **Granularity:** one row per `(Area, ISO 3 code, Date, Drivetrain)`.
2. **Primary key:** `(ISO 3 code, Date, Drivetrain)`.
3. **Target variable:** `Registrations` (integer count).
4. **Aggregate exclusion:** rows where `Is aggregate drivetrain == True` (i.e., `All drivetrains` and `Electric vehicle (BEV+PHEV)`) are **excluded from the training table** and used only for share calculations.
5. **Never sum aggregates with individual drivetrains.**
6. **Never sum country rows with `World` or regional rows.**
7. **Missing data policy:** absent drivetrains are set to zero by the publisher. Distinguish:
   - **Structural zero:** series has zero non-zero observations across its entire history → exclude from modeling.
   - **Reporting zero:** series has at least one non-zero observation but zero in some months → retain, flag in data-quality report.
8. **Latest observation date varies by country.** Always store per-series latest date; never assume a single global end date.
 
### Coverage Summary (from Colab)
 
- Total rows: [n]
- Training rows (non-aggregate): [n]
- Aggregate rows: [n]
- Series with < 24 observations: [n]
- Structurally absent series (all zeros): [n]
- Series with reporting zeros: [n]
 
---
 
## Supporting Dataset: VehiclesDB (metadata only)
 
| Field | Value |
|---|---|
| Publisher | VehiclesDB |
| Source URL | https://huggingface.co/datasets/vehiclesdb/vehiclesdb |
| License | CC BY 4.0 — attribution: "Vehicle data by VehiclesDB" + link to vehiclesdb.com |
| Use | Vehicle make/model/body-type catalogue for UI enrichment |
| **Not for** | Sales quantities — it is a catalogue, not a sales dataset |
 
## Optional Dataset: tco-india (unverified)
 
Status: [Verified / Unverified / Dropped — reason]
 
## Attribution Text (for UI footer)
 
> Registration data: Ember (ember-energy.org), CC BY 4.0.
> Vehicle metadata: VehiclesDB (vehiclesdb.com), CC BY 4.0.
> Inventory figures are synthetic demonstration data, not real dealer stock.