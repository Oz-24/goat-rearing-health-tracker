import os
import numpy as np
import pandas as pd


def generate_goat_data(filename="data/goat_ledger.csv"):
    """Simulates a simple 10-goat tracking ledger."""
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Fixed seed for reproducible data vectors
    np.random.seed(50)

    goat_ids = [f"Goat_{i:03d}" for i in range(1, 11)]
    breeds = [
        "Ewu igbo",
        "Ewu ideke",
        "Ewu igbo",
        "Ewu ofia",
        "Ewu ofia",
        "Ewu igbo",
        "Ewu ideke",
        "Ewu hausa",
        "Ewu igbo",
        "Ewu hausa",
    ]

    # Generate daily feed intake in kg (typically 1.5kg to 3.5kg)
    feed_intake = np.round(np.random.uniform(1.5, 3.5, size=len(goat_ids)), 2)

    # Generate daily weight gain in kg (typically 0.1kg to 0.4kg)
    weight_gain = np.round(np.random.uniform(0.1, 0.4, size=len(goat_ids)), 2)

    # Introduce missing data: 2 weight gain records were missed during weighing
    weight_gain[2] = np.nan
    weight_gain[7] = np.nan

    # Create the DataFrame grid
    df = pd.DataFrame(
        {
            "Goat_ID": goat_ids,
            "Breed": breeds,
            "Feed_Consumed_KG": feed_intake,
            "Weight_Gain_KG": weight_gain,
        }
    )

    df.to_csv(filename, index=False)
    print(f"Raw livestock tracking logs saved to: {filename}")


def process_herd_metrics(filename="data/goat_ledger.csv"):
    """Cleans livestock metrics and applies vectorized logic to assess animal health."""
    # 1. Pandas: Load the dataset
    df = pd.read_csv(filename)

    # 2. Pandas: Impute Missing Data
    # Fill missing weight gains with the herd median value to fix data gaps
    median_gain = df["Weight_Gain_KG"].median()
    df["Weight_Gain_KG"] = df["Weight_Gain_KG"].fillna(median_gain)

    # 3. NumPy: Vectorized Financial/Biological Calculations
    # Extract columns to native arrays for fast computing
    feed_arr = df["Feed_Consumed_KG"].to_numpy()
    gain_arr = df["Weight_Gain_KG"].to_numpy()

    # Calculate Feed Conversion Ratio (FCR = Feed Eaten / Weight Gained)
    # Lower FCR means the animal is highly efficient at converting feed to mass.
    df["Feed_Conversion_Ratio"] = np.round(feed_arr / gain_arr, 2)

    # 4. NumPy: Conditional Health Flag Mask
    # If a goat has an FCR greater than 15 (eating a lot but barely gaining weight), flag it for a health check.
    fcr_arr = df["Feed_Conversion_Ratio"].to_numpy()
    df["Health_Status"] = np.where(fcr_arr > 15.0, "MEDICAL CHECK", "HEALTHY")

    # 5. Descriptive Herd Statistics via NumPy
    herd_stats = {
        "Total Daily Feed Herd Cost (KG)": np.sum(feed_arr),
        "Average Herd FCR Efficiency": np.mean(fcr_arr),
        "Highest Weight Gain Record": np.max(gain_arr),
    }

    # 6. Pandas: Breed Performance Aggregation
    breed_summary = (
        df.groupby("Breed")["Feed_Conversion_Ratio"].mean().to_dict()
    )

    return df, herd_stats, breed_summary


if __name__ == "__main__":
    # Execute the livestock data pipeline
    generate_goat_data()
    processed_df, general_stats, breed_splits = process_herd_metrics()

    print("\n--- PROCESSED GOAT HERD HEALTH REGISTRY ---")
    print(
        processed_df[
            [
                "Goat_ID",
                "Breed",
                "Feed_Consumed_KG",
                "Weight_Gain_KG",
                "Feed_Conversion_Ratio",
                "Health_Status",
            ]
        ]
    )

    print("\n--- HERD-WIDE EVALUATION TOTALS ---")
    for metric, score in general_stats.items():
        print(f"{metric}: {score:.2f}")

    print("\n--- AVG FEED EFFICIENCY (FCR) BY BREED SUMMARY ---")
    print("(Note: Lower FCR means better efficiency)")
    for breed, avg_fcr in breed_splits.items():
        print(f"{breed}: {avg_fcr:.2f}")
