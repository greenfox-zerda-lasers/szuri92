#Given a string, compute recursively a new string where all the 'x' chars have been removed.

def del_x(string):
    if not string:
        return string
    elif string[0] == 'x':
         return '' + del_x(string[1:])
    else:
        return string[0] + del_x(string[1:])




a = 'xanax'
print(del_x('xanaxdsadB'))
print(del_x(a))
