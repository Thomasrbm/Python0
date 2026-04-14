def ft_tqdm(lst: range) -> None:
    """Replicate tqdm progress bar using yield."""
    total = len(lst)
    bar_width = 65
    for i, elem in enumerate(lst):
        filled = int(bar_width * (i + 1) / total)
        bar = "=" * filled + ">" if filled < bar_width else "=" * bar_width
        percent = int(100 * (i + 1) / total)
        print(f"\r{percent}%|[{bar:<{bar_width}}]| {i+1}/{total}", end="", flush=True)
        yield elem