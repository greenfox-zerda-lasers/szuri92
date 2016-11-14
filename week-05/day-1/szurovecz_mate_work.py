from collections import Counter

# return True if string1 and string2 are anagramms
def anagramm(string1, string2):
    new_sorted1 = ''
    new_sorted2= ''
    string1 = list(string1.lower())
    string2 = list(string2.lower())
    string1.sort()
    string2.sort()
    for i in range(len(string1)):
        if string1[i] != ' ':
            new_sorted1 += string1[i]
    for i in range(len(string2)):
        if string2[i] != ' ':
            new_sorted2 += string2[i]
    return new_sorted1 == new_sorted2

#return a dictionary with letters in string, and numbers as occurences
def count_letters(string):
    sorted_list= ''
    string1 = string.lower()
    for i in range(len(string1)):
        if ord(string1[i]) in range (97, 123) or ord(string1[i]) in range (223, 256):
            sorted_list += string1[i]
    sorted_list = Counter(sorted_list)
    if sorted_list == '':
        return {}
    else:
        return sorted_list


print(count_letters('ßélá!'))
