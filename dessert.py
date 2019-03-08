from menu import Menu


class Dessert(Menu):
    def __init__(self, name, price, time):
        super().__init__(name, price, time)
        heat_up = False
        fork_cnt = 2

    def __str__(self):
        return 'name: {}, price: {}, time: {}'.format(
            self.name, self.price, self.time)