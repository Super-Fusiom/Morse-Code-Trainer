from textual.app import App
from morse_code.ui.main_menu import MainMenu
from morse_code.ui.sound_train import SoundUI

class Trainer(App):
    CSS_PATH = "morse_code/ui/style.css"

    def on_mount(self):
        self.install_screen(MainMenu(), "menu")
        self.install_screen(SoundUI(), "sound")
        self.push_screen("menu")


def main():
    app = Trainer()
    app.run()


if __name__ == "__main__":
    main()
