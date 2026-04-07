"""Program for working with a deck of 54 cards.
   Create, shuffle, and draw cards by number with input verification."""


import random
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Card:
    suit: str
    value: str
    number_list = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    masts_list = ["Hearts", "Clubs", "Spades", "Diamonds"]

    def __str__(self) -> str:
        return f"{self.suit} {str(self.value)}"


class CardDeck:
    def __init__(self) -> None:
        self.deck = [Card(s, v) for s in Card.masts_list for v in Card.number_list]
        self.deck.extend([Card("Joker", "Red"), Card("Joker", "Black")])

    def shuffle(self) -> None:
        random.shuffle(self.deck)

    def get(self, index: int) -> Optional[Card]:
        if 1 <= index <= 54:
            return self.deck[index - 1]
        return None


deck = CardDeck()
deck.shuffle()


while True:
    user_input = input("Choose a card (1-54): ")
    if user_input.isdigit():
        card_number = int(user_input)
        card = deck.get(card_number)

        if card:
            print(f'Your card is: {card}')
            break
        print("Error! Only 1 to 54. Please try again.")
    else:
        print("Error! Please enter a whole number. Please try again.")
