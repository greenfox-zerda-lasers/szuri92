# Create a robot controller class. This is the mind of the robot.
# It should take an user input by listening to user input:
# Default functionaly when the robot is switched on:
#  - Automatically names the robot
#  - Sets it's position
#
# List of commands:
#  1) memorize: add a new memory entry to the memory
#  2) recall: displays a list memories
#  3) move: increments the robot's position by one coordinate the N-S-E-W directions
#     - it also displays the new position
#  4) speak: it can introduce itself by saying its name and mood and last memory
#
# Create the class with MVC pattern in mind. It should get and store data in the model object
# and it should pass the data to the view objects
import model_robot
import view_robot

class Controller:

    def __init__(self):
        self.display = view_robot.Display()
        self.robot = model_robot.Robot()
        self.run = False
        self.start()

    def move(self, action):
        if action.upper() == 'N':
            self.robot.move_up()
        elif action.upper() == 'S':
            self.robot.move_down()
        elif action.upper() == 'W':
            self.robot.move_right()
        elif action.upper() == 'E':
            self.robot.move_left()
        else:
            print('Invalid commnad')

    def loop(self):
        while self.run:
            action = input('Waiting for your instructions human!')
            self.move(action)
            self.display.show_position(self.robot.position_x, self.robot.position_y)

    def start(self):
        self.run = True
        self.loop()

belavagyok = Controller()
