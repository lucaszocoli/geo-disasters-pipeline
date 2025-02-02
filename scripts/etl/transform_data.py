import pandas as pd
import glob

def transform_data():
    processed_files = glob.glob("data/processed/*.csv")
    all_data = []

    for file in processed_files:
        df = pd.read_csv(file)
        df["time"] = pd.to_datetime(df["time"])
        df["magnitude"] = df["magnitude"].fillna(0)
        all_data.append(df)

    return pd.concat(all_data, ignore_index=True)

if __name__ == "__main__":
    df = transform_data()
    df.to_csv("data/processed/all_disasters.csv", index=False)
    print("Dados transformados e unificados!")
