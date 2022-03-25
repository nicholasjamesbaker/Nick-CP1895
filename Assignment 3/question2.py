import random


class Player:
    def __init__(self, name: str, value: str):
        self.__name = name
        self.__value = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        self.__name = n

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, v):
        self.__value = v


class Bart(Player):
    def __init__(self, name: str, value: str):
        Player.__init__(self, "Bart", value)

    def generateRoshambo(self):
        self.value = "rock"


class Lisa(Player):
    def __init__(self, name: str, value: str):
        Player.__init__(self, "Lisa", value)

    def generateRoshambo(self):
        choices = ("rock", "paper", "scissors")
        self.value = random.choice(choices)


def main():
    print("Roshambo Game")
    name = input("\nEnter your name: ")
    player_wins = 0
    player_losses = 0
    bart_wins = 0
    bart_losses = 0
    lisa_wins = 0
    lisa_losses = 0
    keep_going = "y"
    while keep_going == "y":
        choice = input("\nWould you like to play Bart of Lisa? (b/l): ")
        value = input("\nRock, paper, or scissors? (r/p/s): ")
        print()
        player = Player(name, value)
        bart = Bart(name, value)
        bart.generateRoshambo()
        lisa = Lisa(name, value)
        lisa.generateRoshambo()
        if choice == "b":
            if player.value == "r":
                player.value = "rock"
                print(player.name + ": " + player.value)
                print(bart.name + ": " + bart.value)
                print("Draw!")
            elif player.value == "p":
                player.value = "paper"
                print(player.name + ": " + player.value)
                print(bart.name + ": " + bart.value)
                print(player.name + " wins!")
                player_wins = player_wins + 1
                bart_losses = bart_losses + 1
            elif player.value == "s":
                player.value = "scissors"
                print(player.name + ": " + player.value)
                print(bart.name + ": " + bart.value)
                print(bart.name + " wins!")
                bart_wins = bart_wins + 1
                player_losses = player_losses + 1
            else:
                print("Wrong letter entered")
        elif choice == "l":
            if player.value == "r":
                player.value = "rock"
                if lisa.value == "rock":
                    print(player.name + ": " + player.value)
                    print(lisa.name + ": " + lisa.value)
                    print("Draw!")
                elif lisa.value == "paper":
                    print(player.name + ": " + player.value)
                    print(lisa.name + ": " + lisa.value)
                    print(lisa.name + " wins!")
                    lisa_wins = lisa_wins + 1
                    player_losses = player_losses + 1
                else:
                    print(player.name + ": " + player.value)
                    print(lisa.name + ": " + lisa.value)
                    print(player.name + " wins!")
                    player_wins = player_wins + 1
                    lisa_losses = lisa_losses + 1
            elif player.value == "p":
                player.value = "paper"
                if lisa.value == "rock":
                    print(player.name + ": " + player.value)
                    print(lisa.name + ": " + lisa.value)
                    print(player.name + " wins!")
                    player_wins = player_wins + 1
                    lisa_losses = lisa_losses + 1
                elif lisa.value == "paper":
                    print(player.name + ": " + player.value)
                    print(lisa.name + ": " + lisa.value)
                    print("Draw!")
                else:
                    print(player.name + ": " + player.value)
                    print(lisa.name + ": " + lisa.value)
                    print(lisa.name + " wins!")
                    lisa_wins = lisa_wins + 1
                    player_losses = player_losses + 1
            elif player.value == "s":
                player.value = "scissors"
                if lisa.value == "rock":
                    print(player.name + ": " + player.value)
                    print(lisa.name + ": " + lisa.value)
                    print(lisa.name + " wins!")
                    lisa_wins = lisa_wins + 1
                    player_losses = player_losses + 1
                elif lisa.value == "paper":
                    print(player.name + ": " + player.value)
                    print(lisa.name + ": " + lisa.value)
                    print(player.name + " wins!")
                    player_wins = player_wins + 1
                    lisa_losses = lisa_losses + 1
                else:
                    print(player.name + ": " + player.value)
                    print(lisa.name + ": " + lisa.value)
                    print("Draw!")
            else:
                print("Wrong letter entered")

        keep_going = input("\nPlay again? (y/n): ")
        if keep_going == "n":
            print("\nResults: ")
            print(player.name + " wins: " + str(player_wins))
            print(player.name + " losses: " + str(player_losses))
            print(bart.name + " wins: " + str(bart_wins))
            print(bart.name + " losses: " + str(bart_losses))
            print(lisa.name + " wins: " + str(lisa_wins))
            print(lisa.name + " losses: " + str(lisa_losses))
            print("\nThanks for playing!")
            break


if __name__ == "__main__":
    main()
