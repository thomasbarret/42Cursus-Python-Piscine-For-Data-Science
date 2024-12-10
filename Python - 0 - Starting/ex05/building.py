import sys


def main():
    """
    Analyze a given string and summarize its content.

    This function counts the number of uppercase letters, lowercase letters,
    punctuation marks, spaces, and digits in a string. The string is either
    provided as a command-line argument or entered via stdin if no arguments
    are passed.

    Behavior:
    - If no arguments: prompts the user for input.
    - If one argument: analyzes the provided string.
    - If more than one argument: raises an AssertionError.

    Output:
    Prints the total number of characters and their breakdown by type.

    Example:
    $ python script.py "Hello, World! 123"
    The text contains 17 characters:
    2 upper letters
    8 lower letters
    2 punctuation marks
    2 spaces
    3 digits
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
