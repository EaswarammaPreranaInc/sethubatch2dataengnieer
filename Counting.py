'''
The program analyzes a string input and calculates the number of characters, vowels, consonants, spaces, tabs, and words.
It defines a function total(s) which:
Counts vowels (AEIOU), consonants, spaces (" "), and tabs ("\t").
Calculates the number of words using len(s.split()).
Returns all counts in a list L.
The main code takes input from the user, calls total(s), and stores results in x.
The results are printed in a readable format using f-strings.
'''

def total(s):
    L=[len(s)]
    vowel=0
    consonant=0
    space=0
    tab=0
    for x in s:
        if x.upper() in 'AEIOU':
            vowel+=1
        elif x == " ":
            space+=1
        elif x == "\t":
            tab+=1
        else:
            consonant+=1
    words=len(s.split())
    L.append(vowel)
    L.append(consonant)
    L.append(space)
    L.append(tab)
    L.append(words)
    return L
s=input("Enter a String:")
x=total(s)
print(f"Number of characters: {x[0]}")
print(f"Number of vowles: {x[1]}")
print(f"Number of consonants: {x[2]}")
print(f"Number of spaces: {x[3]}")
print(f"Number of tabs: {x[4]}")
print(f"Number of words: {x[5]}")


'''
Output:

Enter a String: Python  Programming is fun
Number of characters: 26
Number of vowels: 6
Number of consonants: 17
Number of spaces: 3
Number of tabs: 1
Number of words: 5

'''