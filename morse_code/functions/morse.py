"""Logic and interuppetation of Morse Code"""
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
            output += "/"
            continue
        try:
            output += f"{LETTER_TO_MORSE_CODE[letter]} "
        except KeyError:
           return None
    return output.rstrip()

def decode(msg: str) -> None | str:
    output: str = ""
    inter: str = ""
    for morse in msg:
        if len(inter) > MORSE_CODE_MAX_OPCODE:
            return None
        if morse == " ":
            output += MORSE_CODE_TO_LETTER[inter]
            inter = ""
            continue
        inter += morse
    return output
