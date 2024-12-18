from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Calculate and display statistics of given numeric arguments
    based on specified keywords.

    Parameters:
        *args (Any): Numeric arguments (int or float).
        **kwargs (Any): Keywords specifying the statistic to calculate.
            Supported keywords:
            - "mean": Calculate the mean.
            - "median": Calculate the median.
            - "quartile": Calculate the first and third quartiles.
            - "std": Calculate the standard deviation.
            - "var": Calculate the variance.

    Returns:
        None: Prints the results or an error message if inputs are invalid.
    """
    if len(args) == 0 or not all(isinstance(
            arg, (int, float)) for arg in args):
        print("ERROR")
        return

    data = sorted(args)

    results = []

    for key, value in kwargs.items():
        if value == "mean":
            mean = sum(data) / len(data)
            results.append(f"mean : {mean}")
        elif value == "median":
            median = calculate_median(data)
            results.append(f"median : {median}")
        elif value == "quartile":
            q1 = calculate_percentile(data, 25)
            q3 = calculate_percentile(data, 75)
            results.append(f"quartile : [{q1}, {q3}]")
        elif value == "std":
            std = calculate_std(data)
            results.append(f"std : {std}")
        elif value == "var":
            var = calculate_var(data)
            results.append(f"var : {var}")
        else:
            print("ERROR")
            return

    for result in results:
        print(result)


def calculate_median(data: list) -> float:
    """
    Calculate the median of a sorted list.

    Parameters:
        data (list): A sorted list of numbers.

    Returns:
        float: The median value.
    """
    n = len(data)
    if n % 2 == 0:
        return (data[n // 2 - 1] + data[n // 2]) / 2
    return data[n // 2]


def calculate_percentile(data: list, percentile: int) -> float:
    """
    Calculate a specific percentile of a sorted list.

    Parameters:
        data (list): A sorted list of numbers.
        percentile (int): The desired percentile (0-100).

    Returns:
        float: The calculated percentile value.
    """
    index = (len(data) - 1) * (percentile / 100)
    lower = int(index)
    upper = min(lower + 1, len(data) - 1)
    weight = index - lower
    return data[lower] * (1 - weight) + data[upper] * weight


def calculate_var(data: list) -> float:
    """
    Calculate the variance of a list of numbers.

    Parameters:
        data (list): A list of numbers.

    Returns:
        float: The variance.
    """
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)


def calculate_std(data: list) -> float:
    """
    Calculate the standard deviation of a list of numbers.

    Parameters:
        data (list): A list of numbers.

    Returns:
        float: The standard deviation.
    """
    return calculate_var(data) ** 0.5
