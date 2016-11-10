# 12. write a recursive function that can add numbers in
# [1, 2, [3, 4], 1, [1, [2, 4]]]

def list_add(lista):
    if len(lista) == 0:
        return 0
    elif type(lista[0]) == list:
        return  list_add(lista[0]) + list_add(lista[1:])
    else:
        return  lista[0] + list_add(lista[1:])


print(list_add([1, 2, [3, 4], 1, [1, [2, 4]]]))
