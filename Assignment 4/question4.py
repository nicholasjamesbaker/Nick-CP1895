import random

winning_numbers = {9, 20, 27, 35, 37, 43}


def random_set():
    random_numbers = set()
    while len(random_numbers) < 6:
        random_number = random.randint(1, 49)
        random_numbers.add(random_number)
    return random_numbers


def winner_check(numbers):
    if len(winning_numbers.difference(numbers)) == 4:
        return "2 number matched, you win a free play!"
    elif len(winning_numbers.difference(numbers)) == 3:
        return "3 numbers matched, you win $10!"
    elif len(winning_numbers.difference(numbers)) == 2:
        return "4 numbers matched, you win $90.50!"
    elif len(winning_numbers.difference(numbers)) == 1:
        return "5 numbers matched, you win $5000!"
    elif len(winning_numbers.difference(numbers)) == 0:
        return "6 numbers matched, you win $13,000,000!"
    else:
        return "No numbers matched, please try again!"


def main():
    print("Winning numbers:",winning_numbers)
    your_numbers = random_set()
    print("Your numbers:", your_numbers)
    print(winner_check(your_numbers))


if __name__ == "__main__":
    main()
