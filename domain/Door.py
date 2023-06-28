from dataclasses import dataclass
from uuid import UUID
from .Geometry import Geometry


@dataclass
class Door:
    id: UUID
    name: str
    width: float
    sizeZ: float
    zLevel: float
    outputs: list[UUID]
    xy: list[Geometry]
    sign: str = "DoorWay"
