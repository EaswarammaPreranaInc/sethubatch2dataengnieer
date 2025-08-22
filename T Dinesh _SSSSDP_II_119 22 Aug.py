#index()  and  count()  methods  demo  program   (Home  work)
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#     0    1      2     3    4     5     6    7     8    9    10
try:
	i = a . index(15)
	while  True:
		print('15 is found at index : ' , i)
		i = a . index(15 , i + 1)
except:
		print(F'15  is  found  {a . count(15)}  times')
		
'''
output:-
15 is found at index :  2
15 is found at index :  5
15 is found at index :  8
15  is  found  3  times
'''





a = (10, 20, 30, 40, 50)
print("Before:", a, id(a))

a = a[:2] + (35,) + a[3:]   # replace index 2 (30) with 35

print("After:", a, id(a))







# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
a . remove(30) # Error
del  a[2] # Error
a . pop(2) # Error
print(a)
print(id(a))
How  to  remove  30  from  tuple  'a'
print(a)
print(id(a))

'''
a = (10, 20, 30, 40, 50)
print("Before:", a, id(a))

temp = list(a)    # convert to list
temp.remove(30)   # remove element
a = tuple(temp)   # convert back to tuple

print("After:", a, id(a))
'''





a = ((10, 20), (30, 40, 50), (60, 70, 80, 90))
print(a)             # whole tuple
print(type(a))       # <class 'tuple'>
print(len(a))        # 3 -> there are 3 inner tuples

# Access inner tuples
print(a[0])          # 1st inner tuple -> (10, 20)
print(a[1])          # 2nd inner tuple -> (30, 40, 50)
print(a[2])          # 3rd inner tuple -> (60, 70, 80, 90)

# Access specific elements
print(a[0][1])       # 20  → 1st tuple, index 1
print(a[1][2])       # 50  → 2nd tuple, index 2
print(a[2][3])       # 90  → 3rd tuple, index 3






a = ((10, 20, 30),)

# print inner tuple
print(a[0])         # (10, 20, 30)
print(a[-1])        # (10, 20, 30) -> another way

# print individual elements
print(a[0][0])      # 10
print(a[0][1])      # 20
print(a[0][2])      # 30


b = ((),)

# print inner tuple of 'b'
print(b[0])         # ()
print(b[-1])        # () -> another way






#  Find  outputs (Home  work)
a = ((10 , 20 , 30))
print(a) # (10, 20, 30)
print(*a) # 10 20 30
b = (())
print(b) # ()
print(*b) # nothing is printed because tuple is empty





# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')
print(a) # {10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(a)) # <class 'str'>
b = eval(a)
print(b) # {18, 20, 10, 12, 15}
print(type(b)) # <class 'set'>





#  Find  outputs  (Home  work)
print({(10 , 20 , 30)}) # {(10, 20, 30)}
print({[10 , 20 , 30]}) # Error
print({{10 , 20 , 30}}) # Error
print({{}}) # Error





->Direct print using print()
print("Set with print function:")
print(a)
->Iterate elements of set with for loop
print("Iterate elements of set with for loop:")
for element in a:
    print(element)
->Print using unpacking (*)
print("Set with unpacking (*):")
print(*a)
->Print using join() (works only if all elements are strings)
b = {"apple", "banana", "kiwi"}
print("Set with join:")
print(", ".join(b))





# Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s) # {'Hyd', True, 25}
print(len(s)) # 3
print(type(s)) # <class 'set'>





# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) # {25, 10.8, 'Hyd', True}
a , b , c , d = s
print(a) # 25
print(b) # 10.8
print(c) # Hyd
print(d) # True




# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) # {25, 10.8, 'Hyd', True}
a , *b = s
print(a) # 25
print(b) # [10.8, 'Hyd', True]
print(type(b)) # <class 'list'>




# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) # {25, 'Hyd', 10.8, True}
a , *b , c = s
print(a) # 25
print(b) # ['Hyd', 10.8]
print(c) # True




# Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s) # {10, 20}
x , y = s
print(x) # 10
print(y) # 20





a = range(100 , 151 , 10)
b = set(a)
print(b) # {130, 100, 140, 110, 150, 120}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d) # {10, 12, 15, 18, 50, 20}
e = set('Rama  rAo')
print(e) # {'R', 'o', 'm', 'r', 'a', ' ', 'A'}
print(set(25)) # Error
print(set()) # set()




