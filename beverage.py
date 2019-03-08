from menu import Menu

class Beverage(Menu):
    def __init__(self, name, price, time, size):
        super().__init__(name, price, time)
        self.size = size
        self.iced = False
        self.whip = False
        self.shot_add = 0