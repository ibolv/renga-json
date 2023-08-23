from dataclasses import dataclass
from .Point3D import Point3D


@dataclass(frozen=True, slots=True)
class Geometry:
    points: list[Point3D]
