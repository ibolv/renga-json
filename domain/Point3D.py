from dataclasses import dataclass


@dataclass
class Point3D:
    def __init__(self, x: float, y: float, z: float):
        super().__init__()
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return f"(X: {self.x}, Y: {self.y}, Z: {self.z})"

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Point3D):
            return self.x == __value.x and self.y == __value.y and self.z == __value.z
        return False
