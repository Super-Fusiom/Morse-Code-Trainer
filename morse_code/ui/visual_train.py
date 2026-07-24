# from textual import on
from textual.containers import Container
from textual.screen import Screen
from textual.widgets import Button, Label


class VisualBrief(Screen):

    def compose(self):
        yield Container(
            Label("""
                The Visual Trainer has two parts, Letters to Morse\n
                and Morse to Letters.

                """),
            Button(),
            Button()
        )
