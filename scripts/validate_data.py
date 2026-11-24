"""Validate the Ember monthly EV sales dataset against the data contract."""
import pandas as pd
import sys
 
RAW_PATH = "data/raw/monthly_ev_sales.csv"
 
REQUIRED_COLUMNS = [
    "Area", "ISO 3 code", "Area type", "Date", "Drivetrain",
    "Registrations", "Is aggregate drivetrain",
]
 
def main(path=RAW_PATH):
    df = pd.read_csv(path)
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
 
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        print(f"FAIL: missing columns {missing}")
        sys.exit(1)
 
    train = df[df["Is aggregate drivetrain"] == False]
    agg = df[df["Is aggregate drivetrain"] == True]
 
    print(f"Rows total: {len(df)}")
    print(f"Training rows (non-aggregate): {len(train)}")
    print(f"Aggregate rows: {len(agg)}")
    print(f"Date range: {df['Date'].min()} to {df['Date'].max()}")
    print(f"Countries: {train[train['Area type'] == 'Country or economy']['Area'].nunique()}")
    print(f"Drivetrains: {sorted(train['Drivetrain'].unique())}")
 
    latest = train.groupby("Area")["Date"].max().sort_values()
    print("\nOldest latest-observation dates:")
    print(latest.head(5))
 
    print("\nOK: dataset matches contract.")
    return df
 
if __name__ == "__main__":
    main()