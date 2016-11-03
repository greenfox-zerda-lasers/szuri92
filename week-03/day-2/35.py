# create a function that returns it's input factorial
def factorial(szam):
    i = szam
    factorial = 1
    while i > 0:
        factorial*= i
        i -= 1
    return factorial


print(factorial(7))
