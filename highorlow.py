import random

class Card:

    suits = ["♠", "♥", "♦", "♣"]
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    
    def __init__(self, suit, rank):
        if suit not in Card.suits or rank not in Card.ranks:
            raise ValueError(f"Invalid card: {suit} {rank}")

        self.suit = suit
        self.rank = rank
        self.value = self.calculate_value()

    def calculate_value(self):
        if self.rank == "A":
            return 1
        elif self.rank == "J":
            return 11
        elif self.rank == "Q":
            return 12
        elif self.rank == "K":
            return 13
        else:
            return int(self.rank)

    def __str__(self):
        return f"{self.rank}{self.suit}"

    def card_str(self):
        if self.rank == "10":
            return f"""
            ┌─────┐
            │10   │
            │  {self.suit}  │
            │   10│
            └─────┘
            """
        else:
            return f"""
            ┌─────┐
            │{self.rank}    │
            │  {self.suit}  │
            │    {self.rank}│
            └─────┘
            """


class Deck:
    
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Card.suits for rank in Card.ranks]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def debug_print_deck(self):
        for card in self.cards:
            print(card.card_str())
    
    def deal(self, num_cards=1):
        if num_cards > len(self.cards):
            raise ValueError("Not enough cards in the deck.")
        return [self.cards.pop() for _ in range(num_cards)]
    
    def game(self):
        points = 0
        initial_card = self.deal(1)[0]

        while True:
            print(initial_card.card_str())
            print("Current points:", points)
            choice = input("Will the next card be Higher or Lower? ").strip().lower()
            final_card = self.deal(1)[0]
            print(final_card.card_str())

            if choice in ["higher", "h"]:
                if final_card.value > initial_card.value:
                    points += 1
                    print("You got it right! Your score goes up by 1.")
                elif final_card.value == initial_card.value:
                    print("Same card. You gain no points.")
                else:
                    print("Wrong! Your score was:", points)
                    break
            elif choice in ["lower", "l"]:
                if final_card.value < initial_card.value:
                    points += 1
                    print("Correct! Your score is:", points)
                elif final_card.value == initial_card.value:
                    print("Same card. No points.")
                else:
                    print("Wrong! Your score was:", points, "\nThanks for playing!")
                    break
            else:
                print("Invalid input. Please type 'Higher' or 'Lower'.")

            initial_card = final_card
            
            
if __name__ == "__main__":
    deck = Deck()
    deck.game()

