from morse_code.functions.morse import MORSE_CODE_TO_LETTER as ML, LETTER_TO_MORSE_CODE as LM

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
