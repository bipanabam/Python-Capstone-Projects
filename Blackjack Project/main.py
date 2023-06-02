################## Blackjack Project ##################

#Difficulty Normal 😎: Use al  Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Dificulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project


############## Our Blackjack House Rules ############
##The deck is unlimited in size.
##There are no jokers
##The Jack/Queen/King all count as 10
##The Ace can count as 11 or 1
#   total<17(16 or under: must take another card)
#   total>21(lose without overdue)
# Bust(lose)

#Use the following list as the dek of cards:
#The cards in the list have equal probability of being drawn
#Cards are not removed from the deck as they are drawn
import random 
# from art import logo

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

    return random.choice(cards)

def calculate_score(cards):
    """Take a list of cards and return the score calculated
    from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
            
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blakjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😊"
    elif user_score > computer_score:
        print("You win 😊")
    else:
        print("You lose 😤")

def play_game():
    # print(logo)
    user_cards = []
    computer_cards = []
    for _ in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())

    is_game_over = False

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" Your cards: {user_cards}, current score: {user_score}" )
        print(f" Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, and type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17 :
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f" Your final hand: {user_cards}, final score: {user_score}" )
    print(f" Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    print("\x1B[2J")
    play_game()

