#bubble_sort([3,9,4,5,2,1])
# expected output: [1,2,3,4,5,9]
def bubble_sorter(list):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                sorted = False
                list[i], list [i+1] = list[i+1], list[i]
    return list

bad = [3, 9, 4, 5, 2, 1, 7, 22, 44, 2, 2]
bubble_sorter(bad)
print(bad)
