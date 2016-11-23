import random


class Characters:
    def __init__(self):
        self.level = 1
        self.health_point = 2 * self.level * self.random_dice()
        self.defend_point = (self.level / 2) * self.random_dice()
        self.strike_point = self.level * self.random_dice()
        self.position_x = 0
        self.position_y = 0

    def random_dice(self):
        result = random.randint(1, 6)
        return result

    def move_up(self):
        #if self.position_y > 1:
        self.position_y -= 1

    def move_down(self):
        #if self.position_y < 9:
        self.position_y += 1

    def move_left(self):
        #if self.position_x > 1:
        self.position_x += -1

    def move_right(self):
        #if self.position_x < 8:
        self.position_x += 1

class Hero(Characters):

    def __init__(self):
        super().__init__()
        self.max_health_point = 20 + self.level * 3 * self.random_dice()
        self.health_point = 20 + self.level * 3 * self.random_dice()
        self.defend_point = 2 * self.level * self.random_dice()
        self.strike_point = 5 + self.level * self.random_dice()


class Boss(Characters):
    def __init__(self):
        super().__init__()
        self.health_point = 2 * self.level * 2 * self.random_dice()
        self.defend_point = (self.level / 2) * self.random_dice() + (self.random_dice()/2)
        self.strike_point = self.level * self.random_dice() + self.level

"""
valami2 = Characters()
valami1 = Hero()
valami = Boss()
print(valami.health_point)
print(valami2.health_point)
print(valami1.health_point)
valami.move_right()
valami.move_right()
valami.move_left()
valami.move_down()
valami.move_down()
print(valami.position_x)
print(valami.position_y)
"""
