# Create a function that prints a diamond like this:
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
#   *********
#    *******
#     *****
#      ***
#       *
#
# It should take a number as parameter that describes how many lines the diamond has

def diamond(line):
    if line % 2 == 0:
        print('Give an odd number')
    else:
        for i in range(0, (line+1)//2):
            print(((line//2)-i)*' '+(i*2+1)*'*')
        k = (line-3)//2
        while k > -1:
            print(((line//2)-k)*' '+(k*2+1)*'*')
            k -= 1

diamond(43)
