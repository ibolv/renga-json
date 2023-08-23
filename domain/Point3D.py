from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Point3D:
    x: float
    y: float
    z: float

    def __str__(self) -> str:
        return f"(X: {self.x}, Y: {self.y}, Z: {self.z})"

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Point3D):
            return self.x == __value.x and self.y == __value.y and self.z == __value.z
        return False

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z))
