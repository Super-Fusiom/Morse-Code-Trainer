from pathlib import Path

from textual.app import App

from morse_code.functions.settings import load_settings
from morse_code.ui.main_menu import MainMenu
from morse_code.ui.sound_train import SoundWelcome
from morse_code.ui.visual_train import VisualDecode, VisualEncode, VisualWelcome

SETTINGS_FILE = Path("settings.json")

class Trainer(App):
    CSS_PATH = "morse_code/ui/style.css"
    def __init__(self):
        super().__init__()
        self.settings = load_settings(SETTINGS_FILE)
        self.settings_path = SETTINGS_FILE

    def on_mount(self):
        self.install_screen(MainMenu(), "menu")
        self.install_screen(SoundWelcome(), "sound")
        self.install_screen(VisualWelcome(), "visual")
        self.install_screen(VisualDecode(), "visual_decode")
        self.install_screen(VisualEncode(), "visual_encode")
        self.push_screen("menu")


def main():
    app = Trainer()
    app.run()


if __name__ == "__main__":
    main()
