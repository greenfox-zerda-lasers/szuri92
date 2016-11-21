import TKWander_view
import TKWander_map

class Control:
    def __init__(self):
        self.view = TKWander_view.GameDisplay()
        self.map = TKWander_map.GameMap()

    def draw_game_map(self):
        self.view.draw_map(self.map.game_field_element)




valami = Control()
valami.draw_game_map()
valami.view.root.mainloop()
