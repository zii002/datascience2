import matplotlib.pyplot as plt
from load_csv import load


def main():
    income_data = load(
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    )
    life_data = load("life_expectancy_years.csv")

    if income_data is None or life_data is None:
        return

    year = "1900"

    if year not in income_data.columns or year not in life_data.columns:
        print("Year not found")
        return

    # aynı sırada ülkeleri almak için merge yerine index align
    income_data = income_data.set_index("country")
    life_data = life_data.set_index("country")

    common_countries = income_data.index.intersection(life_data.index)

    gdp_values = income_data.loc[common_countries, year]
    life_values = life_data.loc[common_countries, year]

    plt.scatter(gdp_values, life_values)

    plt.xscale("log")
    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
