#create a 300x300 canvas.
# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300', bg='orange')
canvas.pack()

### draw color rect
##def draw_rect(size, color):
##canvas.create_rectangle(150-size/2, 150-size/2 ,150+size/2 ,150+size/2, fill=color)

def draw_rect(size):
    canvas.create_rectangle(150-size/2, 150-size/2 ,150+size/2 ,150+size/2)


##draw_rect(200, 'blue')
##draw_rect(150, 'red')
##draw_rect(100, 'green')

draw_rect(200)
draw_rect(150)
draw_rect(100)



root.mainloop()
