# write a function that takes a filename and returns the number of lines the
# file consists. It should return zero if the file not exists.

def line_number(filename):
    try:
        f = open('C:/Users/Gáspár/Desktop/Greenfox/szuri92/week-05/day-3/'+filename)
        lines = f.readlines()
        result = len(lines)
        f.close()
        return result
    except FileNotFoundError:
        return 0
    except TypeError:
        return 'Give a valid file name!'
    

#print(line_number(test_text.txt))
