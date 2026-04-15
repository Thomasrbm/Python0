from time import sleep


def ft_tqdm(lst: range) -> None:
    """ print a loading bar """
    length = len(lst)
    bar_max_len = 65
    for i in lst:
        filled = (i + 1) * bar_max_len / length
        pourcentage = (i + 1) * 100 / length
        bar = "=" * int(filled) + '>'
        print(f"\r{int(pourcentage)}%|{bar:<{bar_max_len}}| \
              {i + 1}/{length}", end="")
        sleep(0.005)
    yield 1
