import matplotlib.pyplot as plt
from load_csv import load


def main():
    data = load("life_expectancy_years.csv")
    if data is None:
        return

    # Türkiye verisini al
    country = "Turkey"
    country_data = data[data["country"] == country]

    if country_data.empty:
        print("Country not found")
        return

    # yılları ve değerleri çek
    years = country_data.columns[1:]
    values = country_data.iloc[0, 1:].values

    # grafiği çiz
    plt.plot(years, values)

    plt.title(f"{country} Life Expectancy")
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy")

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
