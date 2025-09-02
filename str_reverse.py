'''
The program takes a list of strings as input from the user.
It uses the Bubble Sort technique with nested loops to compare adjacent strings.
Whenever a string is greater than the next, they are swapped.
After all iterations, the list is sorted in ascending (alphabetical) order and displayed.
'''

a=eval(input("Enter the list of String: "))
n=len(a)
for i in range(n):
    for j in range(n-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
print("Sorted List of Strings: ",a)



