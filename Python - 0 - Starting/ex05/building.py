import sys


def main():
    """
    A faire
    """
    try:
        if len(sys.argv) == 1:
            print("What is the text to count?")
            sentence = sys.stdin.readline().strip()
        elif len(sys.argv) == 2:
            sentence = sys.argv[1]
        else:
            raise AssertionError("more than one argument is provided")

        upper = 0
        lower = 0
        punctuation = 0
        space = 0
        digit = 0

        for char in sentence:
            if char.isupper():
                upper += 1
            elif char.islower():
                lower += 1
            elif char in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
                punctuation += 1
            elif char.isspace():
                space += 1
            elif char.isdigit():
                digit += 1

        print(f"The text contains {len(sentence)} characters:")
        print(f"{upper} upper letters")
        print(f"{lower} lower letters")
        print(f"{punctuation} punctuation marks")
        print(f"{space} spaces")
        print(f"{digit} digits")

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
