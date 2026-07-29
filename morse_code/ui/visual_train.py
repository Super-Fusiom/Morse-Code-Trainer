"""Visual Mode for trainer"""
from textual import on
from textual.containers import Container
from textual.reactive import reactive
from textual.screen import Screen
from textual.widgets import Button, Label, Log


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
        self.app.switch_screen("visual_encode")

    @on(Button.Pressed, "#decode")
    def decode_pressed(self):
        self.app.switch_screen("visual_decode")

class VisualEncode(Screen):

    current_morse = reactive("")

    def compose(self):
        yield Container(
            Label("Encode THIS!"),
            Container(
                Label("Current letter to encode:"),
                Label("", id="encode_randomiser")
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



class VisualDecode(Screen):
    pass
