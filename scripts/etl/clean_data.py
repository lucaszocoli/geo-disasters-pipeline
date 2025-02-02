import pandas as pd
import glob

def clean_csv_files():
    raw_files = glob.glob("data/raw/*.csv")
    for file in raw_files:
        df = pd.read_csv(file)
        df.dropna(subset=["latitude", "longitude"], inplace=True)
        df.to_csv(file.replace("raw", "processed"), index=False)
        print(f"Arquivo {file} limpo e salvo!")

if __name__ == "__main__":
    clean_csv_files()
