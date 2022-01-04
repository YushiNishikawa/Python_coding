"""
    This is hangman.
"""


def hangman(word):
    """
    This is hangman.
    """
    wrong = 0
    stages = [
        "",
        "__________      ",
        "|               ",
        "|        |      ",
        "|        0      ",
        r"|       /|\     ",
        r"|       / \     ",
        "|               ",
    ]

    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1

        print((" ".join(board)))
        endl = wrong + 1
        print("\n".join(stages[0:endl]))

        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[0 : wrong + 1]))
        print("You lose! It was f{word}.")


hangman("cat")
