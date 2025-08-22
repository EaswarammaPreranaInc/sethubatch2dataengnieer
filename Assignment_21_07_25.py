      
#Accessing keys and values
a={10:'Ramesh',20:'Kiran',15:'Amar',18:'Sita'}
print(a)#{10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18: 'Sita'}
print(a.keys())#dict_keys([10, 20, 15, 18])
print(a.values())#dict_values(['Ramesh', 'Kiran', 'Amar', 'Sita'])
print(a.items())#dict_items([(10, 'Ramesh'), (20, 'Kiran'), (15, 'Amar'), (18, 'Sita')])
      

a={
    print('Hyd'),#Hyd
    print('sec'),#sec
    print('cyb')#cyb
  }
print(type(a))#<class 'set'>
print(a)#{None}
print(len(a))#1
      
_=25
print(_)#25
print(type(_))#<class 'int'>
a,_,c=10,20,30
print(a)#10
print(_)#20
print(c)#30
for _ in range(5):
    print(_,'Hello')#0 Hello
                    #1 Hello
                    #2 Hello
                    #3 Hello
                    #4 Hello

#Reusable and non resuable objects 
a=25
print(id(a))#137405425673672
a=35
print(id(a))#137405425673992
print(a)#35

a=25.7
print(id(a))#132664455809168
print(a)#25.7
print(type(a))#<class 'float'>
a=35.6
print(id(a))#132664455818864
print(a)#35.6
b=True
print(id(b))#132664467449280
b=False
print(id(b))#132664467448832
print(b)#False
c=None
print(id(c))#132664467414112
c=None
print(id(c))#132664467414112      

a='Hyd'
print(id(a))#139572569840624
a[1]='e'#TypeError: 'str' object does not support item assignment
a='Sec'
print(id(a))#136002770017792
b=(10,20,15,18)
print(id(b))#136002770044144
b[2]=19#TypeError: 'tuple' object does not support item assignment
b=(30,40,35,32)
print(id(b))#135155044828560
c=range(5)
print(id(c))#135155044801712
c[3]=10#TypeError: 'range' object does not support item assignment
c=range(5)
print(id(c))#137386893647120

a=25
b=25
print(a is b)#True
c='Hyd'
d="Hyd"
print(c is d)#True
e=False
f=False
print(e is f)#True
g=range(10)
h=range(10)
print(g is h)#False

a=[10,20,15,18]
b=[10,20,15,18]
print(a is b)#False
c={10:20,30:40}
d={10:20,30:40}
print(c is d)#False
e=(10,20,15,18)
f=(10,20,15,18)
print(e is f)#True
g={10,20,15,18}
h={10,20,15,18}
print(g is h)#False
#Arithmetic Operators     
print(10+20)#30
print(10.8+20.6)#31.400000000000002
print(3+4j+5+6j)#(8+10j)
print(True+False)#1
print("Hyder"+'abad')#Hyderabad
print('Sankar'+'Dayal'+'Sarma')#SankarDayalSarma
print('10'+'20')#1020
print([10,20,30]+[1,2,3])#[10, 20, 30, 1, 2, 3]
print((25,10.8,"hyd")+(3+4j,True,None))#(25, 10.8, 'hyd', (3+4j), True, None)
print({10,20}+{30,40})#TypeError: unsupported operand type(s) for +: 'set' and 'set'

print({10:"Hyd"},{20:"Sec"})#{10: 'Hyd'} {20: 'Sec'}
print(range(4)+range(5))#TypeError: unsupported operand type(s) for +: 'range' and 'range'
print(10+"20")#TypeError: unsupported operand type(s) for +: 'int' and 'str'
print([10,20,30]+5)#TypeError: can only concatenate list (not "int") to list
print([10,20,30]+(40,50,60))#TypeError: can only concatenate list (not "tuple") to list


print(25 * 3)#75
print(10.8 * 25.6)#276.48
print(True * False)#0
print((3 + 4j) * (5 + 6j))#(-9+38j)
print(3 + 4j * 5 + 6j)#(3+26j)
print('25' * 3)#252525
print(3 * '25')#252525
print('Hyd' * 4)#HydHydHydHyd
print([10 , 20 , 15] * 2)#[10,20,15,10,20,15]
print((25, 10.8, 'Hyd', True) * 3)#(25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True)
print([10 , 20 , 15] * 3.0)#TypeError: can't multiply sequence by non-int of type 'float'
print({10 , 20 , 15} * 2)#TypeError: unsupported operand type(s) for *: 'set' and 'int'
print({10 : 20 , 30 : 40} * 2)#TypeError: unsupported operand type(s) for *: 'dict' and 'int'
print([10] * [20])#SyntaxError: invalid non-printable character U+00A0

print(25 * 3)#75
print(10.8 * 25.6)#276.48
print(True * False)#0
print((3 + 4j) * (5 + 6j))#(-9+38j)
print(3 + 4j * 5 + 6j)#(3+26j)
print('25' * 3)#252525
print(3 * '25')#252525
print('Hyd' * 4)#HydHydHydHyd
print([10 , 20 , 15] * 2)#[10,20,15,10,20,15]
print((25, 10.8, 'Hyd', True) * 3)#(25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True)
print([10 , 20 , 15] * 3.0)#TypeError: can't multiply sequence by non-int of type 'float'
print({10 , 20 , 15} * 2)#TypeError: unsupported operand type(s) for *: 'set' and 'int'
print({10 : 20 , 30 : 40} * 2)#TypeError: unsupported operand type(s) for *: 'dict' and 'int'
print([10] * [20])#SyntaxError: invalid non-printable character U+00A0

print(9.0 / 2)#4.5
print(9 / 2.0)#4.5
print(9.0 / 2.0)#4.5
print(9 / 2)  #  4.5
print(10.5 / 2)#5.25
print(10 / 3)#3.33333
print(10 / 2)#5.0

print(9 // 2)  #   prev  integer  of (4.5) = 4
print(9.0 // 2)#4.0
print(9 // 2.0)#4.0
print(9.0 // 2.0)#4.0
print(10.5 // 2)#5.0
print(10 // 3)#3
print(10.0 // 3)  #    prev  integer  of  3.33 = 3.0
print(8.5 // 3)#2.0
print(18 // 4)#4
print(-18 // 4)#-5
print(-(18 // 4))#-4

print(9 % 5)#4
print(9.0 % 5)#4.0
print(9 % 5.0)#4.0
print(9.0 % 5.0)#4.0
print(10.5 % 2)  #   0.5
print(8.9 % 3)#2.9000000000000004

print(7 / 0)#ZeroDivisionError: division by zero
print(7 // 0)#ZeroDivisionError: integer division or modulo by zero
print(7 % 0)#SyntaxError: invalid non-printable character U+00A0
print(3 ** 4)#81
print(10 ** -2)#0.01
print(4 ** 3 ** 2)#262144
print(3 + 4 * 5 - 32 / 2 ** 3)#19.0
      
#Comparison Operators
print(9 >= 5)  #   True :  >  is  satisfied
print(9 >= 9)   #   True :  =  is  satisfied
print(9 >= 12)   #  False :  Both  are  not  satisfied
print(6 <= 8)#True
print(6 <= 6)#True
print(6 <= 4)#False
print(9 != 7)#True
print(6 == 8)#False
print(True  >  False)#True
print(3 + 4j == 3 + 4j)#True
print(3 + 4j == 5 + 6j)#False
print(3 + 4j != 5 + 6j)#True
print(10 == 10.0)#True
print(3 + 4j >  3 + 4j)#TypeError: '>' not supported between instances of 'complex' and 'complex'

print('Rama'   >  'Rajesh')  #   True :  'm' > 'j'
print('Rama'  <  'Sita') #  True : 'R' < 'S'
print('Hyd'  ==  'Hyd')#True
print('Rama'  <=   'Ramana')#True
print('Rama  Rao'  >=  'Rama')#True
print('Hyd'  != 'Sec')#True
print('HYD'  <   'hyd')#True

print(10 < 20 < 30)  #   True
print(10 >= 20 < 30)  #   False : 10  is  not  >= 20
print(10 < 20 > 30)#False
print(1 < 2 < 3 < 4)#False
print(1 < 2 > 3 > 1)#False
print(4 > 3 >= 3 > 2)#SyntaxError: invalid non-printable character U+00A0

#Logical Operators
print(True  or  False) #  True
print(False  or  True) #   True
print(True  or  True) #  True
print(False  or   False)   #  False
print(10  or  20)#  10
print(0   or  20)  #  20
print(-25  or  0)#-25
print(''  or  35)#35
print(6j  or  'Hyd')#6j
print(0.0  or  3 + 4j)#(3+4j)
print('Hyd'   or   10.8)#Hyd

print(not  True) #   False
print(not  False) #  True
print(not  25)#False
print(not  0)#True
print(not  'Hyd')#False
print(not  '')#True
print(not  -10)#False
print(not  not  'Hyd')#True

i = 10
i = not  i > 14
print(i)#True
print(not(6 < 4  or  9 >= 5  and  6 != 6))#SyntaxError: invalid non-printable character U+00A0

