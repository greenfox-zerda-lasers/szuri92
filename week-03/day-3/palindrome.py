def reverser(list1):
    revers = ''
    i = 0
    while i < len(list1):
        revers += list1[(len(list1)-1)-i]
        i += 1
    return revers


def make_palindrome(list1):
    revers = reverser(list1)
    palindrome = list1 + revers
    return palindrome

print(reverser('pear'))
print(make_palindrome('pear'))
