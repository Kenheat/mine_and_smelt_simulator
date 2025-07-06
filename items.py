class Vein:
    def __init__(self):
        self.type = "Gold"

    def extract(self):
        return Ore()

class Ore(Vein):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f"{self.type} ore"

class Bar(Ore):
    def __init__(self):
        super().__init__()
