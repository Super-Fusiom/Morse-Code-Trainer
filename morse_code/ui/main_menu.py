"""Main Menu UI"""

from textual import on
from textual.containers import Container
from textual.screen import Screen
from textual.widgets import Button, Label

from morse_code.functions.settings import save_settings


class MainMenu(Screen):
    def compose(self):
        yield Container(
            Label("Main Menu - Morse Code Training"),
            Button("Visual Training", id="visual"),
            Button("Audio Training", id="audio"),
            Button("Stats", id="stats"),
            Button("Settings", id="settings"),
            Button("Exit!", id="exit"),
            id="main"
        )

    @on(Button.Pressed, "#visual")
    def visual_pressed(self) -> None:
        self.app.switch_screen("visual")

    @on(Button.Pressed, "#audio")
    def sound_pressed(self) -> None:
        self.app.switch_screen("sound")

    @on(Button.Pressed, "#exit")
    def exit_pressed(self) -> None:
        save_settings(self.app.settings, self.app.settings_path)
        self.app.exit()
