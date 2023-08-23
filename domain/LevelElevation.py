from dataclasses import dataclass


@dataclass(frozen=True)
class LevelElevation:
    levelZ: float
    levelName: str
