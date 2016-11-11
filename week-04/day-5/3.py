from tkinter import *
import time
import math
root = Tk()

size = 400
height = math.sqrt(size **2 - (size/2)**2)
canvas = Canvas(root, width = 1000, height = 1000, bg='silver')
canvas.pack()

def draw_hexa(x, y, size):
    h = math.sqrt(3)/2
    time.sleep(0.1)
    canvas.create_polygon(x, y, x+size, y,
                          x+3/2*size, y+(size*h), x+size, y+2*size*h,
                          x, y+2*size*h, x-0.5*size, y+size*h,
                          fill='white', outline='black', width='1.5')
    canvas.update()
    if size > 4:
        draw_hexa(x, y, size/3)
        draw_hexa(x+2/3*size, y, size/3)
        draw_hexa(x+size, y+2/3*size*h, size/3)
        draw_hexa(x+2/3*size, y+4/3*size*h, size/3)
        draw_hexa(x, y+4/3*size*h, size/3)
        draw_hexa(x-1/3*size, y+2/3*h*size, size/3)

draw_hexa(250, 30, 400)
root.mainloop()
