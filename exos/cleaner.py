


def nettoyer(text : str) :
    return text.replace(" ", "")


if __name__ == "__main__" :
    res = input("input text : ")
    print(nettoyer(res))