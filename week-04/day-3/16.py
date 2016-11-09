# create a 300x300 canvas.
# make it look like a nigth sky:
# - The background should be black
# - The stars can be small squares
# - The stars should have random positions on the canvas
# - The stars should have random color (some shade of grey)


from tkinter import *
from random import *
import time
root = Tk()

def generate_color():
   color = '#{:02x}{:02x}{:02x}'.format(*map(lambda x: random.randint(0, 255), range(3)))
   return color

canvas = Canvas(root, width='300', height='300', bg='black')
canvas.pack()



for i in range(0, 150):
    x = randint(0, 300)
    y = randint(0, 300)
    color = '#'
    color_number = randint(0, 9)
    color += str(color_number) * 3
    canvas.create_rectangle(x, y, x+3, y+3, fill=color)
    time.sleep(0.05)
    canvas.update()

root.mainloop()
