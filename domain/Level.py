from dataclasses import dataclass
from .Room import Room
from .Door import Door
from .Stairway import Stairway


@dataclass(frozen=True)
class Level:
    name: str
    sizeZ: float
    buildingElements: list[Room | Stairway | Door]
