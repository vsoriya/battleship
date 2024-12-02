
import random

# កំណត់តម្លៃកាត
card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

# អនុគមន៍ដើម្បីដាក់កាត
def draw_card():
    return random.choice(card_values)

# អនុគមន៍គណនាពិន្ទុ
def calculate_score(hand):
    score = sum(hand)
    if score > 21 and 11 in hand:  # ពិនិត្យមើលថាតើមាន Ace ឬអត់
        hand[hand.index(11)] = 1   # ប្រែ Ace ពី 11 ទៅ 1
        score = sum(hand)
    return score

# អនុគមន៍សម្រាប់ពិនិត្យ blackjack
def check_blackjack(hand):
    return sum(hand) == 21 and len(hand) == 2

# អនុគមន៍បង្ហាញលទ្ធផលចុងក្រោយ
def display_final_results(user_hand, computer_hand, user_score, computer_score):
    print(f"\nYour final hand: {user_hand}, final score: {user_score}")
    print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
    if user_score > 21:
        print("You went over 21. You lose!")
    elif computer_score > 21 or user_score > computer_score:
        print("You win!")
    elif user_score == computer_score:
        print("It's a draw!")
    else:
        print("You lose!")

# អនុគមន៍ដើម្បីលេងល្បែង
def blackjack_game():
    while True:
        user_hand = [draw_card(), draw_card()]  # ដាក់កាតសម្រាប់អ្នកលេង
        computer_hand = [draw_card(), draw_card()]  # ដាក់កាតសម្រាប់កុំព្យូទ័រ
        user_score = calculate_score(user_hand)
        computer_score = calculate_score(computer_hand)

        # បង្ហាញដៃដំបូង
        print(f"\nYour hand: {user_hand}, current score: {user_score}")
        print(f"Computer's first card: {computer_hand[0]}")

        # ពិនិត្យ blackjack
        if check_blackjack(user_hand):
            if check_blackjack(computer_hand):
                print("Both you and the computer have blackjack! It's a draw.")
            else:
                print("Blackjack! You win!")
            break
        elif check_blackjack(computer_hand):
            print("Computer has blackjack! You lose!")
            break

        # អ្នកលេងគិតចិត្តថាចង់ដកកាតបន្តទៀត
        while user_score < 21:
            another_card = input("Type 'y' to get another card, 'n' to pass: ").lower()
            if another_card == 'y':
                user_hand.append(draw_card())
                user_score = calculate_score(user_hand)
                print(f"Your hand: {user_hand}, current score: {user_score}")
            else:
                break

            if user_score > 21:
                print("You went over 21! You lose.")
                return

        # កុំព្យូទ័រធ្វើការលេង
        while computer_score < 17:
            computer_hand.append(draw_card())
            computer_score = calculate_score(computer_hand)

        # បង្ហាញលទ្ធផលចុងក្រោយ
        display_final_results(user_hand, computer_hand, user_score, computer_score)

        # សំណួរសម្រាប់លេងម្ដងទៀត
        play_again = input("\nDo you want to play again? Type 'y' or 'n': ").lower()
        if play_again != 'y':
            break

# ចាប់ផ្តើមល្បែង
blackjack_game()






