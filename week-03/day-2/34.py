numbers = [4, 5, 6, 7, 8, 9, 10, 11]
# write your own sum function
def sum(list_numbers):
    total = 0
    for i in range(len(list_numbers)):
        total += list_numbers[i]
    print(total)

sum(numbers)
