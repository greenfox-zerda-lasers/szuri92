# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a 50 long horizontal line from that point.
# draw 3 lines with that function.

from tkinter import *

root = Tk()
canvas = Canvas(root, width='300', height='300')
canvas.pack()

def drawing(coord_x, coord_y):
    canvas.create_line(coord_x, coord_y, coord_x+50, coord_y)

for i in range(4):
    drawing(i*30, i*50)

root.mainloop()
