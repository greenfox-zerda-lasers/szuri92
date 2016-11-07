# Create a method that decrypts texts/encoded_zen_lines.txt
import basics
def decrypt(file_name):
    f = open(file_name)
    list_1 = f.read()
    list_code = basics.char_codes(list_1)
    for i in range(len(list_code)):
        if list_code[i] != 10 and list_code[i] != 32:
            list_code[i] = list_code[i]-1
    result = basics.string(list_code)

    return result


print(decrypt('C:/Users/Gáspár/Desktop/Greenfox/szuri92/week-04/day-1/texts/encoded_zen_lines.txt'))
