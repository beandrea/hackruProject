import tile
class Map:
    def __init__(self, lock =  False, req = None) -> None:
        self.tiles = []
        self.neighbors = []
        self.locked = lock
        self.required = req