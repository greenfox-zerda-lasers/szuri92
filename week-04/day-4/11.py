from tkinter import *
import time

root = Tk()

size = 600
canvas = Canvas(root, width = size, height = size, bg = 'yellow')
canvas.pack()

def draw_rect(x, y, size):
    time.sleep(1)
    canvas.create_rectangle(x, y, x+size, y+size, width='2')
    canvas.update()
    if size > 20:
        draw_rect(x, y+size/3, size/3)
        draw_rect(x+(size*(2/3)), y+size/3, size/3)
        draw_rect(x+size/3, y, size/3)
        draw_rect(x+size/3, y+(size*(2/3)), size/3)




draw_rect(0, 0, 600)

root.mainloop()

"""
from tkinter import *

root = Tk()
size = 600
canvas1 = Canvas(root,width=size, height=size, bg="yellow")
canvas1.pack()

def nervtangle(x,y,size):
    canvas1.create_rectangle(x,y,x+size,y+size)
    if size > 20:
        nervtangle(x,y+size/3,size/3)
        nervtangle(x+(size*(2/3)),y+size/3,size/3)
        nervtangle(x+size/3,y,size/3)
        nervtangle(x+size/3,y+(size*(2/3)),size/3)

nervtangle(0,0,600)

root.mainloop()
"""
