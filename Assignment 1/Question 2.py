while True:
    choice = "y"
    basic_string = input("Enter a string and we will determine how many unique characters there are!\n")
    determine_dict = dict.fromkeys(basic_string)
    print("There is/are", len(determine_dict.keys()), "unique character(s) in", basic_string)
    choice = input("Keep going? (y/n) ")
    if choice == "n":
        print("Bye!")
        break
