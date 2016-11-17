# Create an "elevator" class
# The class should track the following things:
#  - elevator position
#  - elevator direction
#  - people in the elevator
#  - add people
#  - remove people
#
# Please remeber that negative amount of people would be troubling

class Elevator:

    def __init__(self):
        self.levels = 12
        self.position = 0
        self.people_count = 0

    def add_people(self):
        self.people_count += 1
        return self.people_count

    def remove_people(self):
        if self.people_count >=1:
            self.people_count -= 1
        return self.people_count

    def move_up(self):
        if self.position <= self.levels:
            self.position += 1
        return self.position

    def move_down(self):
        if self.position >= 1:
            self.position -= 1
        return self.position
