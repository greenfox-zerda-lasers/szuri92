# 7. Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.


def x_to_y_changer(string):
    if not string:
        return string
    elif string[0] == 'x':
         return 'y'+ x_to_y_changer(string[1:])
    else:
        return string[0] + x_to_y_changer(string[1:])


a = 'xanax'
print(x_to_y_changer('xaver xavier'))
print(x_to_y_changer(a))
