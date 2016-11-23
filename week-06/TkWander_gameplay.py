import TKWander_view
import TKWander_map
import TKWander_characters
import random

class Control:
    def __init__(self):
        self.view = TKWander_view.GameDisplay()
        self.map = TKWander_map.GameMap()
        self.skeletons =[]
        self.hero = TKWander_characters.Hero()
        self.boss = TKWander_characters.Boss()
        self.step_count =  0
        self.draw_game_map()
        self.game_running = False
        self.view.canvas.focus_set()
        #self.skeleton_number = 0
        self.start_game()
        #self.view.show_hero_front(0, 0)
        #self.view.show_boss(random.randint(1, 9), random.randint(1, 10))
        #self.keybind_events()
        #self.view.canvas.focus_set()

#***********************Generate ENEMIES SECTION*******************************
    def generate_skeletons(self):
        skel_number = random.randint(2, 5)
        while len(self.skeletons) < skel_number :
            skeleton = TKWander_characters.Characters()
            skeleton.position_x = random.randint(0, 10)
            skeleton.position_y = random.randint(0, 11)
            if self.move_validator(skeleton.position_x, skeleton.position_y) == True and skeleton.position_x != 0 and skeleton.position_y !=0 and skeleton.position_x != self.boss.position_x and skeleton.position_y != self.boss.position_y:
                self.skeletons.append(skeleton)

    def draw_boss(self):
        valid = False
        while valid == False:
            self.boss.position_x = random.randint(0, 9)
            self.boss.position_y = random.randint(0, 10)
            if self.move_validator(self.boss.position_x, self.boss.position_y) == True and self.boss.position_x != 0 and self.boss.position_y !=0:
                self.view.show_boss(self.boss.position_x, self.boss.position_y)
                valid = True

#**************************CHARACTERS MOVEMENT SECTION*********************************

    def move_skeletons(self):
        for i in range(len(self.skeletons)):
            valid = False
            while valid == False:
                movement = random.choice([[0, 1], [1, 0], [-1, 0], [0, -1]])
                movement_x = movement[0]
                movement_y = movement[1]
                #print(movement_y)
                #print(self.move_validator(self.skeletons[i].position_x+movement_x, self.skeletons[i].position_y+movement_y))
                if self.move_validator(self.skeletons[i].position_x+movement_x, self.skeletons[i].position_y+movement_y) == True:
                    #print(movement_y)
                    #print(self.skeletons[i].position_x, self.skeletons[i].position_y)
                    skeleton_id = self.skeletons[i].id
                    self.view.canvas.delete(skeleton_id)
                    self.skeletons[i].position_x += movement_x
                    self.skeletons[i].position_y += movement_y
                    valid = True




    def keybind_events(self):
        self.view.canvas.bind('<w>', self.hero_up)
        self.view.canvas.bind('<s>', self.hero_down)
        self.view.canvas.bind('<a>', self.hero_left)
        self.view.canvas.bind('<d>', self.hero_right)

    def hero_up(self, event):
        #print(self.skeletons[1].position_x)
        #print(self.skeletons[0].position_x)
        #print(self.step_count)
        if self.move_validator(self.hero.position_x, self.hero.position_y-1) == True:
        #if self.map.game_field[self.hero.position_y-1][self.hero.position_x] != 1:
            self.hero.move_up()
        self.view.show_hero_back(self.hero.position_x, self.hero.position_y)
        self.step_count +=  1
        if self.step_count % 2 == 0:
            self.move_skeletons()
            self.draw_skeletons()

    def hero_down(self, event):
        if self.move_validator(self.hero.position_x, self.hero.position_y+1) == True:
        #if self.map.game_field[self.hero.position_y+1][self.hero.position_x] != 1:
            self.hero.move_down()
        self.view.show_hero_front(self.hero.position_x, self.hero.position_y)
        self.step_count +=  1
        if self.step_count % 2 == 0:
            self.move_skeletons()
            self.draw_skeletons()

    def hero_right(self, event):
        if self.move_validator(self.hero.position_x+1, self.hero.position_y) == True:
        #if self.map.game_field[self.hero.position_y][self.hero.position_x+1] != 1:
            self.hero.move_right()
        self.view.show_hero_right(self.hero.position_x, self.hero.position_y)
        self.step_count +=  1
        if self.step_count % 2 == 0:
            self.move_skeletons()
            self.draw_skeletons()

    def hero_left(self, event):
        if self.move_validator(self.hero.position_x-1, self.hero.position_y) == True:
        #if self.map.game_field[self.hero.position_y][self.hero.position_x-1] != 1:
            self.hero.move_left()
        self.view.show_hero_left(self.hero.position_x, self.hero.position_y)
        self.step_count +=  1
        if self.step_count % 2 == 0:
            self.move_skeletons()
            self.draw_skeletons()

#******************************Game Play*********************************************
    def start_game(self):
        self.game_running = True
        self.view.show_hero_front(0, 0)
        self.draw_boss()
        #self.view.show_boss(random.randint(0, 9), random.randint(0, 10))
        self.generate_skeletons()
        self.draw_skeletons()
        #self.game_loop()
        self.keybind_events()


    #def game_loop(self):
    #    while self.hero.healt_point > 0:
    #        self.keybind_events()


    def draw_game_map(self):
        self.view.draw_map(self.map.game_field, self.hero.health_point, self.hero.defend_point, self.hero.strike_point)


    def draw_skeletons(self):
            for skeleton in self.skeletons:
                self.view.show_skeleton(skeleton.position_x, skeleton.position_y, skeleton.id)
            #self.keybind_events()

    def move_validator(self, position_x, position_y):
        if position_x in range(0, 10) and position_y in range(0, 11):
            if self.map.game_field[position_y][position_x] != 1:
                return True
        return False


valami = Control()
valami.view.canvas.mainloop()
