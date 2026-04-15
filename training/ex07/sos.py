from sys import argv


NESTED_MORSE = {
    "A": ".-",    "B": "-...",  "C": "-.-.",
    "D": "-..",   "E": ".",     "F": "..-.",
    "G": "--.",   "H": "....",  "I": "..",
    "J": ".---",  "K": "-.-",   "L": ".-..",
    "M": "--",    "N": "-.",    "O": "---",
    "P": ".--.",  "Q": "--.-",  "R": ".-.",
    "S": "...",   "T": "-",     "U": "..-",
    "V": "...-",  "W": ".--",   "X": "-..-",
    "Y": "-.--",  "Z": "--.."
}


def sos(text: str):
    """print the given text traduced into Morse"""
    mots = text.split()
    resultat = []
    for i in mots:
        for c in i:
            resultat.append(NESTED_MORSE[c.upper()])
    print(*resultat, sep=" ")  # le * ca unpack la list (envoit elem 1 par 1)


def main():
    """entry point"""
    try:
        if len(argv) != 2:
            raise AssertionError("the arguments are bad")
        if not argv[1].replace(" ", "").isalpha():
            raise AssertionError("the arguments are bad")
        sos(argv[1])
    except Exception as e:
        print(f"error : {e}")


if __name__ == "__main__":
    main()
