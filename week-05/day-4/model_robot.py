# Create a "robot" class that manifests a robots's memory
# make sure that you implement the following things:
#  - the robot can remember new things (simple string)
#  - the robot can recall things (as strings)
#  - the robot has a name
#  - the robot has list of possible mood
#  - the robot has a position property
#  - the robot can move by calling a method that sets its position
class Robot:

    def __init__(self):
        self.memory = []
        self.name = 'Mzperx'
        self.mood = ['Happy', 'Sad', 'Bored', 'Angry', 'Surprised', 'Excited']
        self.position_x = 1
        self.position_y = 1




    def add_string(self, thing):
        thing = str(thing)
        self.memory.append(thing)
        return self.memory

    def recall_string(self, thing):
        print(thing)

    def move_right(self):
        if self.position_x in (1, 2):
            self.position_x += 1

    def move_left(self):
        if self.position_x in (2, 3):
            self.position_x -= 1

    def move_up(self):
        if self.position_y in (2, 3):
            self.position_y -= 1

    def move_down(self):
        if self.position_x in (1, 2):
            self.position_y += 1
