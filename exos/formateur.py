


def format_euro(nb : int) -> str :
    euro = str(nb)
    euro += ".00 €"
    return euro


if __name__ == "__main__" :
    print(f"test = {format_euro(10)}")