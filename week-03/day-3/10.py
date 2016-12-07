# Create a function that prints a triangle like this:
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
#
# It should take a number as parameter that describes how many lines the triangle has


def tree(line):
    for i in range(0, line+1):
        print((line-i)*' '+(i*2+1)*'*')

tree(12)
