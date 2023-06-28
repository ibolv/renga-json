from dataclasses import dataclass
from .Point3D import Point3D


@dataclass(frozen=True, slots=True)
class Geometry:
    points: list[Point3D]

    # def __init__(self, points: list[Point3D]):
    #     self.points = points
