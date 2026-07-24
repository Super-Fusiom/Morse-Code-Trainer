from textual import on
from textual.containers import Container
from textual.screen import Screen
from textual.widgets import Button, Label


class SoundUI(Screen):
    def compose(self):
        yield Container(
            Label("""
            The sound trainer will play random characters of short and long beeps.\n
            Ensure your volume is set correctly before starting.
            """),
            Label("Are you ready?"),
            Button("Yes"),
            Button("No", id="main_menu_exit")
        )

    @on(Button.Pressed, "#main_menu_exit")
    def submit_pressed(self):
        self.app.switch_screen("menu")
