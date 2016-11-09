# create a 300x300 canvas.
# fill it with four different size and color rectangles.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

canvas.create_rectangle(145, 145, 200, 200, fill='green')
canvas.create_rectangle(20, 30, 40, 50, fill='purple')
canvas.create_rectangle(210, 190, 250, 230, fill='orange')
canvas.create_rectangle(270, 270, 300, 300, fill='lightblue')

root.mainloop()
