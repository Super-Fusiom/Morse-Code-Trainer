from dataclasses import asdict, dataclass, field
from json import dump, load
from pathlib import Path


@dataclass
class Controls:
    short_beep: str = "x"
    long_beep: str = "z"


@dataclass
class Settings:
    controls: Controls = field(default_factory=Controls)


def load_settings(path: Path) -> Settings:
    if not path.exists():
        settings = Settings()
        save_settings(settings, path)
        return settings
    with open(path) as file:
        data = load(file)

    return Settings(
        controls=Controls(
            short_beep=data.get("controls").get("short_beep"),
            long_beep=data.get("controls").get("long_beep")
        )
    )

def save_settings(settings: Settings, path: Path) -> None:
 with open(path, "w") as file:
     dump(
         asdict(settings),
         file,
         indent=4
     )
