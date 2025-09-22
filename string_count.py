'''
Question:
Write a program to count the number of strings in a list where the first and last characters are the same.
The program should take words separated by spaces as input.
'''

def counts(lst):
    count = 0
    for x in lst:
        if len(x) > 0 and x[0] == x[-1]:
            count += 1
    return count

s = input("Enter words separated by space: ").split()
print(counts(s))

'''
Output 1:
Input: level deed noon apple
3

Output 2:
Input: hello world anna civic
2
'''

