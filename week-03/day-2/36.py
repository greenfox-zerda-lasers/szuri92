numbers = [3, 4, 5, 6, 7, 10, 32, 65, 223, 1]
# write a function that reverses a list
def reverse(a):
    n = []
    x=0
    while x <len(a):
        n.append(a[(len(a)-1)-x])
        x +=1
    return(n)

print(reverse(numbers))
