class Vein:
    def __init__(self):
        self.type = "Gold"

    def __str__(self):
        return f"{self.type} vein"
    
    def extract_ore(self):
        return Ore()

class Ore(Vein):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f"{self.type} ore"
    
    def create_bar(self):
        return Bar()

class Bar(Ore):
    def __init__(self):
        super().__init__()
    
    def __str__(self):
        return f"{self.type} bar"
