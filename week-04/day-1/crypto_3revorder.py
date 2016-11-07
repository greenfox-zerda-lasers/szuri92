# Create a method that decrypts texts/reversed_zen_order.txt
import basics
def decrypt(file_name):
    f = open(file_name)
    make_list = f.readlines()
    reverse_list = []
    for i in range(len(make_list)):
        reverse_list.append(make_list[len(make_list)-1-i])
    result = basics.sentence(reverse_list)
    return result



print(decrypt('C:/Users/Gáspár/Desktop/Greenfox/szuri92/week-04/day-1/texts/reversed_zen_order.txt'))
