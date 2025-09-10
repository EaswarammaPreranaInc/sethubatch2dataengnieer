'''
The program finds the largest element in a list and prints all its indices.
The function largest(l) loops through the list and keeps track of the maximum value.
After finding the largest element, the main code loops through the list to find all indices where the element occurs.
It prints the index (or indices) along with the largest element.
'''

def largest(l):
    max=float("-inf")
    for i in range(len(l)):
        if l[i]>max:
            max=l[i]
    return max
l=eval(input("Enter the List:"))
x=largest(l)
for i in range(len(l)):
    if x == l[i]:
        print(f"Index of the Largest element {x} : {i}")


'''

Output:

Enter the List: [5, 12, 7, 12, 3]
Index of the Largest element 12 : 1
Index of the Largest element 12 : 3

Enter the List: [10, 4, 8, 15, 2]
Index of the Largest element 15 : 3

'''
