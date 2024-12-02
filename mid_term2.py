import random

card_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, "j", "Q", "K", "A"]
player_hand =[] # to store the cards after random
computer_hand = [] # to store the cards after random

player_running = True # while user playing the blckJack
computer_running = True # while the computer is looping


def random_card (turn) :
    card = random.choice(card_list)
    turn.append(card)
    card_list.remove(card)

def total (turn):
    total = 0
    special_card = ["J", "Q", "K"]
    for card in turn :
        if card in range (1, 11):
            total +=card
        elif card in special_card :
            total += 10
        else:
            if total > 11:
                total += 10
            else :
                total += 11
    return total

def computer_card ():
    if len(computer_hand) == 2 :
        return computer_hand[0]
    elif len(computer_hand) > 2:
        return computer_hand


def player_card ():
    if len(player_hand) == 2:
        return player_hand[0],player_hand[1]
    elif len(player_hand) >2:
        return player_hand






play_again = "y"


while play_again == "y":
# to loop new list to play again
    player_running = True  # while user playing the blckJack
    computer_running = True  # while the computer is looping
    card_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, "j", "Q", "K", "A"]
    player_hand=[]
    computer_hand= []
# =============================
    for i in range(2):
        random_card(player_hand)
        random_card(computer_hand)
    while player_running or computer_running :
        print (f"Your cards : \n{player_card()}\nYour scores are : {total(player_hand)}")
        print (f"Dealer's  first cared : \n{computer_card()}")
        if player_running :
            player_input = input("Type 'y' to get another card, 'n' to stop: ").lower()
            print ("===========================================")
        if total(computer_hand) > 16 :
            computer_running = False
        else :
            random_card(computer_hand)
        if player_input == "n" :
            player_running = False

        else:
            random_card(player_hand)
        if total(player_hand) >= 21:
            break
        elif computer_running >= 21 :
            break

    if total(player_hand) == 21 :
        print (f"Your cards:\n{player_card()}\nYour scores are : {total(player_hand)}")
        print (f"Dealer's  first cared : \n{computer_card()}")
        print ("BlackJack! You win!")

    elif total(computer_hand) == 21 :
        print(f"Your cards:\n{player_card()}\nYour scores are : {total(player_hand)}")
        print(f"Dealer's  first cared : \n{computer_card()}\nDealer's final scores: {total(computer_hand)}")
        print("BlackJack! Dealer wins!")

    elif total(player_hand) > 21 :
        print(f"Your cards:\n{player_card()}\nYour scores are : {total(player_hand)}")
        print(f"Dealer's  first cared : \n{computer_card()}\nDealer's final scores: {total(computer_hand)}")
        print("You bust!  You lose!")

    elif total(computer_hand) > 21 :
        print(f"Your cards:\n{player_card()}\nYour scores are : {total(player_hand)}")
        print(f"Dealer's  first cared : \n{computer_card()}\nDealer's final scores: {total(computer_hand)}")
        print("Dealer Busts!  You win!")

    elif total(player_hand) == 21 and total(computer_hand) == 21:
        print(f"Your cards:\n{player_card()}\nYour scores are : {total(player_hand)}")
        print(f"\nDealer's  first cared : \n{computer_card()}\nDealer's final scores: {total(computer_hand)}")
        print("BlackJack! Dealer wins!")

    elif total(player_hand) > total(computer_hand) :
        print(f"Your cards:\n{player_card()}\nYour scores are : {total(player_hand)}")
        print(f"Dealer's  first cared : \n{computer_card()}")
        print("Your scores are more than dealer's scores! You win!")

    elif total(player_hand) < total(computer_hand):
        print(f"Your cards:\n{player_card()}\nYour scores are : {total(player_hand)}")
        print(f"Dealer's  first cared : \n{computer_card()}\nDealer's final scores: {total(computer_hand)}")
        print("Dealer's scores are more than your scores! You lose!")

    while True :
        play_again = input("Do you want to play the game again? [y/n] : ").lower()
        print("===========================================")
        if play_again == "n" or play_again == "y":
            break
