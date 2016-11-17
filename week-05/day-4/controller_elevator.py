# Create an elevator controller class
# It should take an user input by listening to user input
# List of commands:
#
#  - Move elevator up
#  - Move elevator down
#  - Add people
#  - Remove people
#
#  Features to implement:
#   - Always draw the state of the elevator as depicted in "art.txt"
#   - [ x ] is the elevator. X means it has at least 1 person inside
#   - Moving floors should take time
#   - don't move beyond limits
#
# Create the class with MVC pattern in mind. It should get and store data in the model object
# and it should pass the data to the view objects
import model_elevator
import view_elevator
import os
class ElevatorController:
    def __init__(self):
        self.model = model_elevator.Elevator()
        self.display = view_elevator.Display()
        self.runnig = False
        self.start_elevator()


    def start_elevator(self):
        self.runnig = True
        self.display.commands()
        self.display.draw(self.model.levels, 0, 0)
        self.elev_loop()

    def elev_loop(self):
        while self.runnig:
            action = input('what you wanna do?\n')
            os.system('cls' if os.name=='nt' else 'clear')
            if action.lower() == 'add':
                self.model.add_people()
            elif action.lower() == 'remove':
                self.model.remove_people()
            elif action.lower() == 'up':
                self.model.move_up()
            elif action.lower() == 'down':
                self.model.move_down()
            elif action.lower() == 'exit':
                self.runnig = False
            else:
                print('Command not found')
            self.display.draw(self.model.levels, self.model.position, self.model.people_count)
            print('Peoples: {0}'.format(self.model.people_count))
lets_play = ElevatorController()
