import matplotlib.pyplot as plt
from load_csv import load


def main():
    """
    Plots life expectancy vs GDP per capita for the year 1900 for each country.
    """
    income_data = load(
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    )
    life_expectancy_data = load("life_expectancy_years.csv")

    income_1900 = income_data[["country", "1900"]].rename(
        columns={"1900": "gdp_per_capita"}
    )
    life_expectancy_1900 = life_expectancy_data[["country", "1900"]].rename(
        columns={"1900": "life_expectancy"}
    )

    merged_data = income_1900.merge(life_expectancy_1900, on="country")
    merged_data.dropna(inplace=True)

    merged_data["gdp_per_capita"] = merged_data[
        "gdp_per_capita"
    ].apply(float)
    merged_data["life_expectancy"] = merged_data[
        "life_expectancy"
    ].apply(float)

    plt.figure(figsize=(10, 6))
    plt.scatter(
        merged_data["gdp_per_capita"],
        merged_data["life_expectancy"],
        alpha=0.7,
        edgecolors="k"
    )

    try:
        plt.title("1900")
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")
        plt.xscale('log')
        plt.xticks([300, 1000, 10000], ['300', '1K', '10K'])
        plt.grid(True, which="both", linestyle='--', linewidth=0.5)
        plt.tight_layout()
        plt.show()
    except KeyboardInterrupt:
        plt.close()


if __name__ == "__main__":
    main()
