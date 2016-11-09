# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def drawing(coord_x, coord_y):
    length = 50
    canvas.create_rectangle(coord_x, coord_y, coord_x + length, coord_y + length)



drawing(30, 30)
drawing(100, 60)
drawing(140, 90)

root.mainloop()
