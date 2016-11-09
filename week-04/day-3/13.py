# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def draw_line(coord_x, coord_y):
    canvas.create_line(coord_x, coord_y, 150, 150, fill = 'orange' )



for i in range(0, 300, 20):
    for j in range(0, 301, 300):
        draw_line(j, i)


for a in range(0, 301, 300):
    for b in range(0, 300, 20):
        draw_line(b, a)


root.mainloop()
