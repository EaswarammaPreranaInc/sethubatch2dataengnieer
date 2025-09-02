'''
The program first takes a string input from the user and converts it into a list of characters using the list() function. This allows each character in the string to be handled individually for sorting.
It calculates the length of the list and applies the Bubble Sort algorithm using two nested loops. This ensures that each character is compared with the next character in sequence.
During each comparison, if one character is greater (in ASCII/alphabetical order) than the next, they are swapped. This process continues until all characters are arranged in the correct order.
After sorting, the list of characters is joined back into a single string using ''.join(a), and the final sorted string is displayed as output.
'''

str1=input("Enter the list of String: ")
a=list(str1)
n=len(a)
for i in range(n):
    for j in range(n-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
print("Sorted List of Strings: ",''.join(a))



