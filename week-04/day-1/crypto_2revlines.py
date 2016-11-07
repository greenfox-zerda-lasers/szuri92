# Create a method that decrypts texts/reversed_zen_lines.txt
import basics
def decrypt(file_name):
    f = open(file_name)
    result = ''
    linelist = f.readlines()
    for line in linelist:
        charnum = len(line)
        while charnum > 0:
            result += line[charnum-1]
            charnum -= 1
    return result

print(decrypt('C:/Users/Gáspár/Desktop/Greenfox/szuri92/week-04/day-1/texts/reversed_zen_lines.txt'))
