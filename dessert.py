from menu import Menu

class Dessert(Menu):
    def __init__(self, name, price, time):
        super().__init__(name, price, time)
        heat_up = False
        fork_cnt = 2