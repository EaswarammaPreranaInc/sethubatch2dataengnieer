'''
Question:
Write a program to find the first word that occurs the maximum number of times in a given string.
Words are separated by spaces and/or periods.
'''

def maxi(s):
    a = []
    d = {}
    new = s.split(".")
    for x in new:
        a.extend(x.split())
    for y in a:
        d[y] = d.get(y, 0) + 1
    m = max(d.values())
    for k, v in d.items():
        if m == d[k]:
            m = k
            break
    return m
        
s = input("Enter a String : ")
print(maxi(s))

'''
Output 1:
Input: Rama Rao Rama
Rama

Output 2:
Input: hello world. hello everyone. hello you
hello
'''
