# Anagram program

# https://www.geeksforgeeks.org/problems/anagram-1587115620/1

def anagram(str1,str2):
    if len(str1)!=len(str2):
        return False
    lt1 = sorted(str1)
    lt2 = sorted(str2)

    for i in range(len(lt1)):
        if lt1[i]!=lt2[i]:
            return False
        return True
    

str1 = input('Enter first string : ')
str2 = input('Enter ssecond string : ')

if anagram(str1,str2):
    print('Anagram Strings')
else:
    print('Not Anagram')
