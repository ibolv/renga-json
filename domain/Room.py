from dataclasses import dataclass
from .Geometry import Geometry
from uuid import UUID


@dataclass(frozen=True, slots=True)
class Room:
    id: UUID
    name: str
    area: float
    sizeZ: float
    zLevel: float
    outputs: list[UUID]
    xy: list[Geometry]
    sign: str = "Room"
