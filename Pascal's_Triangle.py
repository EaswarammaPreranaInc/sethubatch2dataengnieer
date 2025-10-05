'''
Pattern : Pascal's Triangle
Input:ex-> 6
o/p:
1
1 1 
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
'''

def pattern(n):
    a = []
    for i in range(n):
        b = []
        for j in range(i+1):           
            if j == 0 or j == i:
                b.append(1)
            else:
                b.append(a[j-1] + a[j])
        print(*b)
        a = b
            

n = int(input('Enter no of rows : '))
pattern(n)