import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Load a CSV file into a DataFrame.
    """
    df = pd.read_csv(path)

    print(f"Loading dataset of dimensions {df.shape}")
    return df
