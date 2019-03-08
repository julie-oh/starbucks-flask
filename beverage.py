from menu import Menu
from enum import Enum


class SizeEnum(Enum):
    TALL = 1
    GRANDE = 2
    VENTI = 3


class Beverage(Menu):
    def __init__(self, name, price, time, size=SizeEnum.TALL):
        super().__init__(name, price, time)
        if isinstance(size, SizeEnum):
            self.size = size
        else:
            raise ValueError
        self.iced = False
        self._whip = False
        self._shot_add = 0

    ''' 
        property decorator 는 보통 getter로 쓰인다. 보통 생성사를 생성하고 접근할 때
        멤버변수에 접근하는게 보통이지만 getter로 정의되있으면 사실 method로 접근하는 것이다.
        
        property is usually used as getter.
        incase of using getter, this seems like general construction instance and access member variable
        but uses method 
    '''

    # propery member variable
    @property # x = beverage.whip
    def whip(self):
        return self._whip

    @whip.setter  # beverage.whip = True
    def whip(self, whip):
        if whip:
            self.price += 500
            self._whip = whip

    @property
    def shot_add(self):
        return self._shot_add

    @shot_add.setter
    def shot_add(self, shot):
        if isinstance(shot, int):
            self.price += 500 * shot
            self._shot_add = shot

    def set_options(self, options):
        for opt_name in options:
            if hasattr(self, opt_name):
                if opt_name == 'whip':
                    self.whip = options[opt_name]
                elif opt_name == 'shot_add':
                    self.shot_add = options[opt_name]
                else:
                    setattr(self, opt_name, options[opt_name])

    def __str__(self):
        return 'name: {}, price: {}, time: {}, size: {}, iced: {}, whip: {}, shot_added: {}'.format(
            self.name, self.price, self.time, self.size.name, self.iced, self.whip, self.shot_add)


if __name__ == '__main__':
    tall = Beverage('a', 123, 123, SizeEnum.TALL)
    hotsix = Beverage('a', 123, 123, 'hotsix')