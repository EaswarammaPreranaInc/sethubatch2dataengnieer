(24-07-2025)


# eval()  function  demo  program

print(eval('25'))				# Output: 25
print(eval('10.8'))				# Output: 10.8
print(eval('False'))				# Output: False
print(eval('3+4j'))				# Output: 3+4j
print(eval('Hyd'))				# throws error as 'Hyd' is itself is string  
print(eval("    'Hyd'   "))			# Output: Hyd
print(eval('3 + 4 * 5'))			# Output: 23
print(eval('[10 , 20 , 15 , 18]'))		# Output: [10 , 20 , 15 , 18]
print(eval('{10,20,15,18,20,12,18}'))		# Output: {10,20,15,18,20,12,18}
print(eval('(10 , 20 , 30)'))			# Output: (10 , 20 , 30)
print(eval("{10 : 'Hyd' , 10 : 'Sec'}"))	# Output: {10 : 'Hyd' , 10 : 'Sec'}
print(eval(4 + 5))				# throws error eval() arg must be a string




#  Tricky  program
# Find  outputs  (Home  work)

print(eval("    'hyd'   "))	# Output: hyd
hyd = 'Sec'			
print(eval('hyd'))		# Output: sec
sec = '25'			
print(eval('sec'))		# Output: 25
print(eval(sec))		# Output: 25 it is a integer
cyb = 10.8
print(eval('cyb'))		# Output: 10.8 it is a float 
print(eval(cyb))		# throws error eval() arg must be a string




#  Tricky  program
#  Find  output  (Home  work)

print(eval('print("Hyd")'))	# here first "Hyd" is printed then moves to next line and also returns None value so eval('None') is None output: Hyd
																		  None





#  Find  outputs  (Home  work)

print(bool('False'))		# Output: True
print(eval('False'))		# Output: False 
print(bool(''))			# Output: False because of empty sting
print(eval('  ""  '))		# Output: empty string
#print(eval(''))		# error because no arguments in eval()
print(eval('  " "   '))		# Output: <space>
print(eval(' '))		# error because no arguments in eval()





# What  is  the  advantage  of  eval(input()) ?

x = eval(input('Enter  any  input  :  '))	# Enter  any  input  :  'Hyd'
print(type(x))					# <class 'str'>
print(x)					# output: Hyd





# What  is  a  better  approach  to  read  string  input ?

a = input('Enter  any  string  :  ')		# if any input is entered the input() will consider it as a string enter any string: Hyd 
print(len(a))					# 3
print(a)					# Hyd
b = eval(input('Enter   any  string  : '))	# in eval() the entered value should be in "" orelse it throws error : '1000' 
print(len(b))					# 4
print(b)					# 1000 is a string
 



  
# sep  argument  demo  program  (Home  work)

a , b , c = 25 , 10.8 , 'Hyd'		
print(a , b , c , sep = ',')		# Output: 25, 10.8, Hyd
print(a , b , c , sep = '\t')		# Output: 25	10.8	Hyd
print(a , b , c , sep = '---')		# Output: 25---10.8---Hyd
print(a , b , c , sep = '\n')		# Output: 25<nextline>10.8<nextline>Hyd
print(a , b , c)			# Output: 25 10.8 Hyd
print(a , b , c , separator = ':')	# Output: 25:10.8:Hyd




# Find  outputs  (Home  work)

a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---')				# total output: 	25 10.8 Hyd---25,,,10.8,,,Hyd
print(a , b , c , sep = ',,,')							25:::10.8:::Hyd<tab><tab><tab>25 10.8 Hyd
print(a , b , c , sep = ':::' , end = '\t\t\t')
print(a , b , c)					# when only end is given next output will comes in same line, sep means separate object with anything we give, 
							\t tab space




# Find outputs  (Home  work) 

print('Hyd')	# Output: Hyd
print()		# Output: empty
print('Sec')	# Output: Sec
print()		# Output: empty
print('Cyb')	# Output: Cyb




# Find  outputs  (Home  work)

l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s)	# output: [10, 20, 30, 40]<space>(10, 20, 30, 40)<space>{40, 10, 20, 30}




# Find  Outputs  (Home  work)

a = 10.9274
print('%8.2f'  %a)	# output:  <3  spaces>10.93
print('%9.1f'  %a)	# output:<5 spaces>10.9
print('%10.3f'  %a)	# output: <4 spaces>10.927
print('%.2f'  %a)	# output:10.93
print('%.6f'  %a)	# output:10.927400
print('%f'  %a)		# output:10.927400




#  Find  outputs (Home  work)

a = 25
b = '%f' % a
print(b)             # output: 25.000000 
print(type(b))       # <class 'str'> 
x = 10.8
y = '%d' % x
print(y)             # 10 
print(type(y))       # <class 'str'> 
m = [10, 20, 15, 18]
n = '%s' % m
print(n)             # [10, 20, 15, 18] 
print(type(n))       # <class 'str'> 




# Find  outputs (Home  work)

a = 'Hyd'
print('%7s'  %a)	# output: <4  spaces>Hyd
print('%-7s'  %a)	# output:  Hyd<4   spaces>
print('%2s'  %a)	# output: Hyd  and  ignores  smaller width
print('%s'  %a)		# output: Hyd only string printed
print('%s' , a)		# output: ('%s', 'Hyd') : Prints as tuple
print('%s'  a)		# throws error as missing '%' operator 
print('%s' , %a)	# throws error as the format is invalid 
print(a)		# output: Hyd




# Find  outputs  (Home  work)

a = [10 , 20 , 30 , 40]
print('%s'  %a)		# output: [10 , 20 , 30 , 40]
print('%s' , a)		# output: ('%s', [10 , 20 , 30 , 40])
print('%s'  a)		# throws error as missing '%' operator
print('%s' , %a)	# throws error as format is invalid
print('%l'  %a)		# throws error as  '%l' is not a valid format specifier
print(a)		# output: [10 , 20 , 30 , 40]




#Find outputs  (Home  work)

a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c))	# output: 25 10.927400 Hyd
print('%i    %g    %s'    %(a , b , c))	# output: 25 10.927400 Hyd
print('%s    %s    %s'  %(a , b , c))	# output: 25 10.927400 Hyd
print('%d    %g    %s'  , a , b , c)	# output: ('%d    %g    %s', 25, 10.9274, 'Hyd') 
print('%d    %g      %s'   a , b , c)	# throws error as missing '%' operator
print('%d    %g    %s'  ,  %(a , b , c))# throws error as '%' operator is wrongly placed 
print('%d    %g    %s'    %a%b%c)	# throws error as format is invalid
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c) # output: 25 10.927400 Hyd : Each formatted separately, printed as tuple