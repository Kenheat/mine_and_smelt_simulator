import time
from items import *

def mine(vein):
    vein_to_mine = vein
    extract = vein_to_mine.extract()
    print("Ore extracted.")
    return extract

def smelt():
    pass

def animation():
    symbol = "*"

    for i in range(5):
        time.sleep(1)
        print(symbol)
        symbol += "*"

def help_menu():
    print("")
    print("q: quit")
    print("m: mine")
    print("s: smelt")
    print("i: inventory")
    print("")