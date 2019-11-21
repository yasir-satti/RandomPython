import os
import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4

def deal(deck): #function for dealing 2 cards to player and dealer at start
    hand = []
    for i in range(2): #2 times loop
        random.shuffle(deck)
        card = deck.pop() #pulls one value out of deck array
        if card == 11:
            card = "J"
        if card == 12:
            card = "Q"
        if card == 13:
            card = "K"
        if card == 14:
            card = "A"
        hand.append(card) #places card into hand array
    return hand


def reset_deck():
    global deck
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4

def play_again(): #resets game
    while True:
        again = input("Do you want to play again? (Y/N) : ").lower()
        if again == "y":
            dealer_hand = []
            player_hand = []
            game()
            break
        elif again == "n":
            print ("Bye!")
            exit()
        else:
            print("Invalid Input")
            continue

def total(hand): #quick maths
    total = 0
    ace_count = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            total += 10
        elif card == "A":
            ace_count += 1
        else:
            total += card
    if ace_count != 0:  #Ace needs extended maths logic
        if ace_count == 1:
            if total >= 11:
                total+= 1
            else:
                total += 11
        elif ace_count == 2:
            for i in range(2):
                if total >= 11:
                    total+= 1
                else:
                    total += 11
        elif ace_count == 3:
            for i in range(3):
                if total >= 11:
                    total+= 1
                else:
                    total += 11
        elif ace_count == 4:
            for i in range(4):
                if total >= 11:
                    total+= 1
                else:
                    total += 11
        while True:         #Protects against multiple aces being calculated incorrectly
            if total > 21:
                total -=11
                total +=1
            if total <=21:
                break
    return total

def hit(hand): 
    card = deck.pop()
    if card == 11:card = "J"
    if card == 12:card = "Q"
    if card == 13:card = "K"
    if card == 14:card = "A"
    hand.append(card)
    return hand

def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')

def print_results(dealer_hand, player_hand):
    clear()
    print ("The dealer has a " + str(dealer_hand) + " for a total of " + str(total(dealer_hand)))
    print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))

def blackjack(dealer_hand, player_hand): #checks for blackjack
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Congratulations! You got a Blackjack!\n")
        play_again()
        
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)     
        print("Sorry, you lose. The dealer got a blackjack.\n")
        play_again()

def score(dealer_hand, player_hand): #checks hand values vs each other
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Congratulations! You got a Blackjack!\n")
        
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)     
        print("Sorry, you lose. The dealer got a blackjack.\n")
        
    elif total(player_hand) > 21:
        print_results(dealer_hand, player_hand)
        print("Sorry. You busted. You lose.\n")
        
    elif total(dealer_hand) > 21:
        print_results(dealer_hand, player_hand)            
        print("Dealer busts. You win!\n")
        
    elif total(player_hand) < total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print("Sorry. Your score isn't higher than the dealer. You lose.\n")
        
    elif total(player_hand) > total(dealer_hand):
        print_results(dealer_hand, player_hand)            
        print("Congratulations. Your score is higher than the dealer. You win\n")
        
    elif total(player_hand) == total(dealer_hand):
        print_results(dealer_hand, player_hand)            
        print("Your score is equal to the dealer. You drew\n")
        
    else:
        print("wtf did you do?")

def game():
    global deck
    choice = 0
    clear()
    print ("WELCOME TO BLACKJACK!\n")
    reset_deck()
    dealer_hand = deal(deck) #generates starting hands
    player_hand = deal(deck)
    while choice != "q":
        print("The dealer is showing a " + str(dealer_hand[0])) #shows first card in dealers hand
        print("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))
        blackjack(dealer_hand, player_hand) #checks for blackjack
        choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
        clear()
        if choice == "h":
            hit(player_hand)
            if total(player_hand) > 21:
                print_results(dealer_hand, player_hand)
                print("Sorry. You busted. You lose.\n")
                play_again()
        elif choice == "s":
            while total(dealer_hand) < 17: #dealer must hit to 16
                hit(dealer_hand)
            score(dealer_hand, player_hand)
            play_again()
        elif choice == "q":
                print ("Bye!")
                exit()
    
if __name__ == "__main__":
    game()
