from dataclasses import dataclass
from .Geometry import Geometry
from uuid import UUID


@dataclass
class Room:
    sign: str
    output: list[str]
    id: UUID
    name: str
    area: float
    sizeZ: float
    zLevel: float
    xy: list[Geometry]

    def __init__(
        self,
        sign: str,
        outputs: list[str],
        id: UUID,
        name: str,
        area: float,
        size_z: float,
        z_level: float,
        xy: list[Geometry],
    ):
        super().__init__()
        self.sign = sign
        self.output = outputs
        self.id = id
        self.name = name
        self.area = area
        self.sizeZ = size_z
        self.zLevel = z_level
        self.xy = xy
