MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'H': '....', 'I': '..', 'L': '.-..',
    'O': '---', 'R': '.-.', 'S': '...', 'T': '-',
    ' ': '/'
}

def to_morse(s):
    result = ""
    for i in s:
        if i in MORSE and i != None:
            result += MORSE[i] + " "
    return result 
    


print(to_morse("SOS"))
print(to_morse("HELLO"))
print(to_morse("HI THERE"))