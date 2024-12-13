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

    income_1900 = income_data[
        ["country", "1900"]].rename(columns={"1900": "gdp_per_capita"})
    life_expectancy_1900 = life_expectancy_data[
        ["country", "1900"]].rename(columns={"1900": "life_expectancy"})

    merged_data = income_1900.merge(life_expectancy_1900, on="country")

    merged_data.dropna(inplace=True)

    merged_data["gdp_per_capita"] = merged_data[
        "gdp_per_capita"].apply(float)
    merged_data["life_expectancy"] = merged_data[
        "life_expectancy"].apply(float)

    plt.figure(figsize=(10, 6))
    plt.scatter(
        merged_data["gdp_per_capita"],
        merged_data["life_expectancy"],
        alpha=0.7,
        edgecolors="k"
    )

    # Annotate each country
    # for _, row in merged_data.iterrows():
    #     plt.text(
    #         row["gdp_per_capita"], row["life_expectancy"], row["country"],
    #         fontsize=8, alpha=0.7
    #     )

    # Add title and labels
    try:
        plt.title("Life Expectancy vs GDP per Capita (1900)")
        plt.xlabel("GDP per Capita (1900, in PPP-adjusted USD)")
        plt.ylabel("Life Expectancy (1900, in years)")
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    except KeyboardInterrupt:
        plt.close()


if __name__ == "__main__":
    main()
