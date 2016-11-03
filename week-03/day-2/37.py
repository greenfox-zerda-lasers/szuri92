numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# write a function that filters the odd numbers
# from a list and returns a new list consisting
# only the evens
def filter(a):
    n = []
    x = 0
    while x < len(a):
        if a[x] % 2 == 0:
            n.append(a[x])
        x +=1
    return(n)

filter(numbers)

print(filter(numbers))
