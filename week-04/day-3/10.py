# create a 300x300 canvas.
# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# create a loop that draws 20 squares with that function.

from tkinter import *

root = Tk()

def draw_rect(size):
    canvas.create_rectangle(150-size/2, 150-size/2 ,150+size/2 ,150+size/2)

canvas = Canvas(root, width='300', height='300')
canvas.pack()


for i in range(20):
    draw_rect(10*(i+1))


root.mainloop()
