# 3. Given a non-negative int n,
# return the sum of its digits recursively (no loops).
# Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6),
# while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).


def digit_sum(number):
    if number >= 0 and number < 10:
        return number
    else:
        print(number)
        return number % 10 +digit_sum(number//10)


print(digit_sum(321312))
