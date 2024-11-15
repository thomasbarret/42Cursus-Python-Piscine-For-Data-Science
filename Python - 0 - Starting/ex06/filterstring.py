from ft_filter import ft_filter
import sys


def main():
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        result = list(ft_filter(lambda x: len(x) > int(sys.argv[2]),
                                [world for world in sys.argv[1].split(" ")]))
        print(result)
    except (AssertionError, ValueError):
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
