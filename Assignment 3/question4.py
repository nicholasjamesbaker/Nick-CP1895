import random


class RandomIntList(list):
    def __init__(self, number: int):
        super().__init__()
        self.__number = number

    def append_list(self, number):
        for i in range(number):
            self.append(random.randint(0, 100))

    def num_count(self):
        return len(self)

    def total(self):
        total = 0
        for i in self:
            total = i + total
        return total

    def average(self):
        total = 0
        for i in self:
            total = i + total
        return total / len(self)

    def __str__(self):
        delim = ", "
        s = delim.join(map(str, self))
        return s


def main():
    print("Random Integer List\n")
    keep_going = "y"
    random_int = int(input("How many random integers should the list contain?: "))
    while keep_going == "y":
        ran_list = RandomIntList(random_int)
        ran_list.append_list(random_int)
        print("\nRandom Integers")
        print("===============")
        print("Integers: ", ran_list)
        print("Count:    ", ran_list.num_count())
        print("Total:    ", ran_list.total())
        print("Average:  ", ran_list.average())
        print()

        keep_going = input("Continue? (y/n): ")
        if keep_going == "n":
            print("\nBye!")
            break


if __name__ == "__main__":
    main()
