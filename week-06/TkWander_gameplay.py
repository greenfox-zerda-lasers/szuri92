import TKWander_view
import TKWander_map
import TKWander_characters
import random

class Control:
    def __init__(self):
        self.view = TKWander_view.GameDisplay()
        self.map = TKWander_map.GameMap()
        self.skeleton = TKWander_characters.Characters()
        self.hero = TKWander_characters.Hero()
        self.boss = TKWander_characters.Boss()
        self.step_count =  0
        self.draw_game_map()
        self.view.show_hero_front(0, 0)
        self.view.show_boss(random.randint(1, 9), random.randint(1, 10))
        self.keybind_events()
        self.view.canvas.focus_set()


    def keybind_events(self):
        self.view.canvas.bind('<w>', self.hero_up)
        self.view.canvas.bind('<s>', self.hero_down)
        self.view.canvas.bind('<a>', self.hero_left)
        self.view.canvas.bind('<d>', self.hero_right)

    def hero_up(self, event):
        if self.move_validator(self.hero.position_x, self.hero.position_y-1) == True:
        #if self.map.game_field[self.hero.position_y-1][self.hero.position_x] != 1:
            self.hero.move_up()
        self.view.show_hero_back(self.hero.position_x, self.hero.position_y)
        self.step_count +=  1

    def hero_down(self, event):
        if self.move_validator(self.hero.position_x, self.hero.position_y+1) == True:
        #if self.map.game_field[self.hero.position_y+1][self.hero.position_x] != 1:
            self.hero.move_down()
        self.view.show_hero_front(self.hero.position_x, self.hero.position_y)
        self.step_count +=  1

    def hero_right(self, event):
        if self.move_validator(self.hero.position_x+1, self.hero.position_y) == True:
        #if self.map.game_field[self.hero.position_y][self.hero.position_x+1] != 1:
            self.hero.move_right()
        self.view.show_hero_right(self.hero.position_x, self.hero.position_y)
        self.step_count +=  1

    def hero_left(self, event):
        if self.move_validator(self.hero.position_x-1, self.hero.position_y) == True:
        #if self.map.game_field[self.hero.position_y][self.hero.position_x-1] != 1:
            self.hero.move_left()
        self.view.show_hero_left(self.hero.position_x, self.hero.position_y)
        self.step_count +=  1

    #def boss_move(self)


    def draw_game_map(self):
        self.view.draw_map(self.map.game_field, self.hero.health_point, self.hero.defend_point, self.hero.strike_point)



    def move_validator(self, position_x, position_y):
        if position_x in range(0, 10) and position_y in range(0, 11):
            if self.map.game_field[position_y][position_x] != 1:
                return True
            else:
                return False



valami = Control()
valami.view.canvas.mainloop()
