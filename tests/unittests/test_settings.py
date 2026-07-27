from morse_code.functions.settings import (
    Controls,
    Settings,
    load_settings,
    save_settings,
)


def test_default_settings(tmp_path):
    file = tmp_path / "settings.json"

    settings = load_settings(file)

    assert file.exists()

    assert settings.controls.short_beep == "x"
    assert settings.controls.long_beep == "z"

def test_save_and_load(tmp_path):
    file = tmp_path / "settings.json"

    original = Settings(
        controls=Controls(
            short_beep="j",
            long_beep="k"
        )
    )

    save_settings(original, file)

    loaded = load_settings(file)

    assert loaded.controls.short_beep == "j"
    assert loaded.controls.long_beep == "k"
