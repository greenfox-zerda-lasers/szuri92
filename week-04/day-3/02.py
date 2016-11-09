# create a 300x300 canvas.
# draw a box that has different colored lines on each edge.

from tkinter import *

root = Tk()

canvas = Canvas(root, width = '300', height ='300')
canvas.pack()

line_1 = canvas.create_line(20, 20, 200, 20, fill='red')
line_1 = canvas.create_line(200, 20, 200, 200, fill='green')
line_1 = canvas.create_line(200, 200, 20, 200, fill='blue')
line_1 = canvas.create_line(20, 200, 20, 20, fill='orange')


root.mainloop()
