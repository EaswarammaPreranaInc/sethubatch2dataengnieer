'''
The program takes input in the format "string1 and string2", then splits it into a list containing the two strings.
The function anagram(l) compares the two strings: if their lengths are not equal, it immediately returns False.
If lengths are equal, it checks whether every character in the first string also exists in the second string.
Finally, the function returns True if the condition is satisfied for all characters, otherwise False, and the result is printed.
'''

def anagram(l):
    string1=l[0]
    string2=l[1]
    if len(string1) != len(string2):
        return False
    for x in string1:
        if x not in string2:
            return False
    return True
s=input("Enter 2 string (string1 and string2) : ")
l=s.split(' and ')
x=anagram(l)
print(x)

'''
Output:

Enter 2 string (string1 and string2) : listen and silent
True

Enter 2 string (string1 and string2) : hello and world
False

'''