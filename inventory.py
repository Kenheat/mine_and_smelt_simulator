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
    
    def take_item(self):
        for i in range(len(self.items)):
            if str(self.items[i]) == "Gold ore":
                self.quantities["Gold ore"] -= 1
                return self.items.pop(i)
    
    def show_inventory(self):
        if len(self.items) == 0:
            print("No items in inventory.")
            return
        for item in self.quantities:
            if self.quantities[item] != 0:
                print(f"{item} x {self.quantities[item]}")
