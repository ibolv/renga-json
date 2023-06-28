from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Point2D:
    x: float
    y: float

    # def __init__(self, x: float, y: float):
    #     self.x = x
    #     self.y = y
