

def ft_filter(func: callable, lst: list):
    """Return an iterator yielding those items \
of iterable for which function(item)
is true. If function is None, return the items that are true."""
    for elem in lst:
        if func(elem):
            yield elem


if __name__ == "__main__":
    lst = [1, 5, 18, 1819]
    rst = ft_filter(lambda x: x < 18, lst)
    print(list(rst))  # sinon c est un filter object et non une liste
    # for x in rst:
    #     print(x)
