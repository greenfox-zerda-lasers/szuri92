# Create a method that decrypts the C:/Users/Gáspár/Desktop/Greenfox/szuri92/week-04/day-1/texts/duplicated_chars.txt

def decrypt(file_name):
    f = open(file_name)
    result = ''
    i= 0
    f = open(file_name)
    string = f.read()
    while i < len(string)-1:
        if string[i] == string[i+1]:
            result += string[i]
            i += 2
        else:
            result += string[i]
            i += 1
    return result

print(decrypt('C:/Users/Gáspár/Desktop/Greenfox/szuri92/week-04/day-1/texts/duplicated_chars.txt'))
