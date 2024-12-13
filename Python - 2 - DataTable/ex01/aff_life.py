import matplotlib
import matplotlib.pyplot as plt
from load_csv import load


def main():
    """
    The function plots the life expectancy of France over the years.
    """
    all_data = load("life_expectancy_years.csv")

    france_data = all_data[all_data["country"] == "France"]

    france_data_melted = france_data.melt(
        id_vars=["country"],
        var_name="year",
        value_name="life_expectancy"
    )

    france_data_melted["year"] = france_data_melted["year"].astype(int)

    try:
        matplotlib.use('TkAgg')
        plt.plot(
            france_data_melted["year"],
            france_data_melted["life_expectancy"]
        )
        plt.title('France Life expectancy Projections')
        plt.xlabel('Year')
        plt.ylabel('Life expectancy')

        years = france_data_melted["year"].unique()
        plt.xticks(range(min(years), max(years)+1, 40))

        plt.show()
    except KeyboardInterrupt:
        plt.close()


if __name__ == "__main__":
    main()
