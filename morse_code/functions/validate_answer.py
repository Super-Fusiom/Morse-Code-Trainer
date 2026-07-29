"""Check if the given inputs are correct"""
from morse_code.functions.morse import decode, encode


def encode_question_check(question: str, answer: str) -> bool:
    return question == decode(answer)

def decode_question_check(question: str, answer: str) -> bool:
    return question == encode(answer)
