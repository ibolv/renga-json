from dataclasses import dataclass
from .Room import Room
from .Door import Door
from .Stairway import Stairway


@dataclass(frozen=True)
class Level:
    name: str
    sizeZ: float
    buildingElements: list[Room | Stairway | Door]

    # def __init__(self, name: str, sizeZ: float, buildingElements: list[Room | Stairway | Door]):
    #     self.name = name
    #     self.sizeZ = sizeZ
    #     self.buildingElements = buildingElements
