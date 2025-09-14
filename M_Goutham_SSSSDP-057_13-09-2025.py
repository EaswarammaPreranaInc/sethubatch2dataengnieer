#  How  to  iterate  generator  with  for  loop
import  time 
def   f1(): # Generator function is defined as yield keyword is their inside the function
	print('One')
	yield  25
	print('Two')
	yield  10.8
	print('Three')
	yield  'Hyd'
	print('Four')
# End  of  generator
g = f1() #New generator object is created
for   x   in   g: #generator object is called in the for loop
	print(x)  #Prints the each statement inside the generator function in sequentially
	time . sleep(1) #This line will make execution to wait 1 sec next line will be printed
	print('Hello') #This 'Hello' will prints after each yield statement in the function
# End  of  for  loop
print('End') #prints after end of for loop
print(g) #Prints the type and address
#print(next(g)) #Stop iteration Error #as already all the statements are executed so there are no statements to be executed
g = f1() #Another generator object is created 
print(next(g)) #Prints the 'One'
                #Returns the 25
'''outputs:
One
25
Hello
Two
10.8
Hello
Three
Hyd
Hello
Four
End
Error
Type and address
One
25
''' 




# Most  tricky  program
# Find  outputs(Home  work)
import  time
def   f1(): #Here generator function is defined
	yield  25
	yield  10.8
	yield  'Hyd'
# End  of  generator
g = f1() #Here new empty generator object is created and points too g
print(next(g)) # 25
for  x  in   g:
	print(x) #10.8 #Hyd
print() #prints nothing
for  x  in   f1(): #Here again new generator object is created and iterated 
	print(x) #25 #10.8 #Hyd
print() #Prints nothing
gen = f1() #Here again new empty generator object is created and points to ref gen 
print(next(gen)) #25
for  x  in   f1(): #Here Again new generator object is created and iterated
	print(x) #25 #10.8 #Hyd
print(next(gen)) #10.8
'''
output:
25
10.8
Hyd

25
10.8
Hyd

25
25
10.8
Hyd
10.8
'''





#Find  outputs (Home  work)
import  time
g = (x * x   for    x    in    range(5)) #Here generator expression is pointing to ref g
for  y  in   g: #Here by using for loop we are iterating the generator object
	print(y) #Prints 0 1 4 9 16 
	time . sleep(2) #this will make the each iteration wait for 2 sec
	print('Hello') #After each iteration prints Hello
for  y  in   g: 
	print(y) #Here nothing is printed as there are no iterations left
'''output:
0
Hello
1
Hello
4
Hello
9
Hello
16
Hello'''
	



# Find  outputs (Home  work)
import  time
for  y  in   (x * x   for    x    in    range(5)): #Generator experession #We are iterating the expression
	print(y)
	time . sleep(2)
for  y  in   (x * x   for    x    in    range(5)): #Here again another new generator expression is created and iterated
	print(y)
	time . sleep(2)
'''output:
0
1
4
9
16
0
1
4
9
16
'''
	






# Find  outputs(Home  work)
import  time
g1 = (x * x   for  x  in  range(5)) #Here generator expression is created 
g2 = g1 #Here ref g2 is pointing to generator expression where g1 is pointing 
for  y  in  g1: #Here by using for loop we are iterating the generator expression
	print(y) #0 1 4 9 16
	time . sleep(2)
for  y  in  g2: 
	print(y) #Prints nothing as already we are iterated the expression no more are left
print(g1  is  g2) #True




#  Find  outputs (Home  work)
l = [x * x   for   x   in   range(5)] #List comprehension
print(l) #Prints the list of elements i.e [0,1,4,9,16]
print(type(l)) #<class 'list'>

s = {x * x   for   x   in   range(5)} #Set comprehension
print(s) #Prints the set of elements i.e {0,1,4,9,16}
print(type(s)) #<class 'set'>

d = {x : x * x    for   x   in   range(5)} #Dict comprehension
print(d) #Prints the key-value pairs i.e {0:0,1:1,2:4,3:9,4:16}
print(type(d)) #<class 'dict'>

g = (x * x   for   x   in   range(5)) #Generator expression #there is no tuple comprehension
print(g) #type and address
print(type(g)) #<class 'generator'>





#  Find  outputs (Home  work)
def  f1(): #Regular function is defined
	return  10 #10 is returned
	return  20 #Skipped
	return  30 #Skipped
def  f2(): #Generator expression
	yield  10
	yield  20
	yield  30
# End  of  the  function
print(f1()) #10
print(f1()) #10
print(f1()) #10
print() #nothing is printed
g = f2() #New generator object is created
print(next(g)) #10
print(next(g)) #20
print(next(g)) #30
print(next(g)) #Error #stopiteration




#  Prove  that  there  is  no  waiting  time  for  generator
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]')) #This is the list comprehension where initially all the elements are stored in the list and printed
print(timeit('( x * x   for  x  in  range(500) )')) #This is the generator expression where elements are yielded one at a time on demand
'''output:
here we are using 'timeit' to get the approximate execution time
list comprehension will take more time to give results 
generator expression will take less time compare to list comprehension'''




# Prove  that  there  is  no  memory  error  for  generator
import sys

list = [x * x for x in range(10000)]  # Here list comprehension is used, so all 10000 elements are computed and stored in memory
gen = (x * x for x in range(100000000000000000000000000000000000000000000000))  
# Here generator expression is used, so only generator object is created,
# values are produced one at a time on demand → no memory error even for huge ranges

print(sys.getsizeof(list))  # Prints the size of list object (large, because all elements are stored in memory)
print(sys.getsizeof(gen))   # Prints the size of generator object (very small, same size irrespective of range)





'''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  elements
'''
'''output:
Enter   first  number  :   10
Enter   second  number  :   7
Sum : 17
Differnece :  3
Product :  70
Division : 1.4285714285714286

Enter   first  number  :   10
Enter   second  number  :   0
Sum : 10
Differnece :  10
Product :  0
Division  by zero  is  not  permitted
'''

def f1(a,b):
    yield f"Sum : {a + b}"
    yield f"Differnece : {abs(a - b)}"
    yield f"Product : {a * b}"
    if b != 0:
        yield f"Division : {a / b}"
    else:
        yield "Division  by zero  is  not  permitted"
        
a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
g = f1(a,b)
for i in g:
    print(i)



'''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
'''
'''output:
Enter  start  value :  10
Enter  end  value :  20
10
11
12
13
14
15
16
17
18
19
20
'''

def f1(n, m):
    while n <= m:
        yield n
        n += 1

n = int(input("Enter 1st number: "))
m = int(input("Enter 2nd number: "))
for i in f1(n,m):
    print(i)
        

		

'''
Write  a   generator  to  generate  fibonacci  series

1) What  is  fibonacci  series ?  --->  0 , 1 , 1 , 2 , 3 , 5 , 8 , .....

2) What  is  the  formula  for  10th  term ?  --->  9th  term + 8th  term
    What  is  the  formula  for  3rd  term ?  ---> 2nd  term + 1st  term

3) What  are  the  first  two  terms ?  --->  0  and  1

4) Use  generator  function  and  for  loop
'''
'''
Enter the last value of fibonacci series:10
0
1
1
2
3
5
8
End
'''



def f1(n):
    a, b = 0, 1
    yield a
    yield b
    count = 2
    while count < n:
        c = a + b
        yield c
        a, b = b, c
        count += 1
        
n = int(input("Enter the last value of fibonacci series: "))
for i in f1(n):
    print(i)
print('End')

'''Output:
Enter the last value of fibonacci series: 10
0
1
1
2
3
5
8
13
21
34
End
'''