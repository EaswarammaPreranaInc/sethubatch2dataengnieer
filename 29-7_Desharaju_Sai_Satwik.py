m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye')
# Output:Bye

i = 2
match  i:
	case  1:
		print('One')
	case  _:
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye')
# Output:Error

m = 2
match  m:
	case  1:
		print('One')
	case  _:
		print('Hello')
	case  _:
		print('Bye')
print('End')
# Output:Error

m = 1
match  m:
	case  1:
		print('Hyd')
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye')
# Output:Hyd  
#Bye

x = eval(input('Enter any  number :  '))
match  x:
	case  7 |  -6  |  0:
		print('Hyd')
		print('Sec')
		print('Cyb')
	case  -10 | 15:
		print('One')
		print('Two')
		print('Three')
	case  _:
		print('India')
		print('China')
		print('Usa')
print('Bye')


tpl = eval(input('Enter  any  point  in  the  form  of  (x , y) :  '))
match  tpl:
	case  (0 , 0):
		print('Origin')
	case   (0 , y):
		print('y - axis')
	case   (x , 0):
		print('x - axis')
	case   (x , y):
		print('Quadrant')
	case  _:
		print('Not  a  point')

for  x  in   123:
	print(x)
# Output: Error

while  True:
	print('Hello')
print('Bye')
# Output: Infinite loop printing "Hello"

for  x  in  {10 : 20 , 30 : 40 , 50 : 60}.keys():
	print(x)
# Output:
#10  
#30  
#50

for  x  in  {10 : 20 , 30 : 40 , 50 : 60}.values():
	print(x)
# Output:
#20  
#40  
#60

for  x  in  {10 : 20 , 30 : 40 , 50 : 60}.items():
	print(x)
# Output:
#(10, 20)  
#(30, 40)  
#(50, 60)

for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x)
# Output:
#10  
#30  
#50


a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a.items():
	print(x , y , sep = '...')
# Output:
#10...20  
#30...40  
#50...60

for  x ,  y  in   a:
	print(x , y)
# Output:Error
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...')
# Output:Error


for  x   in   ():
	print(x)
for  x   in  []:
	print(x)
for  x   in   {}:
	print(x)
for  x   in   set():
	print(x)
for  x   in   '':
	print(x)
for  x  in  range(10 , 10):
	print(x)
for  x  in   range():
	print(x)
for  x  in   (25):
	print(x)
# Output:Error
