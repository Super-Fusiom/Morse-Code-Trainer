"""Main Menu UI"""

from textual import on
from textual.app import App
from textual.screen import Screen
from textual.containers import Container
from textual.widgets import Label, Button

from morse_code.ui.sound_train import SoundUI

class Trainer(App):
    CSS_PATH = "style.css"

    def on_mount(self):
        self.install_screen(MainMenu(), "menu")
        self.install_screen(SoundUI(), "sound")
        self.push_screen("menu")

    def exit_app(self):
        self.exit()

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
        self.app.exit_app()
