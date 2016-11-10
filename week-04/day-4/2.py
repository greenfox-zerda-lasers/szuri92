# 2. write a recursive function
# that takes one parameter: n
# and adds numbers from 1 to n

def summ(number):
    if number == 1:
        return 1
    else:
        print(number)
        return number+summ(number-1)



print(summ(5))
