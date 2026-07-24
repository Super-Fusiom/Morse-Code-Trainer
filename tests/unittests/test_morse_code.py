from morse_code.functions.morse import LETTER_TO_MORSE_CODE as LM
from morse_code.functions.morse import MORSE_CODE_TO_LETTER as ML
from morse_code.functions.morse import decode, encode


def test_letter_conversion() -> None:
    assert ML["-"] == "T"
    assert ML["..."] == "S"
    assert ML["--.."] == "Z"
    assert ML[".--"] == "W"

    assert ML["...."] + ML["."] + ML[".-.."] + ML[".-.."] + ML["---"] == "HELLO"

def test_morse_code_conversion() -> None:
    assert LM["A"] == ".-"
    assert LM["E"] == "."
    assert LM["O"] == "---"
    assert LM["Q"] == "--.-"

    message: str = ".-- --- .-. .-.. -..".replace(" ", "")

    assert message == LM["W"] + LM["O"] + LM["R"] + LM["L"] + LM["D"]

def test_encoding() -> None:
    message: str = "SWIPE"
    assert encode(message) == "... .-- .. .--. ."

    assert encode(" ") is None
    assert encode("123") is None
    assert encode("``~~``") is None
    assert encode("") is None

    assert encode("World") == ".-- --- .-. .-.. -.."
    assert encode("     World") == ".-- --- .-. .-.. -.."
    assert encode("World     ") == ".-- --- .-. .-.. -.."

    assert encode("Hi World") == ".... ../.-- --- .-. .-.. -.."


def test_decoding() -> None:
    message: str = "... .-- .. .--. ."
    assert decode(message) == "SWIPE"

    assert decode("SWIPE") is None
    assert decode("........") is None

    assert decode(".--") == "W"
    assert decode(f"{message}/.--") == "SWIPE W"
    assert decode(f"     {message}/.--") == "SWIPE W"
    assert decode(f"     {message}/.--     ") == "SWIPE W"
    assert decode(f"{message}/.--     ") == "SWIPE W"
