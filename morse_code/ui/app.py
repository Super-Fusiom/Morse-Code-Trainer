from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Label, Button


class Trainer(App):
    CSS_PATH = "style.css"
    def compose(self) -> ComposeResult:
        yield Label("Morse code test!", id="morse_code")
        yield Button("EXIT!", id="exit")

    @on(Button.Pressed, "#exit")
    def submit_pressed(self) -> None:
        self.exit()
