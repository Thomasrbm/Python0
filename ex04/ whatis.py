import sys

def whatis():
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
    if len(sys.argv) == 2:
        try:
            n = int(sys.argv[1])
        except ValueError:
            raise AssertionError("argument is not an integer")
        print("I'm Even." if n % 2 == 0 else "I'm Odd.")

if __name__ == "__main__":
    try:
        whatis()
    except AssertionError as e:
        print(f"AssertionError: {e}")