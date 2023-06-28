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

    # def __init__(
    #     self,
    #     sign: str,
    #     output: list[UUID],
    #     id: UUID,
    #     name: str,
    #     area: float,
    #     sizeZ: float,
    #     zLevel: float,
    #     xy: list[Geometry],
    # ):
    #     self.sign = sign
    #     self.output = output
    #     self.id = id
    #     self.name = name
    #     self.area = area
    #     self.sizeZ = sizeZ
    #     self.zLevel = zLevel
    #     self.xy = xy
