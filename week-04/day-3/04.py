# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def draw_line(coord_x, coord_y):
    canvas.create_line(coord_x, coord_y, 150, 150, fill='blue')



i = 0
while i < 4:
    draw_line(0, 20*i)
    i += 1    

root.mainloop()
