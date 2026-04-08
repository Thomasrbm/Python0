def count_in_list(lst: list, item: str) -> int:
    """Count occurrences of item in lst."""
    return sum(1 for x in lst if x == item)