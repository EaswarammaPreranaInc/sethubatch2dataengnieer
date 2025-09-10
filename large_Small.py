'''
The program finds the largest and smallest numbers from the command-line arguments.
It reads numbers from argv[1:] and stores them in list a.
It uses a simple nested loop to sort the list in descending order:
Compares each element with previous elements and swaps if necessary.
After sorting, a[0] is the largest and a[-1] is the smallest number, which are printed.
'''

from sys import argv
a = argv[1:]
if not a: 
    print("Please provide numbers as arguments!")
    exit()
for i in range(len(a)):
    for j in range(i+1):
        if int(a[i]) > int(a[j]):
            a[i], a[j] = a[j], a[i]
print(f"Largest element in the given list : {a[0]}")
print(f"Smallest element in the given list : {a[-1]}")


'''
Output:

python script.py 5 12 7 3 20

Largest element in the given list : 20
Smallest element in the given list : 3

'''
