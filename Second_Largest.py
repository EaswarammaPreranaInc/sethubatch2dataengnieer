'''
The program finds the second largest element in a list and prints all its indices.
The function largest(l) works in two steps:
First, it finds the maximum value max in the list.
Then, it finds the largest element that is not equal to max, which becomes max2 (the second largest).
After finding the second largest element, the program loops through the list to print all indices where this value occurs.
Indices are 0-based.
'''

def largest(l):
    max=float("-inf")
    for i in range(len(l)):
        if l[i]>max:
            max=l[i]
    max2=float("-inf")
    for i in range(len(l)):
        if l[i]!=max:
            if l[i]>max2:
                max2=l[i]
    return max2
l=eval(input("Enter the List:"))
x=largest(l)
for i in range(len(l)):
    if x == l[i]:
        print(f"Index of the Second Largest element {x} : {i} ", )


'''

Output:

Enter the List: [5, 12, 7, 12, 3]
Index of the Second Largest element 7 : 2

'''
