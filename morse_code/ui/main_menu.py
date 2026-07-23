from textual import on
from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.containers import Container
from textual.widgets import Label, Button

class Trainer(App):
    CSS_PATH = "style.css"

    def on_mount(self):
        self.install_screen(MainMenu(), "menu")
        self.push_screen("menu")

    def exit_app(self):
        self.exit()

class MainMenu(Screen):
    def compose(self):
        yield Container(
            Label("Main Menu - Morse Code Training"),
            Button("Exit!", id="exit"),
            id="main"
        )

    @on(Button.Pressed, "#exit")
    def submit_pressed(self) -> None:
        self.app.exit_app()
