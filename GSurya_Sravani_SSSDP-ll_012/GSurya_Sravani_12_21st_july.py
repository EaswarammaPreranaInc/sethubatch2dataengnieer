# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function')# print(a)
How  to  print  dictionary  with  print()  function
print('Keys  of  dictionary')#a.keys()
How  to  print  each  key  of  dict  'a'
print('Values  of  dictionary')#a.values()
How  to  print  each  value  of  dict  'a'
print('All  the  tuples  of  dict_items   object')#a.items()
How  to  print  each  tuple  of  the  list  in  dict_items  object
print('Elements  of  each   tuple')
How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object#a.items()
print('Keys  and  values  of  dictionary')#a.items()
How  to  print  each  key  and  corresponding  value  in  dict  'a'#print(a)


#  Find  outputs (Home  work)
a = {
		print('Hyd') ,
		print('Sec') ,
		print('Cyb')
	}
print(type(a))#set class
print(a){'sec','hyd','cyb'}
print(len(a))3

#  Anonymous  object  demo  program
_ = 25
print(_)#25
print(type(_))#Anonymous  object
a , _ , c = 10 , 20 , 30
print(a)#10
print(_)#20
print(c)#30
for  _  in  range(5):
	print(_ , 'Hello')#0,hello 1,Hello 2,hello. 3,hello 4,hello

 
  #  Find  outputs
a = 25
print(id(a))#address of int onject
a = 35
print(id(a))#adreess of same int object but previous is deleted
 # Find  outputs (Home  work)
a = 25.7
print(id(a))#address of float object but previous is deleted
print(a)#25.7
a = 35.6
print(id(a))#address of float object but previous is deleted
print(a)#35.6
b = True
print(id(b))#address of bool object
b = False
print(id(b))#address of bool object but previous is deleted
c = None
print(id(c))#address of none type
c = None
print(id(c)) address of none type object


#  Find  outputs
a = 25
print(id(a))address of int object
a = 35
print(id(a))address of int object but previous object is deleted
 # Find  outputs (Home  work)
a = 25.7
print(id(a))#address of float object
print(a)#25.7
a = 35.6
print(id(a))##address of float object but previous object is deleted
print(a)# 35.6
b = True
print(id(b))#address of bool type
b = False
print(id(b))#address of bool type but previous is deleted
c = None
print(id(c))#address of none type 
c = None
print(id(c))#adress of none type but previous is deleted 
#  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a))#address of string object
a[1] = 'e'#'eyd'
a = 'Sec'
print(id(a))#address of string object
b = (10 , 20 , 15 , 18)
print(id(b))#address of tuple object
b[2] = 19
b = (30 , 40 , 35 , 32)
print(id(b))#(10 , 20 , 19, 18)
c = range(5)
print(id(c))#address of range object
c[3] = 10#error
c = range(5)
print(id(c))address of range object

# Find  outputs  (Home  work)
a = 25
b = 25
print(a  is  b)#True
c = 'Hyd'
d = 'Hyd'
print(c  is  d)#True
e = False
f = False
print(e  is  f)#True
g = range(10)
h = range(10)
print(g  is  h)#False
 #Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b)#False
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d)#False
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f)#True
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h)#False


# Find outputs (Home work)
print(10 + 20)#40
print(10.8 + 20.6)#31.4
print(3 + 4j + 5 + 6j)#error
print(True + False)#1
print('Hyder' + 'abad')#'Hyderabad'
print('Sankar' + 'Dayal' + 'Sarma')#SankarDayalSarma'
print('10' + '20')#1020 
print([10 , 20 , 30] + [1 , 2 , 3])#10 , 20 , 30 ,1 , 2 , 3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None)#(25 , 10.8 , 'Hyd',(3 + 4j) , True , None)
print((25 , 10.8 , 'Hyd')+(3 + 4j , True , None)
print({10 , 20} + {30 , 40})#error
print({10 : 'Hyd'} + {20 : 'Sec'})#error
print(range(4) + range(5))#error
print(10 + '20')#error
print([10 , 20 , 30] + 5)#error
print([10 , 20 , 30] + (40 , 50 , 60))#error
 # Find outputs (Home work)
print(25 * 3)#75
print(10.8 * 25.6)#276.48
print(True * False)#0
print((3 + 4j) * (5 + 6j))#error
print(3 + 4j * 5 + 6j)#error
print('25' * 3)#252525
print(3 * '25')#252525
print('Hyd' * 4)#hydhydhydhyd
print([10 , 20 , 15] * 2)#[10 , 20 , 15] [10 , 20 , 15]
print((25, 10.8, 'Hyd', True) * 3)#(25, 10.8, 'Hyd', True)  (25, 10.8, 'Hyd', True) (25, 10.8, 'Hyd', True) 
print([10 , 20 , 15] * 3.0)#error
print({10 , 20 , 15} * 2)#error
print({10 : 20 , 30 : 40} * 2)#error
print([10] * [20])#error



#  /  operator  demo  program
print(9.0 / 2)#4.5
print(9 / 2.0)#4.5
print(9.0 / 2.0)#4.5
print(9 / 2)  #  4.5
print(10.5 / 2)#5.25
print(10 / 3)#3.3
print(10 / 2)#5


#  //  operator  demo  program
print(9 // 2)  #   prev  integer  of (4.5) = 4
print(9.0 // 2)#4.5
print(9 // 2.0)##4.5
print(9.0 // 2.0)#4.5
print(10.5 // 2)#5.25
print(10 // 3)#3
print(10.0 // 3)  #    prev  integer  of  3.33 = 3.0
print(8.5 // 3)#2.8
print(18 // 4)#4
print(-18 // 4)#-4
print(-(18 //4))#-4


# % operator demo program
print(9 % 5)#0.45
print(9.0 % 5)#0.45
print(9 % 5.0)#0.45
print(9.0 % 5.0)#0.45
print(10.5 % 2)  #   0.5
print(8.9 % 3)#0.445

# Find outputs
print(7 / 0)#error
print(7 // 0)#error
print(7 % 0)#error


# ** operator demo program
print(3 ** 4)#81
print(10 ** -2)#0.01
print(4 ** 3 ** 2)#262144
print(3 + 4 * 5 - 32 / 2 ** 3)#-1.1





 #  Relational  operators  demo  program (Home  work)
print(9 >= 5)  #   True :  >  is  satisfied
print(9 >= 9)   #   True :  =  is  satisfied
print(9 >= 12)   #  False :  Both  are  not  satisfied
print(6 <= 8)#False
print(6 <= 6)#True
print(6 <= 4)#False
print(9 != 7)#True
print(6 == 8)#False
print(True  >  False)#True
print(3 + 4j == 3 + 4j)#true
print(3 + 4j == 5 + 6j)#False
print(3 + 4j != 5 + 6j)#True
print(10 == 10.0)#True
print(3 + 4j >  3 + 4j)#error


#  Find  outputs  (Home  work)
print('Rama'   >  'Rajesh')  #   True :  'm' > 'j'
print('Rama'  <  'Sita') #  True : 'R' < 'S'
print('Hyd'  ==  'Hyd')#True
print('Rama'  <=   'Ramana')#False
print('Rama  Rao'  >=  'Rama')#True
print('Hyd'  != 'Sec')#True
print('HYD'  <   'hyd')#true


     

'''
# Chaining  relational  opeartors  (Home work)
print(10 < 20 < 30)  #   True
print(10 >= 20 < 30)  #   False : 10  is  not  >= 20
print(10 < 20 > 30)#False
print(1 < 2 < 3 < 4)#True
print(1 < 2 > 3 > 1)#False
print(4 > 3 >= 3 > 2)#True



#  or  operator  demo program
print(True  or  False) #  True
print(False  or  True) #   True
print(True  or  True) #  True
print(False  or   False)   #  False
print(10  or  20)#  10
print(0   or  20)  #  20
print(-25  or  0)#-25
print(''  or  35)#''
print(6j  or  'Hyd')#6j
print(0.0  or  3 + 4j)#3+4j
print('Hyd'   or   10.8)#'hyd'

# not  operator  demo  program
print(not  True) #   False
print(not  False) #  True
print(not  25)##False
print(not  0)#True
print(not  'Hyd')#False
print(not  '')#True
print(not  -10)#False
print(not  not 'Hyd')#True

  

 #  Find   outputs (Home work)
i = 10
i = not  i > 14
print(i)#True
print(not(6 < 4  or  9 >= 5  and  6 != 6))#True