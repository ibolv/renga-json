from dataclasses import dataclass


@dataclass
class Point2D:
    def __init__(self, x: float, y: float):
        super().__init__()
        self.x = x
        self.y = y
