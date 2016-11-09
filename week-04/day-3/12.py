# create a 300x300 canvas.
# fill it with a checkerboard pattern.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()
size = 300/8
for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0:
            color = 'white'
        else:
            color = 'black'
        canvas.create_rectangle(i * size, j * size, (1+i)*size, (j+1)*size, fill = color)
root.mainloop()
