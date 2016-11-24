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
        self.draw_status()
        self.view.canvas.focus_set()
        self.start_game()

#***********************GENERATE ENEMIES****************************************
    #def generate_boss(slef):
    #    self.boss = TKWander_characters.Boss()
    #   self.boss.position_x = 9
    #    self.boss.position_y = 0


    def generate_skeletons(self):
        skel_number = random.randint(2, 5)
        while len(self.skeletons) < skel_number :
            skeleton = TKWander_characters.Characters()
            skeleton.position_x = random.randint(0, 10)
            skeleton.position_y = random.randint(0, 11)
            if self.move_validator(skeleton.position_x, skeleton.position_y) == True and (skeleton.position_x != 0 or skeleton.position_y !=0) and (skeleton.position_x != self.boss.position_x or skeleton.position_y != self.boss.position_y):
                self.skeletons.append(skeleton)


#**************************EVENTS***********************************************

    def keybind_events(self):
        self.view.canvas.bind('<w>', self.hero_up)
        self.view.canvas.bind('<s>', self.hero_down)
        self.view.canvas.bind('<a>', self.hero_left)
        self.view.canvas.bind('<d>', self.hero_right)
        self.view.canvas.bind('<space>', self.lets_fight)
        self.view.canvas.bind('<q>', self.go_next_level)
        self.view.canvas.bind('<r>', self.do_nothing)
#*********************************FIGHT*****************************************

    def hero_vs_boss(self):
        if self.hero.health_point <= 0:
            self.game_over()
        self.draw_status()
        print(self.hero.key, self.boss.health_point)
        if self.boss.health_point < 0:
            self.draw_boss(-2, -2)
        else:
            hero_sv = self.hero.strike_point + 2 * self.hero.random_dice()
            boss_sv = self.boss.strike_point + 2 * self.boss.random_dice()
            if hero_sv > self.boss.defend_point:
                self.boss.health_point -= (hero_sv - self.boss.defend_point)
            if self.boss.health_point > 0:
                if boss_sv > self.hero.defend_point:
                    self.hero.health_point -= (boss_sv - self.hero.defend_point)

    def hero_vs_skeleton(self):
        if self.hero.health_point <= 0:
            self.game_over()
        skel_i = self.battle_coord_validator()
        if self.skeletons[skel_i].health_point < 0:
            skeleton_id = self.skeletons[skel_i].id
            self.view.canvas.delete(skeleton_id)
        else:
            hero_sv = self.hero.strike_point + 2 * self.hero.random_dice()
            skel_sv = self.skeletons[skel_i].strike_point + 2 * self.skeletons[skel_i].random_dice()
            if hero_sv > self.skeletons[skel_i].defend_point:
                self.skeletons[skel_i].health_point -= (hero_sv - self.skeletons[skel_i].defend_point)
            if self.skeletons[skel_i].health_point > 0:
                if skel_sv > self.hero.defend_point:
                    self.hero.health_point -= (skel_sv - self.hero.defend_point)
            else:
                self.hero.level_up_hero()
                self.draw_status()
        if self.skeletons[0].health_point < 0:
            self.hero.key_collect()

    def lets_fight(self, event):
        if self.battle_coord_validator() == 500:
            self.hero_vs_boss()
        elif self.battle_coord_validator() in range(0, len(self.skeletons)):
            self.hero_vs_skeleton()


    def go_next_level(self, event):
        if self.hero.key > 0 and self.boss.health_point <= 0:
            self.map.get_next_map()
            self.hero.key = 0
            for skeleton in self.skeletons:
                self.view.canvas.delete(skeleton.id)
            self.skeletons = []
            self.draw_skeletons()
            self.draw_status()
            self.boss.level_up_boss()
            self.start_game()

#**************************CHARACTER MOVEMENT***********************************

    def move_skeletons(self):
        for i in range(len(self.skeletons)):
            valid = False
            while valid == False:
                movement = random.choice([[0, 1], [1, 0], [-1, 0], [0, -1]])
                movement_x = movement[0]
                movement_y = movement[1]
                if self.move_validator(self.skeletons[i].position_x+movement_x, self.skeletons[i].position_y+movement_y) == True and (self.skeletons[i].position_x+movement_x != 9 or self.skeletons[i].position_y+movement_y != 0):
                    skeleton_id = self.skeletons[i].id
                    self.view.canvas.delete(skeleton_id)
                    self.skeletons[i].position_x += movement_x
                    self.skeletons[i].position_y += movement_y
                    valid = True

    def hero_up(self, event):
        if self.move_validator(self.hero.position_x, self.hero.position_y-1) == True:
            self.hero.move_up()
        self.view.show_hero_back(self.hero.position_x, self.hero.position_y)
        self.step_count +=  1
        if self.step_count % 2 == 0:
            self.move_skeletons()
            self.draw_skeletons()
        #print(self.battle_coord_validator())

    def hero_down(self, event):
        if self.move_validator(self.hero.position_x, self.hero.position_y+1) == True:
            self.hero.move_down()
        self.view.show_hero_front(self.hero.position_x, self.hero.position_y)
        self.step_count +=  1
        if self.step_count % 2 == 0:
            self.move_skeletons()
            self.draw_skeletons()
        #print(self.battle_coord_validator())

    def hero_right(self, event):
        if self.move_validator(self.hero.position_x+1, self.hero.position_y) == True:
            self.hero.move_right()
        self.view.show_hero_right(self.hero.position_x, self.hero.position_y)
        self.step_count +=  1
        if self.step_count % 2 == 0:
            self.move_skeletons()
            self.draw_skeletons()
        #print(self.battle_coord_validator())

    def hero_left(self, event):
        if self.move_validator(self.hero.position_x-1, self.hero.position_y) == True:
            self.hero.move_left()
        self.view.show_hero_left(self.hero.position_x, self.hero.position_y)
        self.step_count +=  1
        if self.step_count % 2 == 0:
            self.move_skeletons()
            self.draw_skeletons()
        #print(self.battle_coord_validator())
#******************************Game Start*********************************************

    def start_game(self):
        self.hero.key = 0
        self.hero.position_x = 0
        self.hero.position_x = 0
        self.view.show_hero_front(0, 0)
        self.draw_boss(9, 0)
        self.generate_skeletons()
        self.draw_skeletons()
        self.keybind_events()

#************************DRAWING SECTION*****************************************
    def draw_status(self):
        self.view.draw_status_bar(self.hero.level, self.hero.max_health_point, self.hero.health_point, self.hero.defend_point, self.hero.strike_point, self.hero.key, self.map.map_number)

    def draw_game_map(self):
        self.view.draw_map(self.map.game_field1)

    def draw_skeletons(self):
            for skeleton in self.skeletons:
                if skeleton.health_point > 0:
                    self.view.show_skeleton(skeleton.position_x, skeleton.position_y, skeleton.id)

    def draw_boss(self, pos_x, pos_y):
            self.boss.position_x = pos_x
            self.boss.position_y = pos_y
            self.view.show_boss(self.boss.position_x, self.boss.position_y)

#*****************************VALIDATORS****************************************
    def move_validator(self, position_x, position_y):
        if position_x in range(0, 10) and position_y in range(0, 11):
            if self.map.game_field1[position_y][position_x] != 1:
                return True
        return False

    def battle_coord_validator(self):
        result = 0
        if self.hero.position_x == self.boss.position_x and self.hero.position_y == self.boss.position_y:
            return 500
        else:
            for i in range(len(self.skeletons)):
                if self.hero.position_x == self.skeletons[i].position_x and self.hero.position_y == self.skeletons[i].position_y:
                    #self.view.show_enemy_stat(self.skeletons[i].health_point, self.skeletons[i].defend_point, self.skeletons[i].strike_point)
                    result = i
                    return result

    def game_over(self):
        self.view.show_game_over()
        self.dead_keybind_events()

    def  dead_keybind_events(self):
        self.view.canvas.bind('<w>', self.do_nothing)
        self.view.canvas.bind('<s>', self.do_nothing)
        self.view.canvas.bind('<a>', self.do_nothing)
        self.view.canvas.bind('<d>', self.do_nothing)
        self.view.canvas.bind('<space>', self.do_nothing)
        self.view.canvas.bind('<q>', self.do_nothing)
        self.view.canvas.bind('<r>', self.restart_game)

    def do_nothing(self, event):
        pass

    def restart_game(self, event):
        self.view.canvas.delete(self.view.text2)
        self.hero.health_point = self.hero.max_health_point
        self.draw_status()
        self.start_game()

valami = Control()
valami.view.canvas.mainloop()
