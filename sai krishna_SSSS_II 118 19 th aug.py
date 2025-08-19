1.Modify  the  following  program  with  walrus  operator

Hint:  Call  index()  method  only  once
'''
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
try:
	i = a . index(15)                               # 2
	while  True:
		print(i)                                # 5
		i = a . index(15 , i + 1)               # 8
except: 
	print(F'15  is  found  {a . count(15)}  times ') # 15 is found 3 times


2.def is_subsequence(first, second):
    it = iter(second)
    return all(item in it for item in first)


print(is_subsequence([10, 20, 30], [15, 18, 10, 12, 19, 20, 14, 12, 30, 25, 16]))          # True
print(is_subsequence([10, 20, 20], [15, 18, 10, 12, 19, 20, 14, 12, 30, 25, 16]))          # False
print(is_subsequence([2, 2, 5], [2, 2, 3, 4, 5]))                                          # True
print(is_subsequence([2, 4, 3], [2, 2, 3, 4, 5]))                                          # False


3.a = [10 , 20 , 15 , 18]
b = a . copy() 
print(b)                              # [10, 20, 15, 18]
print(a  is  b)                       # False
print(a  ==  b)                       # True
c = a[:]   
print(c)                              # [10, 20, 15, 18]
print(a  is  c)                       # False  
print(a  ==  c)                       # True
d = a  
print(d)                              # [10, 20, 15, 18]
print(a  is  d)                       # True
print(a  ==  d)                       # True


lst = list(map(int, input("Enter List : ").split(',')))

unique_elements = set(lst)
mode = None
max_count = 0

for element in unique_elements:
    count = lst.count(element)
    if count > max_count:
        max_count = count
        mode = element

print("Mode :", mode)                 # 15


4.a = [[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]]

print(a)                              # [[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]]
print(len(a))                         # 3

print(a[0])                           # [10, 20, 30, 40]
print(a[1])                           # [50, 60, 70, 80]
print(a[2])                           # [90, 100, 110, 120]

print(a[0][2])                        # 30
print(a[1][3])                        # 80 
print(a[2][1])                        # 100 


5.a = [ [10, 20], [30, 40, 50], [60, 70, 80, 90] ]

print(a[0])                           # [10, 20]
print(a[1])                           # [30, 40, 50]
print(a[2])                           # [60, 70, 80, 90]

print(len(a[0]))                      # 2
print(len(a[1]))                      # 3
print(len(a[2]))                      # 4


6.a = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]

print('Nested list with print function')
print(a)      #[[10, 20], [30, 40, 50], [60, 70, 80, 90]]

print('\nEach inner list of outer list without indexes (using for loop)')
for inner in a:
    print(inner)   # [10, 20]
                  # [30, 40, 50]
                   #[60, 70, 80, 90]

print('\nElements in the form of matrix without using indexes (using nested loop)')
for inner in a:
    for element in inner:
        print(element, end='\t')
    print()         # 10	20	
                    # 30	40	50	
                    # 60	70	80	90	


print('\nElements in the form of matrix using indexes (using nested loop)')
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end='\t')
    print()       # 10	20	
                  #30	40	50	
                 #60	70	80	90	


7.#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]]
for  x  in  a:
    print(x)        # [10, 20]
                    #[30, 40]
                    #[50, 60]
                    #[70, 80]
print()            # Emptty List
for  x , y  in  a:
	print(x , y , sep = '...')    # 10...20
                                  #30...40
                                  #50...60
                                  #70...80

8.#  Find  outputs (Home  work)
a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for  x  in  a:
    print(x)                 # [10, 20, 30]
                             #[40, 50, 60]
                             #[70, 80, 90]
print()                      # Empty List
for  x , y ,  z  in   a:
	print(x , y , z , sep = '...') # 10...20...30
                                   #40...50...60
                                   #70...80...90

9.#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for  x  in  a:
	print(x)               # [10, 20]
                           #[30, 40, 50]
                          #[60, 70, 80, 90]
for  x , y  in  a:       #  too many values to unpack (expected 2)
	print(x , y ,	sep = '...')   # name 'y' is not defined


10.a = [[]]

print("Inner list (method 1):")
print(a[0])                # []

print("Inner list (method 2):")
for inner in a:
    print(inner)           # []

11.#  Find  outputs  (Home  work)
a = [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]
print(sorted(a))                      #[[5, 'Amar', 5000.0], [10, 'Rama', 1000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [20, 'Sita', 2000.0]] 
print(sorted(a , reverse = True))     # [[20, 'Sita', 2000.0], [18, 'Kiran', 2800.0], [15, 'Rajesh', 3500.0], [10, 'Rama', 1000.0], [5, 'Amar', 5000.0]]
print(a)                              # [[10, 'Rama', 1000.0], [20, 'Sita', 2000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [5, 'Amar', 5000.0]]


