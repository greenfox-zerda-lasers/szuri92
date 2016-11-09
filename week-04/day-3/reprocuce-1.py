from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def draw_rect(size, number, color):
    offset = 10
    for i in range(0, number):
        canvas.create_rectangle(offset+(i*size), offset+(i*size), offset+((i+1)*size), offset+((i+1)*size), fill = color)





draw_rect(20, 10, 'purple')

root.mainloop()
