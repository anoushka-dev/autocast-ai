"""Validate the Ember monthly EV sales dataset against the data contract."""
import sys
from pathlib import Path

import pandas as pd

RAW_PATH = Path("data/raw/monthly_ev_sales.csv")

REQUIRED_COLUMNS = [
    "Area", "ISO 3 code", "Area type", "Date", "Drivetrain",
    "Registrations", "Is aggregate drivetrain",
]


def main(path: Path = RAW_PATH) -> None:
    if not path.exists():
        print(f"FAIL: {path} not found. Place the Ember CSV there.")
        sys.exit(1)

    df = pd.read_csv(path)
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        print(f"FAIL: missing columns {missing}")
        sys.exit(1)

    if df["Date"].isna().any():
        print(f"FAIL: {df['Date'].isna().sum()} unparseable dates")
        sys.exit(1)

    train = df[df["Is aggregate drivetrain"] == False]
    agg = df[df["Is aggregate drivetrain"] == True]

    countries = train[train["Area type"] == "Country or economy"]["Area"].nunique()
    regions = train[train["Area type"] == "Region"]["Area"].nunique()

    print(f"Rows total:                   {len(df)}")
    print(f"Training rows (non-aggregate):{len(train)}")
    print(f"Aggregate rows:               {len(agg)}")
    print(f"Date range:                   {df['Date'].min().date()} to {df['Date'].max().date()}")
    print(f"Countries:                    {countries}")
    print(f"Regions:                      {regions}")
    print(f"Drivetrains (individual):      {sorted(train['Drivetrain'].unique())}")
    print(f"NaN in Registrations:         {train['Registrations'].isna().sum()}")

    dup = train.duplicated(["ISO 3 code", "Date", "Drivetrain"]).sum()
    print(f"Duplicate (ISO3, Date, Drivetrain): {dup}")
    if dup > 0:
        print("FAIL: duplicates violate the primary key")
        sys.exit(1)

    print("\nOK: dataset matches contract.")


if __name__ == "__main__":
    main()