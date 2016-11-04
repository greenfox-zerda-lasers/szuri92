# create a function that takes a list and returns a new list that is reversed
def reverser(list1):
    revers = []
    i = 0
    while i < len(list1):
        revers.append(list1[(len(list1)-1)-i])
        i += 1
    return revers


numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print(reverser(numbers))
