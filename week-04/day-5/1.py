from tkinter import *
import time
import math

root = Tk()
size = 600
height = math.sqrt(size **2 - (size/2)**2)
canvas = Canvas(root, width = 800, height = 800, bg='silver')
canvas.pack()

def draw_rect(x, y, size):
    h = math.sqrt(3)/2
    time.sleep(0.00001)
    canvas.create_polygon(x, y, x+size, y, x+size/2, y+size*h, fill='white', outline='black')
    canvas.update()
    if size > 5:
        draw_rect(x, y, size/2)
        draw_rect(x+size/2, y, size/2)
        draw_rect(x+size/4, y+(size*h)/2, size/2)

draw_rect(100, 20, 600)
root.mainloop()
