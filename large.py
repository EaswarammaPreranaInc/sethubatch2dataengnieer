'''
Question:
Write a program to find the next bigger number that can be formed by rearranging
the digits of a given number. If no bigger number is possible, display an appropriate message.
'''

def bigger_number(n):
    digits = list(str(n))
    i = len(digits) - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1
    if i == -1:
        return "No bigger number possible"
    j = len(digits) - 1
    while digits[j] <= digits[i]:
        j -= 1
    digits[i], digits[j] = digits[j], digits[i]
    digits[i + 1:] = reversed(digits[i + 1:])
    return int(''.join(digits))

num = int(input("Enter a number: "))
print(bigger_number(num))

'''
Output 1:
Input: 12
21

Output 2:
Input: 445
454

Output 3:
Input: 987
No bigger number possible
'''
