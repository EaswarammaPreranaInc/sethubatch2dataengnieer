1.# eval()  function  demo  program
print(eval('25'))				#  25
print(eval('10.8'))				#  10.8
print(eval('False'))				#  False
print(eval('3+4j'))				# (3 + 4j)
print(eval('Hyd'))				# Error because 'Hyd' is not defined
print(eval("    'Hyd'   "))			 # "    'Hyd'   "
print(eval('3 + 4 * 5'))			# 3 + (4 * 5) = 3 + 20 = 23
print(eval('[10 , 20 , 15 , 18]'))		# [10 , 20 , 15 , 18]  # list
print(eval('{10,20,15,18,20,12,18}'))		# {10, 12, 15, 18, 20} # set
print(eval('(10 , 20 , 30)'))			 # (10 , 20 , 30) # Tuple
print(eval("{10 : 'Hyd' , 10 : 'Sec'}"))	# { 10 : 'Sec'}
print(eval(4 + 5))				# Error 




2.#  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   "))			# hyd
hyd = 'Sec' 
print(eval('hyd'))			        # sec
sec = '25'
print(eval('sec')) 				# 25
print(eval(sec))				 # 25
cyb = 10.8
print(eval('cyb'))				# 10.8
print(eval(cyb)) 				# Error.




3.#  Tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")'))			 # prints Hyd and returns None.




4.#  Find  outputs  (Home  work)
print(bool('False')) 				# True because it is non empty string.
print(eval('False'))				 # False because it is valid literal.
print(bool(''))      				# False because bool('')) is empty string
print(eval('  ""  ')) 				# Empty string
print(eval(''))      				 # Error
print(eval('  " "   '))				# (" ") because it prints a single space
print(eval(' '))				# Error because it contains only a single line space.




5.# What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  '))  	# Enter  any  input  : 12.8 
print(type(x)) 					# < class 'Float'>              
print(x)					 # 12.8




6.# What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ')				# Enter  any  string  : 'cyb'
print(len(a)) 							# 3
print(a)							# cyb

b = eval(input('Enter   any  string  : '))			# Enter   any  string  :'sec'	
print(len(b))							# 3
print(b)							 # sec




7.# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')  					 #   25 , 10.8 , Hyd
print(a , b , c , sep = '\t') 					# 25 <space> 10.8 <space> Hyd
print(a , b , c , sep = '---')					# 25---10.8---Hyd
print(a , b , c , sep = '\n') 					# 25
                              					# 10.8
                            				        # Hyd

print(a , b , c)						 # 25  10.8  Hyd
print(a , b , c , separator = ':')				# 25:10.8:Hyd


	

8.# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---')				 # 25 10.8 Hyd---25,,,10.8,,,Hyd
print(a , b , c , sep = ',,,') 				# 25:::10.8:::Hyd <Tabspace><Tabspace><Tabspace>25 10.8 Hyd
print(a , b , c , sep = ':::' , end = '\t\t\t')
print(a , b , c)




9.# Find outputs  (Home  work)
print('Hyd') 						# Hyd
print()							 #
print('Sec') 						# sec
print()							#
print('Cyb')						 # Cyb




10.# Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40]					 # list
t = (10 , 20 , 30 , 40) 				# Tuple
s = {10 , 20 , 30 , 40}					 # Set
print(l , t , s) 					# [10 , 20 , 30 , 40] (10 , 20 , 30 , 40) {10 , 20 , 30 , 40}




11.#  Find  outputs (Home  work)
a = 25
b = '%f'  %a
print(b)       			# '25.000000'   
print(type(b))			# <class 'str'>
x = 10.8
y = '%d'  %x
print(y)			# 10
print(type(y))			#<class 'str'>
m = [10 , 20 , 15 , 18]
n = '%s'  %m
print(n)			# "[10 , 20 , 15 , 18]"
print(type(n))			# <class 'str'>




12.# Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f'  %a) 			 #  <3  spaces>10.93
print('%9.1f'  %a)			#<5   spaces>10.9
print('%10.3f'  %a)			#4   spaces>10.927
print('%.2f'  %a)			# 10.93 with no spaces 
print('%.6f'  %a)			#10.927400 with 6 digits after decimal
print('%f'  %a)				#10.927400 with fixed length.




13.# Find  outputs (Home  work)
a = 'Hyd'
print('%7s'  %a)			#  <4  spaces>Hyd
print('%-7s'  %a)			#  Hyd<4   spaces>
print('%2s'  %a)			#  Hyd  and  ignores  smaller width
print('%s'  %a)				# Hyd
print('%s' , a)				# '%s',Hyd
print('%s'  a)				# Invalid 
print('%s' , %a)			# Invalid
print(a)				# Hyd




14.# Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40]
print('%s'  %a)						# "[10, 20, 30, 40]"
print('%s' , a)						#('%s', [10, 20, 30, 40])
print('%s'  a)						#Invalid
print('%s' , %a)					#Invalid
print('%l'  %a)						#Invalid 
print(a)						#[10, 20, 30, 40]




15.#Find outputs  (Home  work)
a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c))			#25    10.927400    Hyd
print('%i    %g    %s'    %(a , b , c))			#25    10.9274    Hyd
print('%s    %s    %s'  %(a , b , c))			#25    10.9274    Hyd
print('%d    %g    %s'  , a , b , c)			#%d    %g    %s 25 10.9274 Hyd
print('%d    %g      %s'   a , b , c)			#Invalid
print('%d    %g    %s'  ,  %(a , b , c))		#Invalid
print('%d    %g    %s'    %a%b%c)			#Invalid
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c) 	#25 10.927400 Hyd