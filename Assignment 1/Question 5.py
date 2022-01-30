text_to_numbers = {'.': 1, ',': 11, '?': 111, '!': 1111, ':': 11111, 'a': 2, 'b': 22, 'c': 222,
                   'd': 3, 'e': 33, 'f': 333, 'g': 4, 'h': 44, 'i': 444, 'j': 5, 'k': 55,
                   'l': 555, 'm': 6, 'n': 66, 'o': 666, 'p': 7, 'q': 77, 'r': 777, 's': 7777,
                   't': 8, 'u': 88, 'v': 888, 'w': 9, 'x': 99, 'y': 999, 'z': 9999, ' ': 0}

print("T9 key display for entered text message")
while True:
    choice = "y"
    word = input("Please enter the word: ")
    word = word.lower()

    score_total = ""
    for i in word:
        if i in text_to_numbers:
            score_total += str(text_to_numbers[i])
        else:
            print(i, "will be ignored. Information below may be incorrect.")

    print("The key presses for", word, "are:", score_total)

    choice = input("Keep going? (y/n) ")
    if choice == "n":
        print("Bye!")
        break
