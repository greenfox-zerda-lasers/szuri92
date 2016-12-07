# Adds a and b, returns as result
def add(a, b):
    return a + b

# Returns the highest value from the three given params
def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

# Returns the median value of a list given as param
def median(pool):
    pool.sort()
    (int(len(pool)-1))
    if len(pool) % 2 == 1:
        return pool[int((len(pool) - 1) / 2)]
    else:
        return (pool[int(len(pool) / 2)] +  pool[int((len(pool) - 2) / 2)]) / 2
# Returns true if the param is a vovel
def is_vovel(char):
    if len(char) > 1:
        raise TypeError
    else:
        return char.lower() in 'aeiouéáőűöüóí'

# Create a method that translates hungarian into the teve language
def translate(hungarian):
    teve = hungarian
    result = ''
    if isinstance(hungarian, str):
        for char in teve:
            if is_vovel(char):
                result += (char+'v'+char)
            else:
                result += char
    else:
        raise TypeError('Give a string')        #teve = (char+'v'+char).join(teve.split(char))
    return result
