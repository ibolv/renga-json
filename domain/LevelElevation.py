from dataclasses import dataclass


@dataclass(frozen=True)
class LevelElevation:
    levelZ: float
    levelName: str

    # def __init__(self, level_z: float, level_name: str):
    #     self.levelZ = level_z
    #     self.levelName = level_name
