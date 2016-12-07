import random

class Characters:

    count = 0
    @classmethod
    def count_increment(cls):
        cls.count += 1

    def __init__(self):
        self.count_increment()
        self.id = 'skeleton' + str(self.count)
        self.level = 1
        self.max_health_point = 2 * (self.level + 1) * self.random_dice()
        self.health_point = self.max_health_point
        self.defend_point = (self.level / 2) * self.random_dice()
        self.strike_point = self.level * self.random_dice()
        self.position_x = 0
        self.position_y = 0

    def level_up_skel(self):
        self.level += 1
        self.max_health_point = 2 * (self.level + 1) * self.random_dice()
        self.defend_point = (self.level / 2) * self.random_dice()
        self.strike_point = self.level * self.random_dice()

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
        self.max_health_point = 20 + 3 * self.random_dice()
        self.health_point = self.max_health_point
        self.defend_point = 2 * self.level * self.random_dice()
        self.strike_point = 5 + self.level * self.random_dice()
        self.key = 0

    def key_collect(self):
        self.key = 1

    def level_up_hero(self):
        self.level += 1
        self.max_health_point += self.random_dice()
        self.defend_point += self.random_dice()
        self.strike_point += self.random_dice()

class Boss(Characters):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.max_health_point = 10 + 3 * self.level * self.random_dice() + self.random_dice()
        self.health_point = self.max_health_point
        self.defend_point = (self.level / 2) * self.random_dice() + (self.random_dice()/2)
        self.strike_point = self.level * self.random_dice() + (self.level+1)

    def level_up_boss(self):
        self.level += 1
        self.max_health_point = 10 + 3 * self.level * self.random_dice() + self.random_dice()
        self.health_point = self.max_health_point
        self.defend_point = (self.level / 2) * self.random_dice() + (self.random_dice()/2)
        self.strike_point = self.level * self.random_dice() + (self.level+1)
