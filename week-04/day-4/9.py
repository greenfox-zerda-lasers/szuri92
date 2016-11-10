# 9. Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".

def star_between(string):
    if len(string) <=1 :
        return string
    else:
        return string[0] + '*' + star_between(string[1:])





a = 'xanax'
print(star_between('xanaxdsadB'))
print(star_between(a))
print(star_between('abaasbabsbabsbasbabsdsa!+"!"+'))
