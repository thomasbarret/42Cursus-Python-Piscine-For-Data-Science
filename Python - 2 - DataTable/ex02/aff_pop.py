import matplotlib.pyplot as plt
from load_csv import load


def convert_to_int(value):
    conversion_factors = {'k': 1000, 'M': 1000000, 'B': 1000000000}
    if value[-1] in conversion_factors:
        return int(float(value[:-1]) * conversion_factors[value[-1]])
    else:
        return int(float(value))


def main():
    """
    The function plots the population projections
    for France and Belgium over the years.
    """
    all_data = load("population_total.csv")

    france_data = all_data[all_data["country"] == "France"]
    france_data_melted = france_data.melt(
        id_vars=["country"],
        var_name="year",
        value_name="population"
    )
    france_data_melted["year"] = france_data_melted["year"].astype(int)
    france_data_melted["population"] = france_data_melted[
        "population"
    ].apply(convert_to_int)

    belgium_data = all_data[all_data["country"] == "Belgium"]
    belgium_data_melted = belgium_data.melt(
        id_vars=["country"],
        var_name="year",
        value_name="population"
    )
    belgium_data_melted["year"] = belgium_data_melted["year"].astype(int)
    belgium_data_melted["population"] = belgium_data_melted[
        "population"
    ].apply(convert_to_int)

    try:
        plt.plot(
            france_data_melted["year"],
            france_data_melted["population"], label="France"
        )
        plt.plot(
            belgium_data_melted["year"],
            belgium_data_melted["population"],
            label="Belgium"
        )

        plt.yticks(
            range(
                0,
                max(france_data_melted["population"]) + 10_000_000, 20_000_000
            ),
            [f"{y // 1_000_000}M"
             for y in range(
                0,
                max(france_data_melted["population"])
                + 10_000_000, 20_000_000)]
            )

        plt.title('Population Projections')
        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.legend(loc="lower right")
        plt.show()
    except KeyboardInterrupt:
        plt.close()


if __name__ == "__main__":
    main()
