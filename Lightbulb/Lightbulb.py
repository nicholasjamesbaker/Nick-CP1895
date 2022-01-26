class Lightbulb:
    def __init__(self, wattage: int, is_led: bool, brand_name: str, is_on: bool = False, brightness: int = 0):
        print("init method is invoked")
        self.wattage = wattage
        self.is_led = is_led
        self.brand_name = brand_name
        self.is_on = is_on
        self.brightness = brightness

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def to_string(self):
        print(f"Lightbulb wattage is {self.wattage}, is it a LED? {self.is_led}"
              f", The brand is {self.brand_name}, the brightness level is {self.brightness}")

    def set_brightness(self, level):
        assert 0 <= level <= 10, "Level outside bounds"
        self.brightness = level


Lightbulb = Lightbulb(60, True, "EcoSmart", False, 0)

Lightbulb.turn_on()

Lightbulb.set_brightness(9)

Lightbulb.to_string()

