# 5. We have a number of bunnies and each bunny has two big floppy ears.
# We want to compute the total number of ears across all the bunnies
# recursively (without loops or multiplication).

def floppy_ear_counter(bunnies):
    if bunnies == 1:
        return 2
    else:
        return 2 + floppy_ear_counter(bunnies-1)




print(floppy_ear_counter(30))
