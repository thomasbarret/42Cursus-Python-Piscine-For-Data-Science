import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    if not isinstance(family, list):
        raise ValueError("The 'family' parameter must be a list.")

    np_family = np.array(family)

    if np_family.ndim != 2:
        raise ValueError("The 'family' list must be a 2D list.")

    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("The 'start' and 'end' parameters must be integers.")

    print(f"My shape is : {np_family.shape}")

    np_family = np_family[start:end, :]

    print(f"My new shape is : {np_family.shape}")

    return np_family.tolist()
