'''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''
'''
Enter  any   string  :  Hyd is green city
Words  of  the  string
Hyd
is
green
city
'''
def divide(n):
    c = n.split()
    for i in c:
        yield i

n = input("Enter the string: ")
print("Words of the string")
for i in divide(n):
    print(i)
	


# Find  outputs
def   f1(): #Here generator function is defined
        yield   [10 , 20]
        yield  {30 , 40 , 50}
        yield  60  , 70 , 80 , 90
        yield  100
# End  of  generator
g = f1() #Here new generator object is created
for   x   in   g: #Here we are iterating the generator function
	print(x) #Here each statement is printed
	print(type(x)) #And type is printed
        
'''output:
[10 20]
<class 'list'>
{30 40 50}
<class 'set'>
(60 70 80 90)
<class 'tuple'>
100 
<class 'int'>
'''
	


#  Find  outputs
def   f1(): #Here generator function is defined
	x = 1 
	while  x <=  100000000000000000000: #checking the condition 
		yield  x 
		x +=  1
# End of  generator
g = f1() #Here new generator object is created
print('Begin') # This is the 1st line that will execute
print(*g) #Unpacks the statments of generator function #It take more time to store the all the elements in the generator object
print('End') #This is the last line of the execution

'''output:
Begin
wait for the elements to be stored in the generator object or raise memory space error
End
'''



#  Find  outputs
g = (x * x  for  x  in  range(500000000000000000)) #Generator expression 
print(*g) #Unpacks the all the elements of generator expression and try to store all the elements into the generator object 



# Find  outputs  (Home  work)
def   f1(begin , end): #Here generator function is defined
	while  begin  <=  end: #Checks the condition weather begin less than or equal to end
			print('Hello') # Prints the Hello
			yield  begin #Returns the Begin value 
			begin += 1 #Increment toe begin by 1
	print('End  of  generator') #Last statement of the generator function
#end of the genrator  function
g = f1(10 , 20) #Here new generator object is created
print('Before') #Print the before
print(list(g)) #Here generator object g is converted to list
print('After') #Prints the After
print(next(g)) #Stopiteration error #already all the elements are iterated

'''output:
Before
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
End  of  generator
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
After
'''


'''
1) What  are  the  four  events  for  list(g) ?  --->
	a) generator  function  is  fully  executed  without  stoping  in  the  middle  even  though  there  is  yield  statement
	b) All  those  elements  which  are  yielded  are  stored  in  generator  object (Non-empty  object)
	c) generator  object  is  converted  to  list
	d) generator  object  becomes  empty

2) What  are  the  two  drawbacks  of  list(g) ?  --->  a) Waiting  time  when  there  are  too  many  yield  statements
																				   b)  Possibility  of  MemoryError

3) Hence  list(g)  is  not  recommended  for  generator  as  we  are  losing   the  power  of  generator
'''




#  Find    outputs (Home  work)
def      f1(): #Here generator function is defined
	print('One')
	yield    1
	print('Two')
	yield    2
	print('Three')
	yield    3
	print('End')
# End  of  generator
g = f1() #Here new generator object is created
for   m   in   g: #Iterating the generator object
	print(m) #Prints the statements of generator object
x ,  y ,  z  =  f1()  #Here new generator object is created and generator function is unpacked
print(x) #1
print(y) #2
print(z) #3
'''outputs:
one
1
Two
2
Three
3
End
one
Two
Three
End
1
2
3
'''



# Identify  error (Home  work)
def  f1(): #Here generator function is created
        yield  10 
        yield  20
        yield  30
        yield  40
a , b , c = f1() #Error #Here there are 4 yield statements but we are giving only 3
p , q , r , s , m = f1() #Error #Here there are 4 yield statements but we are giving only 5 



#  Find  outputs (Home  work)
def   f1(): #Generator function is created
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1() #Here new generator object is created
#print(len(g)) #Error #There is no len() in generator function
#print(g * 3) #Error #We cannot multiply generator obj as it only iterated once
#print(g[0])  #Error #No indexing for generators
#print(g[1 : 3]) #Error #No slicing
print(*g) #Prints the value 1 2 3