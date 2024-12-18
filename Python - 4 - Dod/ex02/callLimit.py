from typing import Any, Callable


def callLimit(limit: int):
    """Limit the number of times a function can be called."""
    def callLimiter(function: Callable) -> Callable:
        count = 0

        def limit_function(*args: Any, **kwds: Any):
            """Call function if under limit, else print error."""
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: {function} call too many times")

        return limit_function

    return callLimiter
