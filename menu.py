from enum import Enum


class MenuKindEnum(Enum):
    BEVERAGE = 1
    DESSERT = 2


menu_kind_dict = {
    MenuKindEnum.BEVERAGE: {'americano', 'latte', 'green tea'},
    MenuKindEnum.DESSERT: {'cake', 'cookie', 'bagel'}
}


class Menu:
    def __init__(self, name, price, time):
        self.name = name
        self.price = price
        self.time = time

    def menu_kind(self, menu_name):
        for k, v in menu_kind_dict.items():
            if menu_name in v:
                return k
        return None
