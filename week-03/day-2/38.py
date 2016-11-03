numbers = [7, 5, 8, -1, 2, -5]
# Write a function that returns the minimal element
# in a list (your own min function)
def function(a):
    n = a[0]
    for x in range(len(a)):
        if a[x] < n:
            n=a[x]
    return n

print(function(numbers))
