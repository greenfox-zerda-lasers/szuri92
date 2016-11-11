from tkinter import *
import time
import math
root = Tk()

size = 400
height = math.sqrt(size **2 - (size/2)**2)
canvas = Canvas(root, width = 1000, height = 1000, bg = 'silver')
canvas.pack()

def draw_poly(x, y, size, height):
    height = math.sqrt(size **2 - (size/2)**2)
    time.sleep(0.0001)
    canvas.create_polygon(x, y, x+size, y, x+3/2*size,
                          y+height, x+size, y+2*height,
                          x, y+2*height, x-0.5*size, y+height,
                          fill='white', outline='black', width='1.5')
    canvas.update()
    if size > 2:
        draw_poly(x, y, size/3, height/3)
        draw_poly(x+2/3*size, y, size/3, height/3)
        draw_poly(x+size, y+2/3*height, size/3, height/3)
        draw_poly(x+2/3*size, y+4/3*height, size/3, height/3)
        draw_poly(x, y+4/3*height, size/3, height/3)
        draw_poly(x-1/3*size, y+2/3*height, size/3, height/3)

draw_poly(250, 0, size, height)
root.mainloop()
