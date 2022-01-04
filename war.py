"""[summary]
    cards game.
    Returns:
    [type]: win or lose strings.
"""
from random import shuffle


class Card:
    """[Create 48 cards.]

    Returns:
        [type]: [description]
    """

    suits = ["spades", "hearts", "diamonds", "clubs"]

    values = [
        None,
        None,
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
        "Ace",
    ]

    def __init__(self, drawvalue, drawsuit):
        """suit + value are ints"""
        self.value = drawvalue
        self.suit = drawsuit

    def __lt__(self, compare2):
        if self.value < compare2.value:
            return True
        if self.value == compare2.value:
            if self.suit < compare2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, compare2):
        if self.value > compare2.value:
            return True
        if self.value == compare2.value:
            if self.suit > compare2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        stringvalue = self.values[self.value] + " of " + self.suits[self.suit]
        return stringvalue


class Deck:
    """[summary]
    48 cards which has created is shuffled and pop
    """

    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rm_card(self) -> Card:
        """[summary]
        pop() from the pile of cards.

        Returns:
            [Card]:[if pop is success.]
        """
        # if len(self.cards) == 0:
        #    return
        return self.cards.pop()


class Player:
    """[summary]Create the two players"""

    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name


class Game:
    """[summary]
    start game
    """

    def __init__(self):
        name1 = input("p1 name ")
        name2 = input("p2 name ")
        self.deck = Deck()
        self.player1 = Player(name1)
        self.player2 = Player(name2)

    def wins(self, winner):
        """[summary]
        print winner

        Args:
            winner ([type]):string
        """
        winresult = "{} wins this round"
        winresult = winresult.format(winner)
        print(winresult)

    def draw(self, p1n, p1c, p2n, p2c):
        """[summary]print the result of each games.

        Args:
            p1n ([type]): string
            p1c ([type]): Card
            p2n ([type]): string
            p2c ([type]): Card
        """
        drawprocess = "{} drew {} {} drew {}"
        drawprocess = drawprocess.format(p1n, p1c, p2n, p2c)
        print(drawprocess)

    def play_game(self):
        """[First Method]"""

        cards = self.deck.cards
        print("beginning War!")
        while len(cards) >= 2:
            message = "q to quit. Any " + "key to play:"
            response = input(message)
            if response == "q":
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.player1.name
            p2n = self.player2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.player1.wins += 1
                self.wins(self.player1.name)
            else:
                self.player2.wins += 1
                self.wins(self.player2.name)

        win = self.winner(self.player1, self.player2)
        print(f"War is over.{win} wins")

    def winner(self, player1, player2):
        """[Print - Final Result]

        Args:
            player1 ([type]):string
            player2 ([type]):string

        Returns:
            [type]: [description]
        """
        if player1.wins > player2.wins:
            return player1.name
        if player1.wins < player2.wins:
            return player2.name
        return "It was a tie!"


game = Game()
game.play_game()
