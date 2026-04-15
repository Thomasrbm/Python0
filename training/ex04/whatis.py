from sys import argv


def whatis(n):
    if not n.isdigit():
        raise AssertionError("argument is not an integer")
    if int(n) % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


def start():
    if len(argv) > 2:
        raise AssertionError("more than one argument is provided")
    elif len(argv) < 2:
        raise AssertionError("not enough arguments were provided")
    whatis(argv[1])


try:
    start()
except AssertionError as e:
    print(f"AssertionError: {e}")
