import sys
from ft_filter import ft_filter


def filterstring(s, n):
    """Return words from s with length greater than n."""
    words = s.split(" ")
    return ft_filter(lambda w: len(w) > n, words)


def main():
    """Entry point for filterstring.py."""
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        if not isinstance(sys.argv[1], str):
            raise AssertionError("the arguments are bad")
        try:
            n = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")
        s = sys.argv[1]
        if isinstance(s, int) or not isinstance(n, int):
            raise AssertionError("the arguments are bad")
        print(filterstring(s, n))
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()