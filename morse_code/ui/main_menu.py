"""Main Menu UI"""

from textual import on
from textual.screen import Screen
from textual.containers import Container
from textual.widgets import Label, Button

class MainMenu(Screen):
    def compose(self):
        yield Container(
            Label("Main Menu - Morse Code Training"),
            Button("Visual Training", id="visual"),
            Button("Audio Training", id="audio"),
            Button("Stats", id="stats"),
            Button("Exit!", id="exit"),
            id="main"
        )

    @on(Button.Pressed, "#audio")
    def sound_pressed(self) -> None:
        self.app.switch_screen("sound")

    @on(Button.Pressed, "#exit")
    def exit_pressed(self) -> None:
        self.app.exit()
