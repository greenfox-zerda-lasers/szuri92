# 4. Given base and n that are both 1 or more, compute recursively (no loops)
# the value of base to the n power, so powerN(3, 2) is 9 (3 squared).

def power_counter(base, power):
    if base == 1 or power == 1:
        return base
    else:
        return base * power_counter(base, power-1)

print(power_counter(5,3))
