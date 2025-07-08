import time
from items import *

def mine(vein):
    vein_to_mine = vein
    extract = vein_to_mine.extract_ore()
    animation()
    print(f"{extract.type} ore extracted.")
    return extract

def smelt(ore):
    ore_to_smelt = ore
    bar = ore_to_smelt.create_bar()
    animation()
    print(f"{bar.type} bar created.")
    return bar

def animation():
    anim_sentence = "|---|"
    
    for i in range(len(anim_sentence)):
        if anim_sentence[i] == "-":
            time.sleep(0.5)
            anim_sentence = anim_sentence.replace("-", ">", 1)
            print(anim_sentence)
        
def help_menu():
    print("")
    print("h: help menu")
    print("q: quit")
    print("m: mine")
    print("s: smelt")
    print("i: inventory")
    print("")