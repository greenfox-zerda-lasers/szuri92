# create a 300x300 canvas.
# create a function that takes 1 parameter:
# a list of [x, y] points
# and connects them with green lines.
# connect these to get a box: [[10, 10], [290,  10], [290, 290], [10, 290]]
# connect these: [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70],
# [120, 100], [85, 130], [50, 100]]

from tkinter import *
import random

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def connect_points(list):
    for i in range(len(list)-1):
        canvas.create_line(list[i][0], list[i][1], list[i+1][0], list[i+1][1], fill = 'green')

connect_points([[50, 100], [70, 70], [80, 90], [90, 90], [100, 70], [120, 100], [85, 130], [50, 100]])

root.mainloop()
