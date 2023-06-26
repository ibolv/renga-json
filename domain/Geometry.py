from dataclasses import dataclass
from .Point3D import Point3D


@dataclass
class Geometry:
    points: list[Point3D]

    def __init__(self, points: list[Point3D]):
        super().__init__()
        self.points = points
