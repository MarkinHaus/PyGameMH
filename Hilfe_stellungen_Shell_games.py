"""
#Number guesser
from random import randint
if __name__ == '__main__':

    pc_nummer = randint(0, 100)
    player_nummer = -1

    while pc_nummer != player_nummer:
        player_nummer = int(input("Nummer: ").strip())

        if player_nummer > pc_nummer:
            print("die pc nummer ist kleiner")

    print("Gewonnen pc nummer war:", pc_nummer)
"""

"""
# Text entwenture help
import os


class Player:

    def __init__(self, name):
        self.name = name
        self.options = ""
        self.gold = 10
        # leben
        # schaden

    def print_(self):

        # os.system("clear") löscht text in der Shell

        print(f"{self.options} \nGold: {self.gold}")


def level1_haus(player: Player):
    level1(player)


def level1_shop(player: Player):
    player.options = "1. 10 leben für 1 Gold\n2. 1 schwert für 5 Gold macht 5 schaden\n3. Zurück"

    player.options = f"1. 10 leben für 1 Gold {'genügend Gold' if player.gold >= 1 else 'nicht genügend Gold'}\n" \
                     f"2. 1 schwert für 5 Gold macht 5 schaden {'genügend Gold' if player.gold >= 5 else 'nicht genügend Gold'}\n" \
                     f"3. Zurück"

    player.print_()

    option = int(input("Auswahl: ").strip())

    if option == 1:
        if player.gold >= 1:
            player.gold -= 1
            # player.leben += 10

    if option == 2:
        if player.gold >= 5:
            player.gold -= 5
            # player.item = ["taktisches Langschwert", 5]

    if option == 3:
        level1(player)

    level1_shop(player)


def ende():
    print("ENDE")
    exit(0)

def level1(player: Player):
    player.options = "1. Ins Haus gehen\n2. Zum Shop gehen\n3. Spiel beenden"

    player.print_()

    option = int(input("Auswahl: ").strip())

    if option == 1:
        level1_haus(player)

    if option == 2:
        level1_shop(player)

    if option == 3:
        ende()

    level1(player)


if __name__ == '__main__':
    pl_name = input("Name: ")

    player_ = Player(pl_name)

    level1(player_)
"""

"""
# tik tak to
def print_feld():

    print("|", str(speil_feld[:3]).replace(",", " |").replace("[", "").replace("]", "").replace("'", ""), "|")
    print("-"*14)
    print("|", str(speil_feld[2:5]).replace(",", " |").replace("[", "").replace("]", "").replace("'", ""), "|")
    print("-" * 14)
    print("|", str(speil_feld[5:8]).replace(",", " |").replace("[", "").replace("]", "").replace("'", ""), "|\n")


def if_win():

    return False


def pl1_play():
    pl1 = input("ply1 : feld ? ")
    for index, value in enumerate(speil_feld):
        if value == pl1:
            speil_feld[index] = "O"

def pl2_play():
    pl2 = input("ply2 : feld ? ")
    for index, value in enumerate(speil_feld):
        if value == pl2:
            speil_feld[index] = "O"

if __name__ == '__main__':

    speil_feld = ["w", "e", "r", "s", "d", "f", "y", "c", "v"]

    print_feld()

    pl1_play()

    print_feld()

    if if_win():
        print("Player 1 Hat gewonen")
        exit(0)

    pl2_play()

    print_feld()

    if if_win():
        print("Player 2 Hat gewonen")
        exit(0)
        

"""

"""
def set_():
    pass
    # global i

    #i = 3
    #w = [3]

    #i += 1
    #w[0] += 1


if __name__ == '__main__':
    i = 1

    w = [1]

    set_()

    print(f"{i=}, {w=}")
"""