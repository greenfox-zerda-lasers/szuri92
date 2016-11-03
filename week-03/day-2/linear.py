def linear_search(list, x):
    place = 0
    for i in range(len(list)):
        if list[i] == x:
            place = i
            break
        elif list[i] != x:
            place = -1

    return place

print(linear_search([4, 5, 6], 6))
print(linear_search([4, 5, 7], 6))
