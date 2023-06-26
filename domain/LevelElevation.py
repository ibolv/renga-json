class LevelElevation:
    levelZ: float
    levelName: str

    def __init__(self, level_z: float, level_name: str):
        super().__init__()
        self.levelZ = level_z
        self.levelName = level_name
