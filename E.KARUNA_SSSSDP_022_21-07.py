#How to print dictionary in different ways.
a= {10: 'Ramesh', 20:' Kiran', 15:' Amar', 18: 'sita'}
print(a) #{ 10: 'Ramesh', 20: ' kiran', 15: 'Amar', 18: 'sita'}
print(a. keys()) #  dict-keys ([10, 20, 15, 18]). print the each Keys of 'a'.
print (a. values ()) #  dict-values (['Ramesh', 'kiran', 'Amar', 'sita']) print the each value of dict 'a'
print(a. items ()) # dict-items ([(10,' Ramesh'), (20, 'Kiran'), (15, 'Amar'), (18, 'Sita')]). print  all of each  tuples of dict- items object
for key, values in a. items ():
    print (f" Keys: {key}, values: {values}")                                                                                                                                                                                #keys: 10, values: Ramesh                                                                                                                                                                                                                       Keys: 20, values: Kiran
for key, values in a. items():
    print (f" {key}: {values }")
print()
#  Find  outputs (Home  work)
a = {
		print('Hyd') ,
		print('Sec') ,
		print('Cyb')
	}
print(type(a))
print(a)
print(len(a))
print()
#  Anonymous  object  demo  program
_ = 25
print(_)
print(type(_))
a , _ , c = 10 , 20 , 30
print(a)
print(_)
print(c)
for  _  in  range(5):
	print(_ , 'Hello')
print()
#  Find  outputs
a = 25
print(id(a))
a = 35
print(id(a))
print()
# Find  outputs (Home  work)
a = 25.7
print(id(a))
print(a)
a = 35.6
print(id(a))
print(a)
b = True
print(id(b))
b = False
print(id(b))
c = None
print(id(c))
c = None
print(id(c))
print()
#  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a))
#a[1] = 'e'#error
a = 'Sec'
print(id(a))
b = (10 , 20 , 15 , 18)
print(id(b))
#b[2] = 19#error
b = (30 , 40 , 35 , 32)
print(id(b))
c = range(5)
print(id(c))
#c[3] = 10#error
c = range(5)
print(id(c))
print()
# Find  outputs  (Home  work)
a = 25
b = 25
print(a  is  b)
c = 'Hyd'
d = 'Hyd'
print(c  is  d)
e = False
f = False
print(e  is  f)
g = range(10)
h = range(10)
print(g  is  h)
print()
#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b)
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d)
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f)
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h)
print()
# Find outputs (Home work)
print(10 + 20)
print(10.8 + 20.6)
print(3 + 4j + 5 + 6j)
print(True + False)
print('Hyder' + 'abad')
print('Sankar' + 'Dayal' + 'Sarma')
print('10' + '20')
print([10 , 20 , 30] + [1 , 2 , 3])
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None))
#print({10 , 20} + {30 , 40})#error
#print({10 : 'Hyd'} + {20 : 'Sec'})#error
#print(range(4) + range(5))#error
#print(10 + '20')#error
#print([10 , 20 , 30] + 5)#error
#print([10 , 20 , 30] + (40 , 50 , 60))#error
print()
# Find outputs (Home work)
print(25 * 3)
print(10.8 * 25.6)
print(True * False)
print((3 + 4j) * (5 + 6j))
print(3 + 4j * 5 + 6j)
print('25' * 3)
print(3 * '25')
print('Hyd' * 4)
print([10 , 20 , 15] * 2)
print((25, 10.8, 'Hyd', True) * 3)
#print([10 , 20 , 15] * 3.0)#error
#print({10 , 20 , 15} * 2)#error
#print({10 : 20 , 30 : 40} * 2)#error
#print([10] * [20])#error
print()
#  /  operator  demo  program
print(9.0 / 2)
print(9 / 2.0)
print(9.0 / 2.0)
print(9 / 2)  #  4.5
print(10.5 / 2)
print(10 / 3)
print(10 / 2)
print()
#  //  operator  demo  program
print(9 // 2)  #   prev  integer  of (4.5) = 4
print(9.0 // 2)
print(9 // 2.0)
print(9.0 // 2.0)
print(10.5 // 2)
print(10 // 3)
print(10.0 // 3)  #    prev  integer  of  3.33 = 3.0
print(8.5 // 3)
print(18 // 4)
print(-18 // 4)
print(-(18 // 4))
print()
# % operator demo program
print(9 % 5)
print(9.0 % 5)
print(9 % 5.0)
print(9.0 % 5.0)
print(10.5 % 2)  #   0.5
print(8.9 % 3)
print()
# Find outputs
#print(7 / 0)#error
#print(7 // 0)#error
#print(7 % 0)#error
print()
# ** operator demo program
print(3 ** 4)
print(10 ** -2)
print(4 ** 3 ** 2)
print(3 + 4 * 5 - 32 / 2 ** 3)
print()
#  Relational  operators  demo  program (Home  work)
print(9 >= 5)  #   True :  >  is  satisfied
print(9 >= 9)   #   True :  =  is  satisfied
print(9 >= 12)   #  False :  Both  are  not  satisfied
print(6 <= 8)
print(6 <= 6)
print(6 <= 4)
print(9 != 7)
print(6 == 8)
print(True  >  False)
print(3 + 4j == 3 + 4j)
print(3 + 4j == 5 + 6j)
print(3 + 4j != 5 + 6j)
print(10 == 10.0)
#print(3 + 4j >  3 + 4j)#error
print()
#  Find  outputs  (Home  work)
print('Rama'   >  'Rajesh')  #   True :  'm' > 'j'
print('Rama'  <  'Sita') #  True : 'R' < 'S'
print('Hyd'  ==  'Hyd')
print('Rama'  <=   'Ramana')
print('Rama  Rao'  >=  'Rama')
print('Hyd'  != 'Sec')
print('HYD'  <   'hyd')
print()
# Chaining  relational  opeartors  (Home work)
print(10 < 20 < 30)  #   True
print(10 >= 20 < 30)  #   False : 10  is  not  >= 20
print(10 < 20 > 30)
print(1 < 2 < 3 < 4)
print(1 < 2 > 3 > 1)
print(4 > 3 >= 3 > 2)
print()
#  or  operator  demo program
print(True  or  False) #  True
print(False  or  True) #   True
print(True  or  True) #  True
print(False  or   False)   #  False
print(10  or  20)#  10
print(0   or  20)  #  20
print(-25  or  0)
print(''  or  35)
print(6j  or  'Hyd')
print(0.0  or  3 + 4j)
print('Hyd'   or   10.8)
print()
# not  operator  demo  program
print(not  True) #   False
print(not  False) #  True
print(not  25)
print(not  0)
print(not  'Hyd')
print(not  '')
print(not  -10)
print(not  not  'Hyd')
print()
#  Find   outputs (Home work)
i = 10
i = not  i > 14
print(i)
print(not(6 < 4  or  9 >= 5  and  6 != 6))