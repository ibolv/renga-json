from dataclasses import dataclass
from uuid import UUID
from .Geometry import Geometry


@dataclass
class Door:
    sign: str
    output: list[UUID]
    id: UUID
    name: str
    width: float
    sizeZ: float
    zLevel: float
    xy: list[Geometry]

    # def __init__(
    #     self,
    #     sign: str,
    #     output: list[UUID],
    #     id: UUID,
    #     name: str,
    #     width: float,
    #     sizeZ: float,
    #     zLevel: float,
    #     xy: list[Geometry],
    # ):
    #     self.sign = sign
    #     self.output = output
    #     self.id = id
    #     self.name = name
    #     self.width = width
    #     self.sizeZ = sizeZ
    #     self.zLevel = zLevel
    #     self.xy = xy
