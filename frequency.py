'''
Question:
Write a program to count the frequency of each character (ignoring spaces) in a given string.
The output should display each character in uppercase along with its count, sorted alphabetically.
'''

def freq(s):
    d={}
    for y in s.upper():
        if y == ' ':
            continue
        else:
            d[y]=d.get(y,0)+1
    return d

s = input("Enter a String : ")
x = freq(s)
for k, v in sorted(x.items()):
    print(f'{k}...{v}', end=",")

'''
Output 1:
Input: Rama Rao
A...3,M...1,O...1,R...2,

Output 2:
Input: Hello World
D...1,E...1,H...1,L...3,O...2,R...1,W...1,
'''
