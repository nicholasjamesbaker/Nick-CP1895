class Lightbulb:
    def __init__(self, wattage = 0, is_led = bool, brand_name = "", is_on = bool):
        print("init method is invoked")
        self.wattage = wattage
        self.is_led = is_led
        self.brand_name = brand_name
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def to_string(self):
        print(self.wattage, self.is_led, self.brand_name)

    def set_brightness(self, level):
        level = int(input("Set brightness level (0-100)"))
