def ft_filter(func, iterable):
    """Filter elements of iterable using func, like the built-in filter."""
    if func is None:
        return [x for x in iterable if x]
    return [x for x in iterable if func(x)]