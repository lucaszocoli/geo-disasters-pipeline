import pandas as pd
from sqlalchemy import create_engine
from config.settings import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_DATABASE

def load_to_postgres():
    engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}")
    
    df = pd.read_csv("data/processed/all_disasters.csv")
    df.to_sql("disasters", engine, if_exists="append", index=False)
    
    print("Dados inseridos no PostgreSQL!")

if __name__ == "__main__":
    load_to_postgres()
