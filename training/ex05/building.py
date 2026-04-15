from sys import argv
import string


def building(text):
    """Count the number of x type char in a text"""
    upper = sum(1 for c in text if c.isupper())
    lower = sum(1 for c in text if c.islower())
    punctuation = sum(1 for c in text if c in string.punctuation)
    space = sum(1 for c in text if c in string.whitespace)
    digit = sum(1 for c in text if c.isdigit())

    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation mark")
    print(f"{space} spaces")
    print(f"{digit} digits")


def main():
    """Entry point."""
    try:
        if len(argv) != 2:
            raise AssertionError("Wrong number of arguments")
        building(argv[1])
    except Exception as e:
        print(f"Error : {e}")


if __name__ == "__main__":
    main()
