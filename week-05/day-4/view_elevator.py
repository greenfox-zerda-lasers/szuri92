# Create a class the displays the Elevator art and navigation (list of commands)

class Display:

    def commands(self):
        print('commands: - add people:      add')
        print('          - remove people:   remove')
        print('          - elevator up:     up')
        print('          - elevator down:   down')
        print('          - exit :           exit')

    def draw(self, level, position, people):
        print("___________________________________\n`._______________________________.'")
        for i in range(level, -1, -1):
            if position > level:
                position = level
            elif position  < 0:
                position = 0
            if i == position and i >= 0 and position != 0:
                if people > 0:
                    print('   || || [_X_] || ||       || ||')
                else:
                    print('   || || [_ _] || ||       || ||')
            else:
                if i == 0 and position == 0 and people > 0:
                    print('  _||_||_[_X_]_||_||_______||_||_')
                elif i == 0 and position == 0 and people == 0:
                    print('  _||_||_[_ _]_||_||_______||_||_')
                elif i == 0 and  i!= position:
                    print('  _||_||______ ||_||_______||_||_')
                else:
                    print('   || ||       || ||       || ||')
        print(".'_______________________________`.")
