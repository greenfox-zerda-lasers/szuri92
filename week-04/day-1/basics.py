# 1. Create a method that reads all contents of a file when its name given as param
def readfile(file_name):
    f = open(file_name)
    result = f.read()
    f.close()
    return result

#print(readfile('C:/Users/Gáspár/Desktop/Greenfox/szuri92/week-04/day-1/texts/zen_of_python.txt'))

# 2. Create a method that gets a file_name and a number as param and reads the numberth line of the file
def readline(file_name, number):
    f = open(file_name)
    result = f.readlines()[number-1].rstrip()
    return result

#print(readline('C:/Users/Gáspár/Desktop/Greenfox/szuri92/week-04/day-1/texts/zen_of_python.txt', 2))

# 3. Create a method that gets a long sentence as param and gives back the contained words in a list
def words(sentence):
    result = []
    result2 = sentence.split()
    for word in result2:
        cleanword = ""
        for char in word:
            if char in '!.?':
                char = ""
            cleanword += char
        result.append(cleanword)
    #result = sentence.split()
    return result



# 4. Create a method that gets a list of words and creates a sentence with the words separated by spaces
def sentence(words):
    result = ''
    for i in range(len(words)):
        result += words[i]
    return result

#print(sentence(['Ma', 'van', 'a', 'negyedik', 'het', 'elso', 'napja']))

# 5. Create a method that gets a string and gives back the character codes in a list
def char_codes(string):
    result = []
    for i in range(len(string)):
        result.append(ord(string[i]))
    return result

#print(char_codes("Hello"))


# 6. Create a method that gets a list of integers and gives back a string which characters are created from the numbers used as character codes
def string(char_codes):
    result = ''
    for i in range(len(char_codes)):
        result  += (chr(char_codes[i]))
    return result

#print(string([72, 101, 108, 108, 111]))
