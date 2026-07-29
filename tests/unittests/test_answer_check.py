from morse_code.functions.validate_answer import (
    decode_question_check,
    encode_question_check,
)


def test_decoding_question_validation() -> None:
    assert encode_question_check("E", ".") == True
    assert encode_question_check("G", "..-") == False

def test_encoding_question_validation() -> None:
    assert decode_question_check(".", "E") == True
    assert decode_question_check(".--.", "P") == True
