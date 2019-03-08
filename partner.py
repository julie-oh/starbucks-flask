from menu import Menu, MenuKindEnum
from beverage import Beverage
from dessert import Dessert


class Partner:
    def __int__(self, nickname):
        self.nickname = nickname

    def make(self, menu):
        print(menu.name)

    def take_order(self, order_req):
        # m = Menu('m', 12, 131)
        # m.menu_kind('americano')

        # static method: 인스턴스를 생성하지 않고 메소드를 사용하고 싶을 떄
        #                want to use method without constructing instance


        order_item = order_req['order']
        total_order = {'price': 0, 'time': 0}

        for order in order_item:
            menu_kind = Menu.menu_kind(order['name'])
            if menu_kind == MenuKindEnum.BEVERAGE:
                ordered_menu = Beverage(order['name'], order['price'], order['time'])
                ordered_menu.set_options(order)
            elif menu_kind == MenuKindEnum.DESSERT:
                ordered_menu = Dessert(order['name'], order['price'], order['time'])
            else:
                raise ValueError('not match menu type! try again :( ')
            total_order['price'] += ordered_menu.price
            total_order['time'] += ordered_menu.time

        return total_order
