import time
import sys
import random

count = 0
print("You must choose. But choose wisely. For as the True Grail will bring you life -- the False Grail will take it from you.")
while True:
    selection = random.randint(5,10)
    userinpt = selection + 1
    while userinpt == 0 or userinpt >= selection:
        if count == 3:
            print("He's not the Messiah. He's a very naughty boy")
            time.sleep(3)
            sys.exit()
        count += 1
        randomnum = random.randint(1,selection)
        print("There are ", selection, "goblets, pick a goblet: ")
        try:
            userinpt = int(input())
        except ValueError:
            print("Invalid input")
            continue
        if userinpt == randomnum:
            print("You have chosen")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print("Wisely")
            time.sleep(2)
        elif userinpt <= 0:
            print("Why?")
            continue
        elif userinpt >= selection:
            print("Not an option boyo")
            continue
        else:
            print("You have chosen")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print("Poorly")
            time.sleep(2)
            print("correct answer: ", randomnum)

        answer = input('Play again? (y/n): ')
        if answer in ("y", "n", "Y", "N"):
            if answer == "y" or answer == "Y":
                continue
            else:
                print ("Goodbye")
                sys.exit()
        else:
            print("I'll take that as a no then")
            time.sleep(5)
            sys.exit()

