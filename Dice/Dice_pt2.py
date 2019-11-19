from Dice import throw

while True:
        again = input("Do you want to throw dice? (Y/N) : ").lower()
        if again == "y":
            dice = throw()
            print(dice)
        elif again == "n":
            print ("Bye!")
            exit()
        else:
            print("Invalid Input")
            continue
