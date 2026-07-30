"""Storing session data for statictical data"""
from dataclasses import dataclass, field


@dataclass
class QuestionSessionData:
    questions_correct: list[bool] = field(default_factory=list)
    question_times: list[float] = field(default_factory=list)
