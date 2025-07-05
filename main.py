from items import *
from actions import *

def main():
    while True:
        user_input = input(">")

        if user_input == "q":
            print("Goodbye!")
            return
        
        if user_input == "m":
            mine()

        if user_input == "s":
            smelt()

if __name__ == "__main__":
    main()
