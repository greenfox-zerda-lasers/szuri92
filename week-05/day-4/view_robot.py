# Create a class that displays the robot's messages, position, etc
class Display:

    def messeges(self, messege):
        print('messege')


    def show_position(selef, position_x, position_y):
        print(' ---  ---  ---')
        for i in range(1, 4):
            if i == position_y:
                if position_x == 1:
                    print('| X ||   ||   |')
                elif position_x == 2:
                    print('|   || X ||   |')
                elif position_x == 3:
                    print('|   ||   || X |')
            else:
                print('|   ||   ||   |')
            print(' ---  ---  ---')
