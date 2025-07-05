class Vein:
    def __init__(self):
        pass

class Ore(Vein):
    def __init__(self):
        super().__init__()

class Bar(Ore):
    def __init__(self):
        super().__init__()

class Inventory():
    def __init__(self):
        self.items = {}
