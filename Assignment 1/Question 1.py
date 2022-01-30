def main():
    provinces = {'A': "Newfoundland", 'B': "Nova Scotia", 'C': "Prince Edward Island",
                 'E': "New Brunswick", 'G': "Quebec", 'H': "Quebec", 'J': "Quebec",
                 'K': "Ontario", 'L': "Ontario", 'M': "Ontario", 'N': "Ontario", 'P': "Ontario",
                 'R': "Manitoba", 'S': "Saskatchewan", 'T': "Alberta", 'V': "British Columbia",
                 'X': "Nunavut and Northwest Territories", 'Y': "Yukon"}

    while True:
        choice = "y"
        postal_code = input("Enter postal code: ")
        if postal_code[0].upper() in provinces:
            if postal_code[1] == "0":
                province = provinces[postal_code[0].upper()]
                print("Postal code is for a rural address in", province)
            else:
                province = provinces[postal_code[0].upper()]
                print("Postal code is for an urban address in", province)
        else:
            print("There is no Province with this initial, please try again.")
        choice = input("Keep going? (y/n) ")
        if choice == "n":
            print("Bye!")
            break


if __name__ == "__main__":
    main()
