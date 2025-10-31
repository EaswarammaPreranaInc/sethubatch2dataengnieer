# How  to  iterate  zip  object  in  differenet  ways  (Home  work)
import   time
a = ['Telangana' , 'Andhra Pradesh' , 'Karnataka ', 'Tamilnadu']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore', 'Chennai']
z1 = zip(a , b)
print(type(z1))
print(z1)
print('Iterate  thru  zip  object  with   next()   function')
while True:
  try:   # How  to   iterate  thru  zip  object  with  next()  function
    print(next(z1))
  except:
    break
print('Iterate  thru  zip  object  with  _next_  method')
z2=zip(a,b)  # How  to   iterate  thru  zip  object  with  _next_()  method
while True:
  try:   # How  to   iterate  thru  zip  object  with  next()  function
    print(z2.__next__())
  except:
    break
print('Iterate  thru  zip  object  with   for  loop')
z3=zip(a,b) # How  to   iterate  thru  zip  object  with  for  loop
for x in z3:
  print(x)
print('Iterate  thru  elements  of  each  tuple  in  zip  object')
z4=zip(a,b)  # How  to   iterate  thru  elements  of  each  tuple  of  zip  object  with  for  loop
for x,y in z4:
  print(x,"...",y)
z5=zip(a,b)
print('Unpacks  zip  object  with   *  operator  :  ' ,*z5)
print()
z6=zip(a,b)
print('zip   object  in  the  form  of   list  :  ' ,list(z6))
print()
z7=zip(a,b)
print('zip   object  in  the  form  of   dictionary :  ' ,dict(z7))

# Output :
<class 'zip'>
<zip object at 0x000001D376EF7D40>
Iterate  thru  zip  object  with   next()   function
('Telangana', 'Hyderabad')
('Andhra Pradesh', 'Amaravathi')
('Karnataka ', 'Bangalore')
('Tamilnadu', 'Chennai')
Iterate  thru  zip  object  with  _next_  method
('Telangana', 'Hyderabad')
('Andhra Pradesh', 'Amaravathi')
('Karnataka ', 'Bangalore')
('Tamilnadu', 'Chennai')
Iterate  thru  zip  object  with   for  loop
('Telangana', 'Hyderabad')
('Andhra Pradesh', 'Amaravathi')
('Karnataka ', 'Bangalore')
('Tamilnadu', 'Chennai')
Iterate  thru  elements  of  each  tuple  in  zip  object
Telangana ... Hyderabad
Andhra Pradesh ... Amaravathi
Unpacks  zip  object  with   *  operator  :   ('Telangana', 'Hyderabad') ('Andhra Pradesh', 'Amaravathi') ('Karnataka ', 'Bangalore') ('Tamilnadu', 'Chennai')

zip   object  in  the  form  of   list  :   [('Telangana', 'Hyderabad'), ('Andhra Pradesh', 'Amaravathi'), ('Karnataka ', 'Bangalore'), ('Tamilnadu', 'Chennai')]

zip   object  in  the  form  of   dictionary :   {'Telangana': 'Hyderabad', 'Andhra Pradesh': 'Amaravathi', 'Karnataka ': 'Bangalore', 'Tamilnadu': 'Chennai'}

                                                                   
#  Find  outputs  (Home  work)
import   time
a = [ 'Empno' , 'Emp Name' , 'Salary']
b = [ 25 , 'Rama  Rao' , 10000.0 , 'Male' , True]
c = zip(a , b)
while   True:
	try:
		print(next(c))
		time . sleep(1)
	except  StopIteration:
		break

# Output :
('Empno', 25)
('Emp Name', 'Rama  Rao')
('Salary', 10000.0)


#  Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Banglore' , 'Chennai' , 'Mumbai']
c = [50000000 , 40000000 , 70000000 , 60000000 , 30000000]
for   x   in   zip(a , b , c):
	print(x)
	time . sleep(1)

# Output :
('Telangana', 'Hyderabad', 50000000)
('Andhra  Pradesh', 'Amaravathi', 40000000)
('Karnataka', 'Banglore', 70000000)
('TamilNadu', 'Chennai', 60000000)
('Maharastra', 'Mumbai', 30000000)


# Find  outputs   (Home  work)
import   time
a = [1 , 2 , 3]
b = [4 , 5 , 6 , 7 , 8]
for  x , y  in   zip(a , b):
	print(x + y)
	time . sleep(1)

# Output :
5
7
9


# Find outputs  (Home  work)
import   time
def   disp(z):
	while   True:
		try:
			print(next(z))
			time . sleep(1)
		except:
			break
	print()
a = [10 , 20 ,  30]
b = {1 : 2 , 3 : 4 , 5 : 6}
z1 = zip(a , b . keys())
disp(z1)
z2 = zip(a , b . values())
disp(z2)
z3 = zip(a , b . items())
disp(z3)
z4 = zip(a , b)
disp(z4)
z5 = zip(a)
disp(z5)
z6 = zip(b)
disp(z6)
z7 = zip()
disp(z7)

# Output :
(10, 1)
(20, 3)
(30, 5)

(10, 2)
(20, 4)
(30, 6)

(10, (1, 2))
(20, (3, 4))
(30, (5, 6))

(10, 1)
(20, 3)
(30, 5)

(10,)
(20,)
(30,)

(1,)
(3,)
(5,)




# Find  outputs  (Home  work)
z = zip(range(5) , range(20 , 25))
a = [ [x , y]  for  x , y   in   z]
print(a)

# Output :
[[0, 20], [1, 21], [2, 22], [3, 23], [4, 24]]
