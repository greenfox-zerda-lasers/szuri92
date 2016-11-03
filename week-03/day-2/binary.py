def bubble_sorter(list):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                sorted = False
                list[i], list [i+1] = list[i+1], list[i]
    return list

def binary_search(list, x):
    bubble_sorter(list)
    min = 0
    max = len(list)
    while min < max:
        y = min + (max - min) // 2
        target = list[y]
        if x == target:
            return y
        elif x > target:
            if min == y:
                break
            min = y
        elif x < target:
            max = y

ab = [2, 1, 3, 5, 4, 7, 6]

print(binary_search(ab, 7))
print(ab)
