from items import *
from actions import *
from inventory import *

def main():
    print("Start game.")
    help_menu()

    valid_commands = ["h", "q", "m", "s", "i"]

    inventory = Inventory()

    while True:
        user_input = input(">")

        if user_input not in valid_commands:
            print("Invalid command.")
            continue

        if user_input == "h":
            help_menu()

        if user_input == "q":
            print("Quit game.")
            return
        
        if user_input == "m":
            ore = mine(Vein())
            inventory.add_item(ore)

        if user_input == "s":
            item = inventory.take_item()
            if item == None:
                print("No ores to smelt.")
                continue
            bar = smelt(item)
            inventory.add_item(bar)
        
        if user_input == "i":
            inventory.show_inventory()

if __name__ == "__main__":
    main()
