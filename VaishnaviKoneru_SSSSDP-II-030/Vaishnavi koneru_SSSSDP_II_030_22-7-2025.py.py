#  Find  outputs (Home  work)
a = {
		print('Hyd') ,
		print('Sec') ,
		print('Cyb')
	}
print(type(a))#class 'set'
print(a)# {None}
print(len(a))# 1
#  Anonymous  object  demo  program
_ = 25
print(_)#25
print(type(_))#class 'int'
a , _ , c = 10 , 20 , 30
print(a)#10
print(_)#20
print(c)#30
for  _  in  range(5):
	print(_ , 'Hello')# 0 Hello 1 Hello 2 Hello 3 Hello 4 Hello 

#  Find  outputs
a = 25
print(id(a))#reference of 25
a = 35
print(id(a))#reference is pointing to 35 and 25 is automatically deleted by PVM
# Find  outputs (Home  work)
a = 25.7
print(id(a))#reference of 25.7 
print(a)#25.7
a = 35.6
print(id(a))#reference is pointing to some other object 35.6
print(a)#35.6
b = True
print(id(b))#reference of True
b = False
print(id(b))#reference is pointing to some other object False
c = None
print(id(c))#refrence of none
c = None
print(id(c))#same refrence of none type.because none is single object
#  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a))#reference of string object Hyd
a[1] = 'e'#error because immutable object str cannot be changed
a = 'Sec'
print(id(a))#same reference of string object Sec and Hyd is deleted
b = (10 , 20 , 15 , 18)
print(id(b))#reference of object tuple
b[2] = 19 #error because tuple is fixed and immutable
b = (30 , 40 , 35 , 32)
print(id(b))#refrence of another object tuple
c = range(5)
print(id(c))#refrence of object range
c[3] = 10#error because range is immutable cannot be changed
c = range(5)
print(id(c))#refrence of new range object
# Find  outputs  (Home  work)
a = 25
b = 25
print(a  is  b) #True because is keyword checks references
c = 'Hyd'
d = 'Hyd'
print(c  is  d) #True because is keyword checks references and they points to the same object.
e = False
f = False
print(e  is  f) #True beacuse immutbale object False
g = range(10)
h = range(10)
print(g  is  h) #false because range different ranges are created
#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b) #false because different lists are created and list is mutable
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d)#false because different sets are created and set is mutable
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f) #true because tuple is immutable once created cannot be changed
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h)#false because set is mutable and different objects are created 
# Find outputs (Home work)
print(10 + 20)#prints 30
print(10.8 + 20.6)#31.4
print(3 + 4j + 5 + 6j)#(8+10j)
print(True + False)#1
print('Hyder' + 'abad')#'Hyderabad'
print('Sankar' + 'Dayal' + 'Sarma')#'SankarDayalSarma'
print('10' + '20')#1020
print([10 , 20 , 30] + [1 , 2 , 3])#[10,20,30,1,2,3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None))#(25 , 10.8 , 'Hyd',3 + 4j , True , None)
print({10 , 20} + {30 , 40}#set doesnot allow duplicates so it is not possible to conactinate set
print({10 : 'Hyd'} + {20 : 'Sec'})#error beacuse dict shuld notbe concatinated
print(range(4) + range(5))#error range objects cannot be concatinated
print(10 + '20') #error operands should be of same type
print([10 , 20 , 30] + 5)#error operands should be of same type
print([10 , 20 , 30] + (40 , 50 , 60))#error operands should be of same type
# Find outputs (Home work)
print(25 * 3)#75
print(10.8 * 25.6)#256.48
print(True * False)#0
print((3 + 4j) * (5 + 6j))#(-9+38j)
print(3 + 4j * 5 + 6j)#(3 + 26j)
print('25' * 3)#'252525'
print(3 * '25')#'252525'
print('Hyd' * 4)#'HydHydHydHyd'
print([10 , 20 , 15] * 2)#[10 , 20 , 15,10 , 20 , 15]
print((25, 10.8, 'Hyd', True) * 3)(25, 10.8, 'Hyd', True,25, 10.8, 'Hyd', True,25, 10.8, 'Hyd', True)
print([10 , 20 , 15] * 3.0)#error float object should not be used for sequence
print({10 , 20 , 15} * 2)#error because set doesnot accept duplicates
print({10 : 20 , 30 : 40} * 2)#error because dictionary keys doesnot accept duplicates
print([10] * [20])#error
#  /  operator  demo  program
print(9.0 / 2)#4.5
print(9 / 2.0)#4.5
print(9.0 / 2.0)#4.5
print(9 / 2)  #  4.5
print(10.5 / 2)#4.5
print(10 / 3)#3.33
print(10 / 2)#5.0


 #  //  operator  demo  program
print(9 // 2)  #   prev  integer  of (4.5) = 4
print(9.0 // 2)#prev  integer  of (4.5) = 4
print(9 // 2.0)#prev  integer  of (4.5) = 4
print(9.0 // 2.0)#prev  integer  of (4.5) = 4
print(10.5 // 2)#prev  integer  of (5.25) = 5
print(10 // 3)##3.33=3
print(10.0 // 3)  #    prev  integer  of  3.33 = 3.0
print(8.5 // 3)#2.0
print(18 // 4)#4
print(-18 // 4)#-4
print(-(18 // 4))#4


 # % operator demo program
print(9 % 5)#4
print(9.0 % 5)#4.0
print(9 % 5.0)#4.0
print(9.0 % 5.0)#4.0
print(10.5 % 2)  #   0.5
print(8.9 % 3)#2.9



# Find outputs
print(7 / 0)#error
print(7 // 0)#error
print(7 % 0)#error
# ** operator demo program
print(3 ** 4)#81
print(10 ** -2)#0.01
print(4 * 3 * 2)#24
print(3 + 4 * 5 - 32 / 2 ** 3)#19




#  Relational  operators  demo  program (Home  work)
print(9 >= 5)  #   True :  >  is  satisfied
print(9 >= 9)   #   True :  =  is  satisfied
print(9 >= 12)   #  False :  Both  are  not  satisfied
print(6 <= 8) #True + is satisfied
print(6 <= 6) #true = is satisfied
print(6 <= 4) #False beacuse both are not satisfied
print(9 != 7) #True 9 and 7 are different
print(6 == 8) #False because 6 and 8 are different
print(True  >  False) #True 
print(3 + 4j == 3 + 4j) #True
print(3 + 4j == 5 + 6j) #False
print(3 + 4j != 5 + 6j) #True
print(10 == 10.0) #True
print(3 + 4j >  3 + 4j) #False

#  Find  outputs  (Home  work)
print('Rama'   >  'Rajesh')  #   True :  'm' > 'j'
print('Rama'  <  'Sita') #  True : 'R' < 'S'
print('Hyd'  ==  'Hyd') # True both objects have same name
print('Rama'  <=   'Ramana') #True <space> < n
print('Rama  Rao'  >=  'Rama') #True <space> = <space>
print('Hyd'  != 'Sec') #True Hyd and Sec are different names
print('HYD'  <   'hyd') #False 


# Chaining  relational  opeartors  (Home work)
print(10 < 20 < 30)  #   True
print(10 >= 20 < 30)  #   False : 10  is  not  >= 20
print(10 < 20 > 30) #False
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
print(-25  or  0) # -25
print(''  or  35) # 35
print(6j  or  'Hyd') # 0+6j
print(0.0  or  3 + 4j) #3+4j
print('Hyd'   or   10.8) #'Hyd



# not  operator  demo  program
print(not  True) #   False
print(not  False) #  True
print(not  25) #False
print(not  0) #True
print(not  'Hyd') #False
print(not  '')#True
print(not  -10)#False
print(not  not  'Hyd')#True

#  Find   outputs (Home work)
i = 10
i = not  i > 14
print(i)#True
print(not(6 < 4  or  9 >= 5  and  6 != 6))#True