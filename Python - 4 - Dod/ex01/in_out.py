def square(x: int | float) -> int | float:
    """
    Returns the square of x.

    :param x: An integer or float.
    :return: The square of x.
    """
    return x * x


def pow(x: int | float) -> int | float:
    """
    Returns x raised to the power of x.

    :param x: An integer or float.
    :return: x raised to the power of x.
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Returns a callable object that applies the function
    to x with increasing powers.

    :param x: An integer or float.
    :param function: A function to apply to x.
    :return: A callable object.
    """
    count = 1

    def inner() -> float:
        """
        Applies function to x and raises the result to the power of count.

        :return: The result of function(x) raised to the power of count.
        """
        nonlocal count
        result = function(x)
        for _ in range(count - 1):
            result = function(result)
        count += 1
        return result

    return inner
