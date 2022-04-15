import random

winning_numbers = {9, 20, 27, 35, 37, 43}


def random_set():
    random_numbers = set()
    while len(random_numbers) < 6:
        random_number = random.randint(1, 49)
        random_numbers.add(random_number)
    return random_numbers


def lottery(amount_of_times):
    cost_to_play = 0
    amount_won = 0
    counter = 0
    for i in range(amount_of_times + 1):
        cost_to_play = i * 2
        your_numbers = random_set()
        amount_won += winner_check(your_numbers)
        counter = i
    total = amount_won - cost_to_play
    print("You played the lottery", counter, "time(s)")
    print("It cost you $" + str(cost_to_play), "to play")
    print("You won: $" + str(amount_won))
    if total > 1:
        return "Amount profited: $" + str(total)
    elif total < 0:
        total = abs(total)
        return "Amount lost: $" + str(total)
    else:
        return "You broke even: $" + str(total)



def winner_check(numbers):
    if len(winning_numbers.difference(numbers)) == 4:
        return 2
    elif len(winning_numbers.difference(numbers)) == 3:
        return 10
    elif len(winning_numbers.difference(numbers)) == 2:
        return 90.50
    elif len(winning_numbers.difference(numbers)) == 1:
        return 5000
    elif len(winning_numbers.difference(numbers)) == 0:
        return 13000000
    else:
        return 0


def main():
    amount = int(input("How many times would you like to play the lottery? ($2 fee): "))
    print("Winning numbers:", winning_numbers)
    print(lottery(amount))


if __name__ == "__main__":
    main()
