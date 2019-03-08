from beverage import Beverage
from menu import beverage_set, dessert_set

class Partner:
    def __int__(self, nickname):
        self.nickname = nickname

    def make(self, menu):
        print(menu.name)

    def take_order(self, order):
        print(order)

        menu = Beverage('americano', '4000', '1', 'grande')
        return menu

