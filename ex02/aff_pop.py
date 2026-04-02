import matplotlib.pyplot as plt
from load_csv import load


def convert_population(value):
    """
    Convert population values like '1.2M', '300k', '2B'
    into numeric values.
    """
    if isinstance(value, (int, float)):
        return float(value)
    if not isinstance(value, str):
        return None

    value = value.strip()

    try:
        if value.endswith("k"):
            return float(value[:-1]) * 1_000
        if value.endswith("M"):
            return float(value[:-1]) * 1_000_000
        if value.endswith("B"):
            return float(value[:-1]) * 1_000_000_000
        return float(value)
    except ValueError:
        return None


def main():
    data = load("population_total.csv")
    if data is None:
        return

    country1 = "Turkey"
    country2 = "France"

    country1_data = data[data["country"] == country1]
    country2_data = data[data["country"] == country2]

    if country1_data.empty or country2_data.empty:
        print("One or both countries not found")
        return

    years = [int(year) for year in data.columns[1:] if year.isdigit()]
    years = [year for year in years if 1800 <= year <= 2050]

    year_columns = [str(year) for year in years]

    values1 = [convert_population(country1_data.iloc[0][year]) for year in year_columns]
    values2 = [convert_population(country2_data.iloc[0][year]) for year in year_columns]

    plt.plot(years, values1, label=country1)
    plt.plot(years, values2, label=country2)

    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
