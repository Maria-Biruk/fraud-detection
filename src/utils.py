import pandas as pd

def load_data(path):
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None