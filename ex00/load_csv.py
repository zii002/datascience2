import pandas as pd


def load(path: str):
    """
    Load a CSV dataset, print its dimensions, and return the dataset.
    Returns None if an error occurs.
    """
    try:
        data = pd.read_csv(path)
        print(f"Loading dataset of dimensions {data.shape}")
        return data
    except Exception:
        print("Error: could not load dataset")
        return None


def main():
    data = load("life_expectancy_years.csv")
    if data is not None:
        print(data.head())


if __name__ == "__main__":
    main()
