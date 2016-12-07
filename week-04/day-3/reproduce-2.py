from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def draw_rect(size, number, color):
    for i in range(0, number):
        canvas.create_rectangle(size*(i+1), size*(i+1), 2*size*(i+1), 2*size*(i+1), fill= color)

draw_rect(20, 5, '#1a5e35')

root.mainloop()
