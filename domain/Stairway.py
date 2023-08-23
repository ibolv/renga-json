from dataclasses import dataclass
from uuid import UUID
from .Geometry import Geometry


@dataclass(frozen=True, slots=True)
class Stairway:
    id: UUID
    name: str
    area: float
    sizeZ: float
    zLevel: float
    outputs: list[UUID]
    xy: list[Geometry]
    sign: str = "Staircase"
