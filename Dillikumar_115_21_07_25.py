# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function')
	Print(a)
How  to  print  dictionary  with  print()  function
print('Keys  of  dictionary')
How  to  print  each  key  of  dict  
	for key in a.keys():
	    print(key)

print('Values  of  dictionary')
	for value in a.values():
	    print(value)
How  to  print  each  value  of  dict  'a'
	
print('All  the  tuples  of  dict_items   object')
	print(a.items())
How  to  print  each  tuple  of  the  list  in  dict_items  object
	for item in a.items():
	    print("Key:", item[0], "Value:", item[1])
print('Elements  of  each   tuple')
	for tuple_item in a.items():
                      print(tuple_item)
How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object
print('Keys  and  values  of  dictionary')
	for key in a:
	    print("Key:", key, "Value:", a[key])
How  to  print  each  key  and  corresponding  value  in  dict  'a'
#  Find  outputs (Home  work)
a = {     print('Hyd') ,  print('Sec') ,      print('Cyb')   }
print(type(a))
	<class ‘set’ > 
print(a)
	a = {     print('Hyd') ,  print('Sec') ,      print('Cyb')   }
print(len(a)) : 3

#  Find  outputs
a = 25
print(id(a))   : 140711716527288 
a = 35
print(id(a))  : 140711716527608
# Find  outputs (Home  work)
a = 25.7
print(id(a))  : 2201938275440 
print(a)   25.7
a = 35.6
print(id(a)): 1648192685360 
print(a)  : 35.6
b = True
print(id(b)) : 140711728316048
b = False
print(id(b)) : 140711728316080
c = None
print(id(c))  : 140711728316112 
#  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a))
a[1] = 'e'
a = 'Sec'
print(id(a))
b = (10 , 20 , 15 , 18)
print(id(b))  :  1763652405344
b[2] = 19
b = (30 , 40 , 35 , 32)
print(id(b))
c = range(5)
print(id(c))
c[3] = 10
c = range(5)
print(id(c)) 
#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b)  : 0 or false
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d)   : o or false 
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f)   :  it’s a tuple allow multi objects , true 
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h)   : false 

# Find outputs (Home work)
print(10 + 20)         : 30
print(10.8 + 20.6)  : 31.4
print(3 + 4j + 5 + 6j)   :  8+ 10j
print(True + False)  : 1+0 =1
print('Hyder' + 'abad')  : ‘Hyderabad ‘
print('Sankar' + 'Dayal' + 'Sarma')   : ‘sankarDayalsarma
print('10' + '20')   :              10 20
print([10 , 20 , 30] + [1 , 2 , 3])      : [ 1, 2,3, 10, 20, 30 ]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None))   :   (25 , 10.8 , 'Hyd' , 3 + 4j , True , None)   
print({10 , 20} + {30 , 40})    : {} error
print({10 : 'Hyd'} + {20 : 'Sec'})  :    error
print(range(4) + range(5)) : error
print(10 + '20') : error
print([10 , 20 , 30] + 5)        :error
print([10 , 20 , 30] + (40 , 50 , 60))   : error

# Find outputs (Home work)
print(25 * 3)               75
print(10.8 * 25.6)    276.48  
print(True * False) : false   
print((3 + 4j) * (5 + 6j))        :  38j+24j*j+15  =  15-24 + 38j  38j+9
print(3 + 4j * 5 + 6j)        3+26j
print('25' * 3)   25 25 25 
print(3 * '25')   252525
print('Hyd' * 4)   ‘HydHydHydHyd’
print([10 , 20 , 15] * 2)       [10 , 20 , 15, 10 , 20 , 15]
print((25, 10.8, 'Hyd', True) * 3)  : (25, 10.8, 'Hyd', True , 25, 10.8, 'Hyd', True , 25, 10.8, 'Hyd', True)
print([10 , 20 , 15] * 3.0) : error 
print({10 , 20 , 15} * 2)”error
print({10 : 20 , 30 : 40} * 2)    : not multiply 
print([10] * [20]) : errorr

#  /  operator  demo  program
print(9.0 / 2)  : 4.5
print(9 / 2.0) : 4.5
print(9.0 / 2.0) :4.5
print(9 / 2)    : 4.5
print(10.5 / 2)  :   5.25
print(10 / 3) :3.3333_
print(10 / 2) : 5.0  or 5

#  //  operator  demo  program
print(9 // 2)  #   prev  integer  of (4.5) = 4
print(9.0 // 2)      :  4
print(9 // 2.0)  :4
print(9.0 // 2.0)  :4
print(10.5 // 2)  : 5
print(10 // 3)  : 3
print(10.0 // 3)  #    prev  integer  of  3.33 = 3.0
print(8.5 // 3)  
print(18 // 4)  : 4
print(-18 // 4)  : -4
print(-(18 // 4))    : -4
# % operator demo program
print(9 % 5)            : 4
print(9.0 % 5)   :4.0
print(9 % 5.0)  :  4.0
print(9.0 % 5.0) :  4 .0
print(10.5 % 2)  #   0.5
print(8.9 % 3)  : 2.9
# Find outputs
print(7 / 0)    :0 
print(7 // 0)  : 0
print(7 % 0)  : 0

# ** operator demo program
print(3 ** 4)  : 81
print(10 ** -2) :  0.01
print(4 ** 3 ** 2)  : 4**9=  262144
print(3 + 4 * 5 - 32 / 2 ** 3)   :  23-4  =19

#  Find  outputs  (Home  work)
print('Rama'   >  'Rajesh')  #   True :  'm' > 'j'       :    true
print('Rama'  <  'Sita') #  True : 'R' < 'S'            :  true 
print('Hyd'  ==  'Hyd')  : true 
print('Rama'  <=   'Ramana')   :true
print('Rama  Rao'  >=  'Rama')  : true 
print('Hyd'  != 'Sec') : true  
print('HYD'  <   'hyd') :    true
 # Chaining  relational  opeartors  (Home work)
print(10 < 20 < 30)  #   True
print(10 >= 20 < 30)  #   False : 10  is  not  >= 20
print(10 < 20 > 30)  :   false
print(1 < 2 < 3 < 4)  : true 
print(1 < 2 > 3 > 1) : false 
print(4 > 3 >= 3 > 2): true 

#  or  operator  demo program
print(True  or  False) #  True
print(False  or  True) #   True
print(True  or  True) #  True
print(False  or   False)   #  False
print(10  or  20)#  10     
print(0   or  20)  #  20
print(-25  or  0)  : -25
print(''  or  35)  : 35
print(6j  or  'Hyd')  : 6j
print(0.0  or  3 + 4j)  : 3+4j
print('Hyd'   or   10.8) : ‘hyd’

# not  operator  demo  program
print(not  True) #   False
print(not  False) #  True
print(not  25) : false
print(not  0)  : true 
print(not  'Hyd')  : false
print(not  '')   : true
print(not  -10) : false 
print(not  not  'Hyd')  : true 

#  Find   outputs (Home work)
i = 10
i = not  i > 14   
print(i)   true 
print(not(6 < 4  or  9 >= 5  and  6 != 6))  : true   // not false ==true  
