print("Enter 2 words and we will determine if they an anagram of each other")
while True:
    choice = "y"
    word1 = input("Word 1: ")
    word2 = input("Word 2: ")
    word1_dict = dict.fromkeys(word1)
    word2_dict = dict.fromkeys(word2)

    sort_word1 = sorted(word1_dict.keys())
    sort_word2 = sorted(word2_dict.keys())

    if sort_word1 == sort_word2:
        print("It's an anagram!")
    else:
        print("It's not an anagram.")

    choice = input("Keep going? (y/n) ")
    if choice == "n":
        print("Bye!")
        break
