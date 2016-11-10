class DrawSquares:
    def __init__(self, square):
##        self.squares = squares

        self.root_window = tkinter.Tk()

        self.canvas = tkinter.Canvas(master = self.root_window,
                                 width = 500, height = 500,
                                 background = 'blue')
        self.canvas.grid(row=0, column = 0, padx=0, pady = 0,
                     sticky = "nsew")

##        self.canvas.bind('<Configure>', self._resized)

        self.root_window.rowconfigure(0, weight = 1)
        self.root_window.columnconfigure(0, weight = 1)

        self.draw_squares_recursively(square)
        self.root_window.mainloop()


    def draw_squares_recursively(self, square):
        ##self.canvas.delete(tkinter.ALL)

        for value in square:
            if value < 0.05 or value > 100:
                return

        self.canvas.create_rectangle(square[0], square[1],
                                     square[2], square[3],
                                     outline = 'grey', width=2)
        square[2] += 20
        square[3] += 20
        self.draw_squares_recursively(square)
