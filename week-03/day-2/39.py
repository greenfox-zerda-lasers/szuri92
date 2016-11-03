names = ['Zakarias', 'Hans', 'Otto', 'Ole', 'a']
# create a function that returns the shortest string
# from a list
def shortest(a):
    n = len(a[0])

    for x in range(len(a)):
        if len(a[x]) < n:
            n = len(a[x])
            short = a[x]
    return short

print(shortest(names))
