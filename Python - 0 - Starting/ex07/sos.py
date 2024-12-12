import sys


def main():
    """
    The function converts the provided string into Morse code.
    """
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")

        NESTED_MORSE = {
            " ": "/ ",
            "A": ".- ", "B": "-... ",
            "C": "-.-. ", "D": "-.. ",
            "E": ". ", "F": "..-. ",
            "G": "--. ", "H": ".... ",
            "I": ".. ", "J": ".--- ",
            "K": "-.- ", "L": ".-.. ",
            "M": "-- ", "N": "-. ",
            "O": "--- ", "P": ".--. ",
            "Q": "--.- ", "R": ".-. ",
            "S": "... ", "T": "- ",
            "U": "..- ", "V": "...- ",
            "W": ".-- ", "X": "-..- ",
            "Y": "-.-- ", "Z": "--.. ",
            "0": "----- ", "1": ".---- ",
            "2": "..--- ", "3": "...-- ",
            "4": "....- ", "5": "..... ",
            "6": "-.... ", "7": "--... ",
            "8": "---.. ", "9": "----. "
        }
        sentence = ""

        for letter in sys.argv[1]:
            if not letter.upper() in NESTED_MORSE:
                raise AssertionError("the arguments are bad")

            sentence += NESTED_MORSE[letter.upper()]

        print(sentence[:-1])
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
