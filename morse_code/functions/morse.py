"""Logic and interuppetation of Morse Code"""

from random import choice

MORSE_CODE_MAX_OPCODE = 5

LETTER_TO_MORSE_CODE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
}

MORSE_CODE_TO_LETTER = {
    code: letter
    for letter, code in LETTER_TO_MORSE_CODE.items()
}


def encode(msg: str) -> None | str:
    msg = msg.lstrip()
    msg = msg.rstrip()
    msg = msg.upper()
    if len(msg) < 1:
        return None
    output: str = ""
    for letter in msg:
        if letter == " ":
            output = output.rstrip()
            output += "/"
            continue
        try:
            output += f"{LETTER_TO_MORSE_CODE[letter]} "
        except KeyError:
           return None
    return output.rstrip()

def decode(msg: str) -> None | str:
    msg = msg.lstrip()
    msg = msg.rstrip()
    output: str = ""
    inter: str = ""
    for i in range(len(msg)):
        if len(inter) > MORSE_CODE_MAX_OPCODE:
            return None
        # Case for last letter decode
        if i == len(msg) - 1:
            inter += msg[i]
            try:
                output += MORSE_CODE_TO_LETTER[inter]
                continue
            except KeyError:
                return None
        if msg[i] == "/":
            try:
                output += MORSE_CODE_TO_LETTER[inter]
            except KeyError:
                return
            inter = ""
            output += " "
            continue
        if msg[i] == " ":
            try:
                output += MORSE_CODE_TO_LETTER[inter]
            except KeyError:
                return None
            inter = ""
            continue
        inter += msg[i]

    return output

def randomise_morse() -> str:
    return choice(list(MORSE_CODE_TO_LETTER))

def randomise_letter() -> str:
    return choice(list(LETTER_TO_MORSE_CODE))
