from tkinter import *
import time
from random import *
import math
root = Tk()
size = 400
height = math.sqrt(size **2 - (size/2)**2)
canvas = Canvas(root, width = 1000, height = 1000, bg='pink')
canvas.pack()

def draw_poly(x, y, size, height):
    height = math.sqrt(size **2 - (size/2)**2)
    time.sleep(0.001)
    color = '#'
    color_number = randint(0, 9)
    color_number2 =  randint(0, 9)
    color_number3 =  randint(0, 9)
    color += str(color_number) + str(color_number2) + str(color_number3)
    canvas.create_polygon(x, y, x+size, y, x+3/2*size, y+height, x+size, y+2*height, x, y+2*height, x-0.5*size, y+height, fill=color, outline='black', width='1.5')
    canvas.update()
    if size > 1:
        draw_poly(x, y, size/2, height/2)
        draw_poly(x+3/4*size, y+1/2*height, size/2, height/2)
        draw_poly(x, y+height, size/2, height/2)

draw_poly(250, 10, size, height)
root.mainloop()
