'''
If we want to add a single element to an existing set, we can use the .add() operation.
It adds the element to the set and returns 'None'.

Input Format:
The first line contains an integer 'a' , the total number of country stamps.
The next 'a' lines contains the name of the country where the stamp is from.

Output Format:
Output the total number of distinct country stamps on a single line.
'''


a  = int(input("Enter a number : "))
b = set()
for i in range(a):
    c = input("Enter a string : ")
    b.add(c)
d = len(b)
print(d)
