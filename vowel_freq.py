'''
Question:
Write a program to count the frequency of vowels (A, E, I, O, U) in a given string.
Ignore spaces and treat letters case-insensitively. Display the vowels and their counts alphabetically.
'''

def freq(s):
    d = {}
    for y in s.upper():
        if y == ' ':
            continue
        elif y in 'AEIOU':
            d[y] = d.get(y, 0) + 1
    return d

s = input("Enter a String : ")
x = freq(s)
for k, v in sorted(x.items()):
    print(f'{k}...{v}', end=",")

'''
Output 1:
Input: Rama Rao
A...3,O...1,

Output 2:
Input: Hello World
E...1,O...2,
'''
