"""Visual Mode for trainer"""
from time import perf_counter

from textual import on
from textual.containers import Container
from textual.reactive import reactive
from textual.screen import Screen
from textual.widgets import Button, Label

from morse_code.functions.morse import randomise_letter
from morse_code.functions.validate_answer import (
    encode_question_check,
)


class VisualWelcome(Screen):
    def compose(self):
        yield Container(
            Label("""
            The visual trainer will show you either morse code or letter for you to encode or decode.
            Depending on what you want to do.\n
            Make sure you know what the controls for short and long beeps are if you are encoding.\n
            (See settings for key binds)
            """),
            Label("Are you ready?"),
            Button("Encode GO!", id="encode"),
            Button("Decode GO!", id="decode"),
            Button("Yea nah", id="main_menu_exit")
        )
    @on(Button.Pressed, "#main_menu_exit")
    def exit_pressed(self):
        self.app.switch_screen("menu")

    @on(Button.Pressed, "#encode")
    def encode_pressed(self):
        self.app.get_screen("visual_encode").reset_session()

        self.app.switch_screen("visual_encode")

    @on(Button.Pressed, "#decode")
    def decode_pressed(self):
        self.app.switch_screen("visual_decode")

class VisualEncode(Screen):

    def __init__(self):
        self.question_letter = reactive(f"{randomise_letter()}")
        self.current_morse = reactive("")
        self.start_time = perf_counter()
        self.questions = 10
        self.player_record = self.app.session_data
        super().__init__()

    def reset_session(self):
        self.question_letter = randomise_letter()
        self.current_morse = ""
        self.start_time = perf_counter()
        self.questions = 10

    def compose(self):
        yield Container(
            Label("Encode THIS!"),
            Container(
                Label("Current letter to encode:"),
                Label(f"{self.question_letter}", id="encode_randomiser")
            ),
            Container(
                Label("Current morse:"),
                Label(id="encode_input")
            )
        )

    def on_key(self, event):
        if event.key == self.app.settings.controls.short_beep:
            if len(self.current_morse) >= 5:
                return
            self.current_morse += "."
            self.query_one("#encode_input").update(self.current_morse)

        if event.key == self.app.settings.controls.long_beep:
            if len(self.current_morse) >= 5:
                return
            self.current_morse += "-"
            self.query_one("#encode_input").update(f"{self.current_morse}")

        # TODO implement hardcoded binds to settings
        if event.key == "enter":
            if len(self.current_morse) == 0:
                return
            self.player_record.question_times.append(perf_counter() - self.start_time)
            self.start_time = perf_counter()
            self.player_record.questions_correct.append(encode_question_check(self.question_letter, self.current_morse))
            if len(self.player_record.questions_correct) == self.questions:
                self.app.push_screen("visual_results")
                return
            self.question_letter = randomise_letter()
            self.current_morse = ""
            self.query_one("#encode_randomiser").update(self.question_letter)
            self.query_one("#encode_input").update(self.current_morse)


        if event.key == "backspace":
            if len(self.current_morse) < 0:
                return
            self.current_morse = self.current_morse[:-1]
            self.query_one("#encode_input").update(f"{self.current_morse}")

class VisualDecode(Screen):
    pass
