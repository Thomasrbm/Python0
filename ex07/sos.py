import sys

NESTED_MORSE = {
    " ": "/", "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
    "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..",
    "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.",
    "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...",
    "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..", "0": "-----", "1": ".----",
    "2": "..---", "3": "...--", "4": "....-", "5": ".....",
    "6": "-....", "7": "--...", "8": "---..", "9": "----.",
}


def encode_morse(text):
    """Encode a string into Morse code."""
    return " ".join(NESTED_MORSE[c.upper()] for c in text)


def main():
    """Entry point for sos.py."""
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")
        text = sys.argv[1]
        if not all(c.upper() in NESTED_MORSE for c in text):
            raise AssertionError("the arguments are bad")
        print(encode_morse(text))
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()