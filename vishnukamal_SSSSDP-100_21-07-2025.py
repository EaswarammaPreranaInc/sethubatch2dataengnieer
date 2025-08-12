(21-07-2025)


# How  to  print  dictionary  in  different  ways

a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function') # How  to  print  dictionary  with  print()  function
print(a)	# output: {10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18: 'Sita'}

print('Keys  of  dictionary') # How  to  print  each  key  of  dict  'a'
print(a.keys())	# output: dict_keys([10, 20, 15, 18])

print('Values  of  dictionary') # How  to  print  each  value  of  dict  'a'
print(a.values()) # output: dict_values(['Ramesh', 'Kiran', 'Amar', 'Sita'])

print('All  the  tuples  of  dict_items   object') # How  to  print  each  tuple  of  the  list  in  dict_items  object
print(a.items()) # output: dict_items([(10, 'Ramesh'), (20, 'Kiran'), (15, 'Amar'), (18, 'Sita')])

print('Elements  of  each   tuple') # How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object
for item in a.items():
  print(item) 	# output: (10, 'Ramesh')
                          (20, 'Kiran')
       			  (15, 'Amar')
			  (18, 'Sita')

print('Keys  and  values  of  dictionary') # How  to  print  each  key  and  corresponding  value  in  dict  'a'
for key, value in a.items():
    print(key, ":", value)	# output: {10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18: 'Sita'}





#  Find  outputs (Home  work)

a = {
		print('Hyd') ,
		print('Sec') ,
		print('Cyb')
	}				# Hyd
					  Sec
					  Cyb
print(type(a))				# <class 'set'>
print(a)				# {None}
print(len(a))				# 1




#  Anonymous  object  demo  program

_ = 25
print(_)			# output: 25
print(type(_))			# output: <class 'int'>
a , _ , c = 10 , 20 , 30
print(a)			# output: 10
print(_)			# output: 20
print(c)			# output: 30
for  _  in  range(5):
	print(_ , 'Hello', sup=',')	# output: 0 Hello
					  1 Hello
					  2 Hello
					  3 Hello
					  4 Hello




#  Find  outputs

a = 25
print(id(a))	# Address  of   object  'a' 
a = 35
print(id(a))	# new address  of   object  'a'




# Find  outputs (Home  work)

a = 25.7
print(id(a))	# Address  of   object  'a' 
print(a)	# 25.7
a = 35.6	# the reference 'a' is modified to another object 'a': 35.6
print(id(a))	# new address  of   object  'a' 
print(a)	# 35.6
b = True	
print(id(b))	# Address  of   object  'b' 
b = False	# the reference 'b' is modified to another object 'b': False
print(id(b))	# new address  of   object  'b' 
c = None
print(id(c))	# Address  of   object  'c' 
c = None
print(id(c))	# same address  of   object  'c' 




#  Find  outputs  (Home  work)

a = 'Hyd'
print(id(a))	# address of int object 'a'
# a[1] = 'e'	# string object does not support item assignment
a = 'Sec'	# the reference 'a' is modified to another object 'a': 'sec'
print(id(a))	# new address  of  int object  'a' 
b = (10 , 20 , 15 , 18)
print(id(b))	# address of tuple object 'b'
#b[2] = 19	# tuple object does not support item assignment
b = (30 , 40 , 35 , 32)	# the reference 'b' is modified to another tuple object 'b': (30 , 40 , 35 , 32)
print(id(b))	# new address  of  tuple object  'b'
c = range(5)
print(id(c))	# address of range object 'c'
#c[3] = 10	# range object does not support item assignment
c = range(5)	# new range object is created as range object is not reusable
print(id(c))	# new address  of range object  'b'




# Find  outputs  (Home  work)


a = 25
b = 25
print(a  is  b)	# output: True as int objects can be reused
c = 'Hyd'
d = 'Hyd'
print(c  is  d)	# output: True as str objects can be reused
e = False
f = False
print(e  is  f)	# output: True as bool objects can be reused
g = range(10)
h = range(10)
print(g  is  h)	# # output: False as range objects cannot be reused





#Find  outputs(Home  work)

a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b)		# output: False as list objects cannot be reused
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d)		# output: False as dict objects cannot be reused
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f)		# output: True as tuple objects can be reused
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h)		# output: False as set objects cannot be reused




# Find outputs (Home work)

print(10 + 20)				# output: 30
print(10.8 + 20.6)			# output: 31.4
print(3 + 4j + 5 + 6j)			# output: (8+10j)
print(True + False)			# output: 1
print('Hyder' + 'abad')			# output: Hyderabad
print('Sankar' + 'Dayal' + 'Sarma')	# output: SankarDayalSarma
print('10' + '20')			# output: 1020
print([10 , 20 , 30] + [1 , 2 , 3])	# output: [10, 20, 30, 1, 2, 3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None))	# output: (25, 10.8, 'Hyd', (3+4j), True, None)
#print({10 , 20} + {30 , 40})		# error as sets objects cannot be added
#print({10 : 'Hyd'} + {20 : 'Sec'})	# error as dict objects cannot be added
#print(range(4) + range(5))		# error as range objects cannot be added
#print(10 + '20')			# error as int and str objects cannot be added
#print([10 , 20 , 30] + 5)		# error as list and int objects cannot be added
#print([10 , 20 , 30] + (40 , 50 , 60))	# error as list and tuple objects cannot be added




# Find outputs (Home work)

print(25 * 3)			# output: 75
print(10.8 * 25.6)		# output: 276.48
print(True * False)		# output: 0
print((3 + 4j) * (5 + 6j))	# output: (-9+38j)
print(3 + 4j * 5 + 6j)		# output: (3+26j)
print('25' * 3)			# output: 252525
print(3 * '25')			# output: 252525
print('Hyd' * 4)		# output: HydHydHydHyd
print([10 , 20 , 15] * 2)	# output: [10, 20, 15, 10, 20, 15]
print((25, 10.8, 'Hyd', True) * 3) # output: (25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True)
#print([10 , 20 , 15] * 3.0)	# error can't multiply sequence by non-int type
#print({10 , 20 , 15} * 2)	# error as set and int objects cannot be multiply
#print({10 : 20 , 30 : 40} * 2)	# error as dict and int objects cannot be multiply
print([10] * [20])		# error can't multiply sequence by non-int type




#  /  operator  demo  program

print(9.0 / 2)		# output: 4.5
print(9 / 2.0)		# output: 4.5
print(9.0 / 2.0)	# output: 4.5
print(9 / 2)  #  4.5	# output: 4.5
print(10.5 / 2)		# output: 5.25
print(10 / 3)		# output: 3.33
print(10 / 2)		# output: 5.0




#  //  operator  demo  program


print(9 // 2)		# prev  integer  of 4.5 = 4
print(9.0 // 2)		# prev  integer  of 4.5 = 4.0
print(9 // 2.0)		# prev  integer  of 4.5 = 4.0
print(9.0 // 2.0)	# prev  integer  of 4.5 = 4.0
print(10.5 // 2)	# prev  integer  of 5.25 = 5.0
print(10 // 3)		# prev  integer  of 3.33 = 3
print(10.0 // 3)	# prev  integer  of 3.33 = 3.0
print(8.5 // 3)		# prev  integer  of 2.83 = 2.0
print(18 // 4)		# prev  integer  of 4.5 = 4
print(-18 // 4)		# prev  integer  of -4.5 = -4
print(-(18 // 4))	# prev  integer  of -4.5 = -4




# % operator demo program


print(9 % 5)	# output: 4
print(9.0 % 5)	# output: 4.0
print(9 % 5.0)	# output: 4.0
print(9.0 % 5.0)# output: 4.0
print(10.5 % 2) # output: 0.5
print(8.9 % 3)	# output: 2.90





# Find outputs

#print(7 / 0)	# error we can't divided any number with '0'
#print(7 // 0)	# error we can't divided any number with '0'
#print(7 % 0)	# error we can't do mudulus with '0'



# ** operator demo program

print(3 ** 4)		# output: 81
print(10 ** -2)		# output: 0.01
print(4 * 3 * 2)	# output: 24
print(3 + 4 * 5 - 32 / 2 ** 3)	# output: 19.0




#  Relational  operators  demo  program (Home  work)

print(9 >= 5)		#   True :  >  is  satisfied
print(9 >= 9)   	#   True :  =  is  satisfied
print(9 >= 12)  	#  False :  Both  are  not  satisfied
print(6 <= 8)		#   True :  <  is  satisfied
print(6 <= 6)		#   True :  =  is  satisfied
print(6 <= 4)		#  False :  Both  are  not  satisfied
print(9 != 7)		#   True :  !=  is  satisfied
print(6 == 8)		#  False :  ==  is  satisfied
print(True  >  False)	#   True :  >  is  satisfied
print(3 + 4j == 3 + 4j)	#   True :  ==  is  satisfied
print(3 + 4j == 5 + 6j)	#  False :  ==  is  satisfied
print(3 + 4j != 5 + 6j) #   True :  !=  is  satisfied
print(10 == 10.0)	#   True :  ==  is  satisfied
print(3 + 4j >  3 + 4j)	#  error as > is not supported for complex objects





#  Find  outputs  (Home  work)

print('Rama'   >  'Rajesh')	#  True : 'm' > 'j'
print('Rama'  <  'Sita') 	#  True : 'R' < 'S'
print('Hyd'  ==  'Hyd')		#  True : 'Hyd'  ==  'Hyd'
print('Rama'  <=   'Ramana')	#  True : '' < 'na'
print('Rama  Rao'  >=  'Rama')	#  True : ' Rao' < ''
print('Hyd'  != 'Sec')		#  True : 'Hyd'  != 'Sec'
print('HYD'  <   'hyd')		#  True : 'HYD'  <   'hyd'




# Chaining  relational  opeartors  (Home work)

print(10 < 20 < 30)  	#   True  : 10 < 20 < 30
print(10 >= 20 < 30)  	#   False : 10  is  not  >= 20
print(10 < 20 > 30)	#   False : 20  is  not  > 30
print(1 < 2 < 3 < 4)	#   True  : 1 < 2 < 3 < 4
print(1 < 2 > 3 > 1)	#   False : 2 is  not > 3
print(4 > 3 >= 3 > 2)	#   True  : 4 > 3 >= 3 > 2





#  or  operator  demo program

print(True  or  False) 	# output:  True
print(False  or  True) 	# output:  True
print(True  or  True) 	# output:  True
print(False  or   False)# output:  False
print(10  or  20)	# output:  10	
print(0   or  20)  	# output:  20
print(-25  or  0)	# output:  -25
print(''  or  35)	# output: 35
print(6j  or  'Hyd')	# output: 6j
print(0.0  or  3 + 4j)	# output: (3+4j)
print('Hyd'   or   10.8)# output: Hyd





# not  operator  demo  program

print(not  True)	#  False
print(not  False)	#  True
print(not  25)		#  False
print(not  0)		#  True
print(not  'Hyd')	#  False
print(not  '')		#  True
print(not  -10)		#  False
print(not  not  'Hyd')	#  True





#  Find   outputs (Home work)

i = 10
i = not  i > 14 
print(i)	#  True
print(not(6 < 4  or  9 >= 5  and  6 != 6)) #  True