# reproduce this: [https://github.com/greenfox-velox/velox-syllabus/blob/master/week-04/3-graphics/workshop/r1.png]
# divide the canvas into 4 parts and repeat the pattern.
# reproduce this: [https://github.com/greenfox-velox/velox-syllabus/blob/master/week-04/3-graphics/workshop/r2.png]
# can you make the colors change? make every line a different color.

from tkinter import *
import random

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def generate_color():
   color = '#{:02x}{:02x}{:02x}'.format(*map(lambda x: random.randint(0, 255), range(3)))
   return color

def draw_line(coord_x1, coord_y1, coord_x2, coord_y2, color):
    offset = 20
    canvas.create_line(coord_x1, coord_y1, coord_x2, coord_y2, fill = color )


def draw_eye():
    x = 300
    for j in range(0, x+1, x):
        for i in range(0, x, 20):
            if j == 0:
                color = 'blue'
            else:
                color = 'orange'
            draw_line(j, i, i, x-j, color)



def draw_star():
    x = 150
    color = 'red'
    #for j in range(0, x+1, x):
    for i in range(0, x, 10):
        draw_line(x, i, x-i, x, generate_color())
        draw_line(x, i, x+i, x, generate_color())
    #for j in range(2*x, x+1, -x):
    for i in range(2*x, x, -10):
        draw_line(x, i, x-(2*x-i), x, generate_color())
        draw_line(x, i, x+(2*x-i), x, generate_color())






#draw_eye()
draw_star()


root.mainloop()
