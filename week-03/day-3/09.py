# Create a function that prints a triangle like this:
#   *
#   **
#   ***
#   ****
#   *****
#   ******
# It should take a number as parameter that describes how many lines the triangle has

def triangle(line):
    for i in range(0, line+1):
        print(i*'*')

triangle(23)
