# create a function that takes a list and returns a new list with all the elements doubled

def doubled(list1):
    for i in range(len(list1)):
        list1[i] *= 2
    return list1

list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(doubled(list2))
