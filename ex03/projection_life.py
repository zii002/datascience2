import matplotlib.pyplot as plt
from load_csv import load


def main():
    """
    Load the income and life expectancy datasets and display
    the life expectancy projection in relation to gross
    national product for the year 1900.
    """
    income_data = load(
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    )
    life_data = load("life_expectancy_years.csv")
    if income_data is None or life_data is None:
        return

    merged_data = income_data.merge(life_data, on="country")
    year = "1900"

    if year + "_x" not in merged_data.columns or year + "_y" not in merged_data.columns:
        print("Year 1900 not found in datasets")
        return

    gdp_values = merged_data[year + "_x"]
    life_values = merged_data[year + "_y"]

    plt.scatter(gdp_values, life_values)
    plt.xscale("log")
    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
