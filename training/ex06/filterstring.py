from ft_filter import ft_filter
from sys import argv


def filterstring(s: str, n: int):
    """filter the string that len are great than n"""
    lst = [mot for mot in s.split()]
    return list(ft_filter(lambda x: len(x) > int(n), lst))


def main():
    """entry point"""
    # print(filter.__doc__)
    # print(ft_filter.__doc__)
    try:
        if len(argv) != 3:
            raise AssertionError("the arguments are bad")
        if not argv[2].isdigit():
            raise AssertionError("the arguments are bad")
        if not argv[1].replace(" ", "").isalpha():
            raise AssertionError("the arguments are bad")
        print(filterstring(argv[1], argv[2]))
    except Exception as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
