import random
from art import logo
from replit import clear # Program was made in Replit workspace


def deal_card():
    """"Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


# Takes a list of cards as input and returns the score
def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    # Checking for blackjack(hand w/ only 2 cards: ace(11) + 10); return 0  to represent blackjack
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # Check for ace. If score is already over 21, replace 11 w/ 1.
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw."
    elif computer_score == 0:
        return "You lose..."
    elif user_score == 0:
        return "Blackjack! You win!!!"
    elif user_score > 21:
        return "You're over 21. You lose..."
    elif computer_score > 21:
        return "Computer went over 21. You win!!!"
    elif user_score > computer_score:
        return "You win!!!"
    else:
        return "You lose..."


def play_game():
    print(logo)
    # Deal the user and computer 2 cards each
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score is {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            draw_card = input("Would you like to draw another card? Press 'y' for yes, or 'n' for no\n").lower()
            if draw_card == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, current score is {user_score}")
    print(f"Computer's last hand: {computer_cards}, current score is {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play Blackjack? Type 'y' for yes, or 'n' for no\n") == 'y':
    clear()
    play_game()






