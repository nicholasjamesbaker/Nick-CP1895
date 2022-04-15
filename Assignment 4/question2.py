from question1 import Stack


def reverse(numbers):
    while numbers.length() > 0:
        current_letter = numbers.pop()
        print(current_letter)


def main():
    numbers = Stack()
    while True:
        number = int(input("Enter integer, enter -1 to stop: "))
        numbers.push(number)
        if number == -1:
            numbers.pop()
            break
    reverse(numbers)


if __name__ == "__main__":
    main()
