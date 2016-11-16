# create a function that takes a number and divides ten with it and prints the result
# it should print "fail" if it is divided by 0


def divide_ten(divider):
    try:
        return 10/divider
    except ZeroDivisionError:
        return 'fail'



#print(divide_ten(0))
