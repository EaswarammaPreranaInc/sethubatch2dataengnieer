##1
a = [10, 20, 15, 12, 14, 15, 18, 19, 15, 12, 25]

try:
    i = -1
    while (i := a.index(15, i + 1)) != -1:
        print(i)
except ValueError:
    print(f'15 is found {a.count(15)} times')

##2
def is_sublist(small, big):
    try:
        pos = -1
        for x in small:
            pos = big.index(x, pos + 1)   # find next occurrence after last match
        return True
    except ValueError:
        return False


# Test cases
print(is_sublist([10, 20, 30], [15, 18, 10, 12, 19, 20, 14, 12, 30, 25, 16]))  # True
print(is_sublist([10, 20, 20], [15, 18, 10, 12, 19, 20, 14, 12, 30, 25, 16]))  # False
print(is_sublist([2, 2, 5], [2, 2, 3, 4, 5]))  # True
print(is_sublist([2, 4, 3], [2, 2, 3, 4, 5]))  # False

##3
# copy()  method  demo program  (Home  work)
a = [10 , 20 , 15 , 18]
b = a . copy()
print(b)# [10, 20, 15, 18]
print(a  is  b)# False
print(a  ==  b)# True
c = a[:]
print(c)# [10, 20, 15, 18]
print(a  is  c)# False
print(a  ==  c)# True
d = a
print(d)#[10, 20, 15, 18]
print(a  is  d)# True
print(a  ==  d)# True

##4
a = [12, 20, 18, 15, 10, 15, 10, 15, 20, 18, 15, 10, 20, 15, 10]

# initialize
mode = None
ctr = 0  

for x in set(a):   # unique elements
    count = a.count(x)
    print(f"{x} is repeated {count} times")   # just to see counts
    if count > ctr:   # update if this element occurs more times
        ctr = count
        mode = x

print("Mode =", mode)
print("Count =", ctr)
##5
#  Nested  List  demo  program  (Home  work)
a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a)
print(len(a))
print(*a[0])
print(*a[1])
print(*a[2])
print(*a[0][2])  
print(*a[1][3])  
print(*a[2][1])
##6
#  Find  outputs  (Home  work)
a=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
print(*a[0])
print(* a[1])
print(*a[2])
print(a[0][1])
print(a[1][2])
print(a[2][3])
##7
a = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]

print('Nested list with print function')
print(a)   # direct print

print('\nEach inner list of outer list without indexes')
for inner in a:   # loop directly over sublists
    print(inner)

print('\nElements in the form of matrix without using indexes')
for inner in a:       # loop over each inner list
    for elem in inner:  # loop over each element
        print(elem, end=" ")
    print()

print('\nElements in the form of matrix using indexes')
for i in range(len(a)):         # index for outer list
    for j in range(len(a[i])):  # index for inner list
        print(a[i][j], end=" ")
    print()

##8
#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]]
for  x  in  a:
    print(x)# [10, 20]
print()
for  x , y  in  a:
	print(x , y , sep = '...')# [10...20]

#  Find  outputs (Home  work)
a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for  x  in  a:
    print(x)#  [10, 20, 30]
print()
for  x , y ,  z  in   a:
	print(x , y , z , sep = '...')# [10...20...30]

#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for  x  in  a:
	print(x)# [10, 20]
for  x , y  in  a:
	print(x , y ,	sep = '...')# [30...40...50]
       
#  Find  outputs  (Home  work)
a = [[]]
print(*a)
print(extend(a))# 
      
#  Find  outputs  (Home  work)
a = [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]
print(sorted(a))
# [[5, 'Amar', 5000.0], [10, 'Rama', 1000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [20, 'Sita', 2000.0]]

print(sorted(a, reverse=True))
# [[20, 'Sita', 2000.0], [18, 'Kiran', 2800.0], [15, 'Rajesh', 3500.0], [10, 'Rama', 1000.0], [5, 'Amar', 5000.0]]

print(a)
# [[10, 'Rama', 1000.0], [20, 'Sita', 2000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [5, 'Amar', 5000.0]]
