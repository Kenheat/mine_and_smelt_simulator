class Inventory():
    def __init__(self):
        self.items = []
        self.quantities = {}

    def add_item(self, item):
        self.items.append(item)

        if str(item) in self.quantities:
            self.quantities[str(item)] += 1
        else:
            self.quantities[str(item)] = 1
    
    def show_inventory(self):
        for item in self.quantities:
            print(f"{item} x {self.quantities[item]}")
