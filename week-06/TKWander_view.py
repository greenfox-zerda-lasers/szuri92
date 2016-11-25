from tkinter import *
from PIL import Image, ImageTk


class GameDisplay:

    def __init__(self):
        self.resize_value = 55
        self.root = Tk()
        self.canvas_width = 1000
        self.canvas_height =900
        self.resized_floor = self.resize("C:/Users/Gáspár/Desktop/Tk_wander/b-floor.gif", self.resize_value, self.resize_value)
        #self.resized_floor = self.resize("floor.png", self.resize_value, self.resize_value)
        self.resized_hero_front = self.resize("C:/Users/Gáspár/Desktop/Tk_wander/c3po_front.gif", self.resize_value, self.resize_value)
        self.resized_hero_right = self.resize("C:/Users/Gáspár/Desktop/Tk_wander/c3po_right.gif", self.resize_value, self.resize_value)
        self.resized_hero_left = self.resize("C:/Users/Gáspár/Desktop/Tk_wander/c3po_left.gif", self.resize_value, self.resize_value)
        self.resized_hero_back = self.resize("C:/Users/Gáspár/Desktop/Tk_wander/c3po_back.png", self.resize_value, self.resize_value)
        self.resized_wall = self.resize("C:/Users/Gáspár/Desktop/Tk_wander/b-wall.gif", self.resize_value, self.resize_value)
        self.resized_boss = self.resize("C:/Users/Gáspár/Desktop/Tk_wander/lord_veder.png", self.resize_value, self.resize_value)
        self.resized_skeleton = self.resize("C:/Users/Gáspár/Desktop/Tk_wander/stormtroop.png", self.resize_value, self.resize_value)
        self.resized_logo =  self.resize("C:/Users/Gáspár/Desktop/Tk_wander/logo.png", 400, 500)
        self.canvas = Canvas(self.root, height = self.canvas_height, width = self.canvas_width, bg = 'black')
        self.hero = -10
        self.boss = -11
        self.text = -23
        self.enemy_text = None
        self.canvas.pack()

    def resize(self, img_path, width, height):
        image = Image.open(img_path)
        resized_image = image.resize((width, height), Image.ANTIALIAS)
        return ImageTk.PhotoImage(resized_image)

    def draw_map(self, game_field):
        for i in range(10):
            for j in range(11):
                if game_field[j][i] == 0:
                    self.canvas.create_image(i*self.resize_value, j*self.resize_value, anchor=NW, image = self.resized_floor)
                else:
                    self.canvas.create_image(i*self.resize_value, j*self.resize_value, anchor=NW, image = self.resized_wall)


    def draw_status_bar(self, hero_lvl, hero_max, hero_hp, hero_dp, hero_sp, hero_key, map_lev):
        self.canvas.delete(self.text)
        self.text = self.canvas.create_text(275, 620, fill='white', font="Times 12 bold",  text="Hero  ( Level {} )   HP: {}/{}   | DP: {}   | SP: {}   | key {}     | Map:         {}".format(hero_lvl, hero_max ,hero_hp, hero_dp, hero_sp, hero_key, map_lev))

    def show_hero_front(self, position_x, position_y):
        self.canvas.delete(self.hero)
        self.hero = self.canvas.create_image(position_x*self.resize_value, position_y*self.resize_value, anchor =NW, image = self.resized_hero_front)

    def show_hero_right(self, position_x, position_y):
        self.canvas.delete(self.hero)
        self.hero = self.canvas.create_image(position_x*self.resize_value, position_y*self.resize_value, anchor =NW, image = self.resized_hero_right)

    def show_hero_left(self, position_x, position_y):
        self.canvas.delete(self.hero)
        self.hero = self.canvas.create_image(position_x*self.resize_value, position_y*self.resize_value, anchor =NW, image = self.resized_hero_left)

    def show_hero_back(self, position_x, position_y):
        self.canvas.delete(self.hero)
        self.hero = self.canvas.create_image(position_x*self.resize_value, position_y*self.resize_value, anchor =NW, image = self.resized_hero_back)

    def show_boss(self, position_x, position_y):
        self.canvas.delete(self.boss)
        self.boss = self.canvas.create_image(position_x*self.resize_value, position_y*self.resize_value, anchor =NW, image = self.resized_boss)

    def show_skeleton(self, position_x, position_y, skel_id):
        #self.canvas.delete(self.skeleton)
        self.skeleton = self.canvas.create_image(position_x*self.resize_value, position_y*self.resize_value, anchor =NW, image = self.resized_skeleton, tag = skel_id)

    def show_game_over(self):
        self.text2 = self.canvas.create_text(200, 200, fill = 'tomato', font = 'Times 100 bold', text = "Game\n Over!" )

    def show_enemy_stat(self, enemy_hp, enemy_sp, enemy_dp):
        self.canvas.delete(self.enemy_text)
        self.enemy_text = self.canvas.create_text(275, 620, fill='white', font="Times 12 bold",  text="Enemy HP: {}/{}  | DP: {}  | SP:  {}".format(enemy_hp, enemy_sp, enemy_dp))

    def game_logo(self):
        self.canvas.create_image(550, 20, anchor = NW, image = self.resized_logo)
