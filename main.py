"""a small program to deal cards for a game of Texas Hold'em."""


import random


def deck_shuffler(card):
    random.shuffle(card)
    return iter(card)


def number_of_players():
    while True:
        print()
        number = input("How many players are there?  ").strip()

        try:
            number = int(number)
        except ValueError:
            print(f"{number} is not a digit")
        else:
            if number not in range(2, 11):
                print(f"The number of player should be between 2 and 10")
            else:
                return number


def deck_handler(card, players):
    deal_to_player(deck_shuffler(card), players)
    deal_to_table(deck_shuffler(card))


def deal_to_player(card, players):
    print()

    first_hand = [next(card) for _ in range(players)]
    second_hand = [next(card) for _ in range(players)]

    deal = zip(first_hand, second_hand)

    for index, deal in enumerate(deal, start=1):
        print(f"Player {index} was dealt: {', '.join(map(str, deal))}")

    print()


def deal_to_table(card):
    next(card)
    flop = ', '.join(map(str, [next(card) for _ in range(3)]))
    next(card)
    turn = next(card)
    next(card)
    river = next(card)

    print(f"The flop: {flop}\nThe turn: {turn}\nThe river: {river}\n")


suits = ['clubs', 'diamonds', 'hearts', 'spades']
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'ace', 'king', 'queen', 'jack']
deck = [(rank, suit) for rank in ranks for suit in suits]

menu = """Make a new party ?
P: Play
Q: Quit
"""

selection = input(menu).strip().title()[0]

while selection == 'P':
    deck_handler(deck, number_of_players())

    selection = input(menu).strip().title()[0]
