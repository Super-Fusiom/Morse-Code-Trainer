from textual import on
from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Label, Button, Header, Footer

class Trainer(App):
    CSS_PATH = "style.css"

    def on_mount(self):
        self.theme = "atom-one-dark"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Container(
            Label("Morse code test!", id="morse_code"),
            Button("EXIT!", id="exit"), id="main"
        )

    @on(Button.Pressed, "#exit")
    def submit_pressed(self) -> None:
        self.exit()
