from question1 import Queue


def mirror(letters):
    mirror_size = letters.length()
    mirror_letters = []
    while mirror_size > 0:
        letter = letters.queue[0]
        letters.queue.append(letter)
        mirror_letters.append(letter)
        letters.queue.pop(0)
        mirror_size -= 1
    while len(mirror_letters) != 0:
        element = mirror_letters[len(mirror_letters) - 1]
        letters.queue.append(element)
        mirror_letters.pop()


def main():
    letters = Queue()
    while True:
        letter = input("Enter letter, enter % to stop: ")
        if letter == "%":
            break
        else:
            letters.enqueue(letter)
    mirror(letters)
    print(letters)


if __name__ == "__main__":
    main()
