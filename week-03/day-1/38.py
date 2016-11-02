# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number
# and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".
i=1

while i < 100:
    if i % 5 == 0 and i % 3 !=0:
        print("Buzz")
    elif i % 3 == 0 and i % 5 != 0:
        print("Fizz")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    else:
        print(i)
    i+=1
