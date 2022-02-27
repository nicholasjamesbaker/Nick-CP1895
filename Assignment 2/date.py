class Date:
    def __init__(self, year: int, month: int, day: int):
        self.__year = year
        self.__month = month
        self.__day = day
        if not isinstance(year, int):
            raise TypeError("Year must be int")
        if not isinstance(month, int):
            raise TypeError("Month must be int")
        if not isinstance(day, int):
            raise TypeError("Day must be int")
        if isinstance(day, bool):
            raise TypeError("No booleans allowed")
        if not 0 < year < 2099:
            raise ValueError("Must be a valid year")
        if not 0 < month < 13:
            raise ValueError("Must be valid month")
        if not 0 < day < 32:
            raise ValueError("Must be valid day")

    def __str__(self):
        return f"{str(self.__day).zfill(2)}/{str(self.__month).zfill(2)}/{self.__year}"

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, d):
        self.__day = d

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, m):
        self.__month = m

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, y):
        self.__year = y

    @property
    def is_leap_year(self):
        if (self.__year % 400 == 0) and (self.__year % 100 == 0):
            return True
        elif (self.__year % 4 == 0) and (self.__year % 100 != 0):
            return True
        else:
            return False

    @property
    def is_valid_date(self):
        dd = self.__day
        mm = self.__month
        yy = self.__year
        if mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12:
            max1 = 31
        elif mm == 4 or mm == 6 or mm == 9 or mm == 11:
            max1 = 30
        elif yy % 4 == 0 and yy % 100 != 0 or yy % 400 == 0:
            max1 = 29
        else:
            max1 = 28
        if mm < 1 or mm > 12:
            return False
        elif dd < 1 or dd > max1:
            return False
        elif dd == max1 and mm != 12:
            return True
        elif dd == 31 and mm == 12:
            return True
        else:
            return True
