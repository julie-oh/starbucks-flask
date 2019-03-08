from menu import Menu
from enum import Enum


class SizeEnum(Enum):
    TALL = 1
    GRANDE = 2
    VENTI = 3


class Beverage(Menu):
    def __init__(self, name, price, time, size):
        super().__init__(name, price, time)
        if isinstance(size, SizeEnum):
            self.size = size
        else:
            raise ValueError
        self.iced = False
        self.whip = False
        self.shot_add = 0


if __name__ == '__main__':
    tall = Beverage('a', 123, 123, SizeEnum.TALL)
    hotsix = Beverage('a', 123, 123, 'hotsix')