import sys
import string


def count_chars(text):
    """Count and print character statistics for a given string."""
    upper = sum(1 for c in text if c.isupper())
    lower = sum(1 for c in text if c.islower())
    punct = sum(1 for c in text if c in string.punctuation)
    spaces = sum(1 for c in text if c in string.whitespace)
    digits = sum(1 for c in text if c.isdigit())

    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punct} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    """Entry point for building.py."""
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        if len(sys.argv) == 2:
            text = sys.argv[1]
        else:
            print("What is the text to count?")
            text = input()
        count_chars(text)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()