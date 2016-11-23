from tkinter import *
from PIL import Image, ImageTk


class GameDisplay:

    def __init__(self):
        self.resize_value = 55
        self.root = Tk()
        self.canvas_width = 800
        self.canvas_height =900
        self.resized_floor = self.resize("C:/Users/Gáspár/Desktop/floor.png", self.resize_value, self.resize_value)
        self.resized_hero_front = self.resize("C:/Users/Gáspár/Desktop/hero_front.png", self.resize_value, self.resize_value)
        self.resized_hero_right = self.resize("C:/Users/Gáspár/Desktop/hero-right.png", self.resize_value, self.resize_value)
        self.resized_hero_left = self.resize("C:/Users/Gáspár/Desktop/hero-left.png", self.resize_value, self.resize_value)
        self.resized_hero_back = self.resize("C:/Users/Gáspár/Desktop/hero-back.png", self.resize_value, self.resize_value)
        self.resized_wall = self.resize("C:/Users/Gáspár/Desktop/wall.png", self.resize_value, self.resize_value)
        self.resized_boss = self.resize("C:/Users/Gáspár/Desktop/boss.png", self.resize_value, self.resize_value)
        self.canvas = Canvas(self.root, height = self.canvas_height, width = self.canvas_width, bg = 'silver')
        self.hero = -10
        self.boss = -11
        self.canvas.pack()

    def resize(self, img_path, width, height):
        image = Image.open(img_path)
        resized_image = image.resize((width, height), Image.ANTIALIAS)
        return ImageTk.PhotoImage(resized_image)

    def draw_map(self, game_field, hero_hp, hero_dp, hero_sp):
        for i in range(10):
            for j in range(11):
                if game_field[j][i] == 0:
                    self.canvas.create_image(i*self.resize_value, j*self.resize_value, anchor=NW, image = self.resized_floor)
                else:
                    self.canvas.create_image(i*self.resize_value, j*self.resize_value, anchor=NW, image = self.resized_wall)
        self.draw_status_bar(hero_hp, hero_dp, hero_sp)

    def draw_status_bar(self, hero_hp, hero_dp, hero_sp):
        self.canvas.create_text(275, 620, fill='black', font="Times 12 bold",  text="Stats: HP: {}  DP {}  SP {}".format(hero_hp, hero_dp, hero_sp))

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
