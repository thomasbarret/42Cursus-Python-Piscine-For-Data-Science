from typing import Any
import numpy as np


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    This function takes a list of numbers and a list of keywords.
    The function calculates the statistics of the numbers
    and prints the results.
    """

    if len(args) == 0 or not all(isinstance(
                arg, (int, float)
            ) for arg in args):
        print("ERROR")
        return

    data = np.array(args)

    results = []
    for key, value in kwargs.items():
        if value == "mean":
            mean = np.mean(data)
            results.append(f"mean : {mean}")
        elif value == "median":
            median = np.median(data)
            results.append(f"median : {median}")
        elif value == "quartile":
            q1 = np.percentile(data, 25)
            q3 = np.percentile(data, 75)
            results.append(f"quartile : [{q1}, {q3}]")
        elif value == "std":
            std = np.std(data)
            results.append(f"std : {std}")
        elif value == "var":
            var = np.var(data)
            results.append(f"var : {var}")
        else:
            print("ERROR")
            return

    for result in results:
        print(result)
