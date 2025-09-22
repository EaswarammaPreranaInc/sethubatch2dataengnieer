'''
Question:
Write a program to find the first character that occurs the maximum number of times in a given string.
Ignore spaces and treat letters case-insensitively.
'''

def first_max(s):
    s = s.replace(" ", "").upper()  
    count = {}
    
    for ch in s:
        count[ch] = count.get(ch, 0) + 1

    max_count = max(count.values())
    
    for ch in s:
        if count[ch] == max_count:
            return ch

input_str = input("Enter a string: ")
print(first_max(input_str))

'''
Output 1:
Input: Rama Rao
A

Output 2:
Input: Hello World
L
'''
