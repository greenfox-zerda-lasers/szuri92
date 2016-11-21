from tkinter import *
from PIL import Image, ImageTk


class GameDisplay:

    def __init__(self):

        self.root = Tk()
        self.canvas_width = 800
        self.canvas_height =900
        self.resized_floor = self.resize("C:/Users/Gáspár/Desktop/floor.png", 65, 65)
        self.resized_wall = self.resize("C:/Users/Gáspár/Desktop/wall.png", 65, 65)
        self.canvas = Canvas(self.root, height = self.canvas_height, width = self.canvas_width, bg = 'silver')
        self.canvas.pack()

    def resize(self, img_path, width, height):
        image = Image.open(img_path)
        resized_image = image.resize((width, height), Image.ANTIALIAS)
        return ImageTk.PhotoImage(resized_image)


    def draw_map(self, game_field):
        for i in range(10):
            for j in range(11):
                if game_field[j][i] == 0:
                    self.canvas.create_image(i*65, j*65, anchor=NW, image = self.resized_floor)
                else:
                    self.canvas.create_image(i*65, j*65, anchor=NW, image = self.resized_wall)
