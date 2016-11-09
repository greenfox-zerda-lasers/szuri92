# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.
from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def draw_rect(size, color):
    canvas.create_rectangle(150-size/2, 150-size/2 ,150+size/2 ,150+size/2, fill=color)

rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'violet']


i = 6
while i >= 0:
    draw_rect((i+1)*40, rainbow[i])
    i -= 1


root.mainloop()
