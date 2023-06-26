from dataclasses import dataclass


@dataclass
class Point3D:
    def __init__(self, x: float, y: float, z: float):
        super().__init__()
        self.x = x
        self.y = y
        self.z = z
