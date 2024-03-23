class Tile:
    def __init__(self, walk, lock = False, req = None) -> None:
        self.neighbors = []
        self.walkable = walk
        self.locked = lock
        self.requiredItem = req
