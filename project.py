#!/usr/bin/env python3
"""
City Energy Consumption Analysis & Prediction System (single-file, corrected)

What this script does:
1) Generate a 1-year synthetic dataset for multiple zones
2) Analyze patterns (monthly averages, correlations, event vs non-event)
3) Create 3 matplotlib charts and save them as PNGs
4) Train/test a RandomForest model for next-day consumption per zone
5) Save artifacts: CSV dataset, charts, and trained model (joblib)
6) Provide an interactive CLI predictor: `python city_energy_system.py predict`

Usage examples:
- Analyze + train + export artifacts (default):
    python city_energy_system.py analyze --year 2024 --zones 5 --outdir ./artifacts

- Interactive predictor (loads model from outdir if present or trains on the fly):
    python city_energy_system.py predict --outdir ./artifacts

Notes:
- Uses only matplotlib for plots; no seaborn.
- Handles input validation and missing/inconsistent data.
- Next-day target is built by shifting EnergyConsumption by -1 within each zone.

Requirements:
    pip install numpy pandas matplotlib scikit-learn joblib
"""

from __future__ import annotations

import argparse
import os
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List, Tuple

import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


# -----------------------------
# Configuration & Data Classes
# -----------------------------

@dataclass
class GenConfig:
    year: int = 2024
    zones: int = 5
    seed: int = 42


# -----------------------------
# Data Generation
# -----------------------------

def generate_synthetic_data(cfg: GenConfig) -> pd.DataFrame:
    rng = np.random.default_rng(cfg.seed)
    start_date = datetime(cfg.year, 1, 1)
    end_date = datetime(cfg.year, 12, 31)
    days = (end_date - start_date).days + 1
    dates = [start_date + timedelta(days=i) for i in range(days)]

    zones = [f"Z{i}" for i in range(1, cfg.zones + 1)]
    rows: List[dict] = []

    for zone in zones:
        base_load = float(rng.uniform(1800, 2400))  # kWh baseline per day
        temp_sensitivity = float(rng.uniform(25, 45))  # kWh per °C above comfort
        humidity_sensitivity = float(rng.uniform(2, 6))  # kWh per % humidity (scaled
        weekend_uplift = float(rng.uniform(40, 100))
        event_uplift = float(rng.uniform(200, 450))

        for d in dates:
            day_of_year = (d - datetime(d.year, 1, 1)).days + 1

            # Seasonal temperature (°C) with noise; warmer mid-year
            temp = 22 + 10 * np.sin(2 * np.pi * (day_of_year - 120) / 365) + rng.normal(0, 2)

            # Humidity (%) inversely-ish related to temperature trend with noise
            humidity = 60 - 10 * np.sin(2 * np.pi * (day_of_year - 120) / 365) + rng.normal(0, 5)
            humidity = float(np.clip(humidity, 25, 95))

            is_weekend = int(d.weekday() >= 5)
            month = d.month

            # Events more likely on weekends and in festive months (Aug, Oct, Dec)
            base_event_prob = 0.04
            month_boost = 0.06 if month in (8, 10, 12) else 0.0
            weekend_boost = 0.05 if is_weekend else 0.0
            p_event = min(0.9, max(0.0, base_event_prob + month_boost + weekend_boost))
            event = int(rng.uniform() < p_event)

            # Nonlinear cooling load: only above 20°C
            cooling_load = max(0.0, float(temp) - 20.0)
            noise = float(rng.normal(0, 80))

            # Energy model; scale humidity effect sanely
            energy = (
                base_load
                + temp_sensitivity * cooling_load
                + humidity_sensitivity * (humidity - 40)  # center near 40% so low humid days don't explode
                + weekend_uplift * is_weekend
                + event_uplift * event
                + noise
            )
            energy = float(max(200.0, energy))  # clamp minimum

            rows.append(
                {
                    "Date": d.date(),
                    "ZoneID": zone,
                    "AvgTemperature": round(float(temp), 2),
                    "Humidity": round(float(humidity), 1),
                    "SpecialEvent": event,
                    "EnergyConsumption": round(energy, 2),
                }
            )

    df = pd.DataFrame(rows)

    # Add time-related helpers
    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.month
    df["Year"] = df["Date"].dt.year
    df["DayOfWeek"] = df["Date"].dt.dayofweek
    df["IsWeekend"] = (df["DayOfWeek"] >= 5).astype(int)

    return df


# -----------------------------
# Analysis & Visualization
# -----------------------------

def ensure_outdir(outdir: str) -> None:
    os.makedirs(outdir, exist_ok=True)


def analyze_and_visualize(df: pd.DataFrame, outdir: str) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    ensure_outdir(outdir)

    # Monthly averages (overall)
    monthly_avg = (
        df.groupby("Month")["EnergyConsumption"].mean().reset_index(name="AvgMonthlyConsumption")
    )

    # Zone-wise monthly averages
    zone_monthly_avg = (
        df.groupby(["ZoneID", "Month"])["EnergyConsumption"].mean().reset_index(name="AvgConsumption")
    )

    # Event vs. Non-Event averages
    event_vs_nonevent = df.groupby("SpecialEvent")["EnergyConsumption"].mean().reset_index()
    event_vs_nonevent["Label"] = event_vs_nonevent["SpecialEvent"].map({0: "No Event", 1: "Event"})
    event_vs_nonevent = event_vs_nonevent[["Label", "EnergyConsumption"]]

    # Save summary CSVs
    monthly_avg.to_csv(os.path.join(outdir, "monthly_avg.csv"), index=False)
    zone_monthly_avg.to_csv(os.path.join(outdir, "zone_monthly_avg.csv"), index=False)
    event_vs_nonevent.to_csv(os.path.join(outdir, "event_vs_non_event.csv"), index=False)

    # Correlation matrix (select numeric columns)
    corr = df[[
        "AvgTemperature",
        "Humidity",
        "SpecialEvent",
        "IsWeekend",
        "EnergyConsumption",
    ]].corr()

    # 1) Line chart: monthly energy usage trends
    plt.figure()
    plt.plot(monthly_avg["Month"], monthly_avg["AvgMonthlyConsumption"], marker="o")
    plt.title("Monthly Average Energy Consumption (Overall)")
    plt.xlabel("Month")
    plt.ylabel("Average Consumption (kWh)")
    plt.grid(True)
    plt.savefig(os.path.join(outdir, "chart_monthly_trend.png"), bbox_inches="tight", dpi=160)
    plt.close()

    # 2) Heatmap: correlation between features
    plt.figure()
    im = plt.imshow(corr.values, interpolation="nearest", aspect="auto")
    plt.title("Feature Correlation Heatmap")
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=45, ha="right")
    plt.yticks(range(len(corr.index)), corr.index)
    plt.colorbar(im, fraction=0.046, pad=0.04)
    plt.tight_layout()
    plt.savefig(os.path.join(outdir, "chart_correlation_heatmap.png"), bbox_inches="tight", dpi=160)
    plt.close()

    # 3) Bar chart: average usage on event vs non-event days
    plt.figure()
    x = np.arange(len(event_vs_nonevent))
    plt.bar(x, event_vs_nonevent["EnergyConsumption"].values)
    plt.xticks(x, event_vs_nonevent["Label"].values)
    plt.title("Average Energy Consumption: Event vs Non-Event Days")
    plt.ylabel("Average Consumption (kWh)")
    plt.grid(axis="y")
    plt.savefig(os.path.join(outdir, "chart_event_vs_nonevent.png"), bbox_inches="tight", dpi=160)
    plt.close()

    return monthly_avg, zone_monthly_avg, event_vs_nonevent


# -----------------------------
# Modeling
# -----------------------------

def build_training_frame(df: pd.DataFrame) -> pd.DataFrame:
    df_sorted = df.sort_values(["ZoneID", "Date"]).copy()
    df_sorted["TargetNextDay"] = df_sorted.groupby("ZoneID")["EnergyConsumption"].shift(-1)
    model_df = df_sorted.dropna(subset=["TargetNextDay"]).copy()
    return model_df


def train_model(df: pd.DataFrame, outdir: str) -> Tuple[Pipeline, float]:
    ensure_outdir(outdir)
    model_df = build_training_frame(df)

    X = model_df[["ZoneID", "AvgTemperature", "Humidity", "SpecialEvent"]]
    y = model_df["TargetNextDay"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=123
    )

    preprocess = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), ["ZoneID"]),
            ("num", "passthrough", ["AvgTemperature", "Humidity", "SpecialEvent"]),
        ]
    )

    model = Pipeline(
        steps=[
            ("preprocess", preprocess),
            ("rf", RandomForestRegressor(n_estimators=300, random_state=123)),
        ]
    )

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mae = float(mean_absolute_error(y_test, y_pred))

    # Save model
    import pickle
...
with open(model_path, "wb") as f:
    pickle.dump(model, f)

with open(model_path, "rb") as f:
    model = pickle.load(f)

# -----------------------------
# CLI Prediction
# -----------------------------

def validate_zone(z: str, zones: List[str]) -> str:
    if not isinstance(z, str):
        raise ValueError("Zone ID must be a string like 'Z1'..'Z5'.")
    z = z.strip().upper()
    if z not in zones:
        raise ValueError(f"Zone ID must be one of: {', '.join(zones)}.")
    return z


def validate_float(name: str, val: str, lo: float, hi: float) -> float:
    try:
        x = float(val)
    except Exception:
        raise ValueError(f"{name} must be a number.")
    if not (lo <= x <= hi):
        raise ValueError(f"{name} must be between {lo} and {hi}.")
    return x


def validate_event(val: str) -> int:
    val = val.strip()
    if val not in {"0", "1"}:
        raise ValueError("Event indicator must be 0 or 1.")
    return int(val)


def interactive_predict(model: Pipeline, zones: List[str]) -> None:
    print("\n=== Next-Day Energy Consumption Predictor ===")
    print("Enter ZoneID (e.g., Z1), Temperature (°C), Humidity (%), SpecialEvent (0/1).")
    while True:
        try:
            zone = validate_zone(input("Zone ID: "), zones)
            temp = validate_float("Temperature (°C)", input("Tomorrow's Avg Temperature (°C): "), -10.0, 55.0)
            hum = validate_float("Humidity (%)", input("Tomorrow's Humidity (%): "), 0.0, 100.0)
            evt = validate_event(input("Special Event? (0=No, 1=Yes): "))

            X_new = pd.DataFrame([
                {
                    "ZoneID": zone,
                    "AvgTemperature": temp,
                    "Humidity": hum,
                    "SpecialEvent": evt,
                }
            ])
            pred = float(model.predict(X_new)[0])
            print(f"Predicted next-day energy consumption for {zone}: {pred:.2f} kWh\n")
        except KeyboardInterrupt:
            print("\nExiting. Goodbye!")
            break
        except Exception as e:
            print(f"Input error: {e}\n")

        again = input("Predict again? (y/n): ").strip().lower()
        if again != "y":
            break


# -----------------------------
# Command Handlers
# -----------------------------

def cmd_analyze(args: argparse.Namespace) -> None:
    cfg = GenConfig(year=args.year, zones=args.zones, seed=args.seed)
    outdir = args.outdir
    ensure_outdir(outdir)

    print(f"Generating synthetic data for year {cfg.year} across {cfg.zones} zones...")
    df = generate_synthetic_data(cfg)

    dataset_path = os.path.join(outdir, "city_energy_dataset.csv")
    df.to_csv(dataset_path, index=False)
    print(f"Saved dataset: {dataset_path}")

    print("Creating analyses and charts...")
    analyze_and_visualize(df, outdir)
    print(f"Saved charts to: {outdir}")

    print("Training model (RandomForest)...")
    _, mae = train_model(df, outdir)
    print(f"Model trained. Hold-out MAE: {mae:.2f} kWh")
    print(f"Saved model to: {os.path.join(outdir, 'model_nextday.joblib')}")


def cmd_predict(args: argparse.Namespace) -> None:
    outdir = args.outdir
    ensure_outdir(outdir)

    model_path = os.path.join(outdir, "model_nextday.joblib")

    if os.path.exists(model_path):
        print(f"Loading existing model from {model_path}...")
        model: Pipeline = pickle.load(model_path)
        # Try to infer zones from encoder categories
        try:
            ohe = model.named_steps["preprocess"].named_transformers_["cat"]
            zones = [str(z) for z in ohe.categories_[0]]
        except Exception:
            zones = [f"Z{i}" for i in range(1, 6)]
    else:
        print("No saved model found. Generating data and training a new model on the fly...")
        cfg = GenConfig(year=args.year, zones=args.zones, seed=args.seed)
        df = generate_synthetic_data(cfg)
        model, _ = train_model(df, outdir)
        zones = [f"Z{i}" for i in range(1, cfg.zones + 1)]

    interactive_predict(model, zones)


# -----------------------------
# Main
# -----------------------------

def build_arg_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="City Energy Consumption Analysis & Prediction System (corrected single-file)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    sub = p.add_subparsers(dest="command", required=True)

    # analyze subcommand
    pa = sub.add_parser("analyze", help="Generate data, run analysis, create charts, train model")
    pa.add_argument("--year", type=int, default=2024, help="Year for data generation")
    pa.add_argument("--zones", type=int, default=5, help="Number of zones")
    pa.add_argument("--seed", type=int, default=42, help="Random seed")
    pa.add_argument("--outdir", type=str, default="./artifacts", help="Output directory for artifacts")
    pa.set_defaults(func=cmd_analyze)

    # predict subcommand
    pp = sub.add_parser("predict", help="Interactive console predictor using the trained model")
    pp.add_argument("--outdir", type=str, default="./artifacts", help="Directory where model is saved / will be saved")
    pp.add_argument("--year", type=int, default=2024, help="(Used only if training on the fly)")
    pp.add_argument("--zones", type=int, default=5, help="(Used only if training on the fly)")
    pp.add_argument("--seed", type=int, default=42, help="(Used only if training on the fly)")
    pp.set_defaults(func=cmd_predict)

    return p


if __name__ == "__main__":
    parser = build_arg_parser()
    args = parser.parse_args()
    args.func(args)
