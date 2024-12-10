import sys


def ft_tqdm(lst: range) -> None:
    """
    A simple progress bar for the terminal.
    """
    total = len(lst)
    bar_length = 60

    for i, number in enumerate(lst, 1):
        percent = i / total
        filled = int(bar_length * percent)

        bar = "=" * filled + ">" + " " * (bar_length - filled)

        sys.stdout.write(f"\r{int(percent * 100)}%|[{bar}]| {i}/{total}")
        sys.stdout.flush()

        yield number
