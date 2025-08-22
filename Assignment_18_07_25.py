#LIST
a=[25,10.8,'Hyd',True,3+4j,None,'Hyd',25]
   
print(a)
   
[25, 10.8, 'Hyd', True, (3+4j), None, 'Hyd', 25]
print(*a)
   
25 10.8 Hyd True (3+4j) None Hyd 25
print(type(a))
   
<class 'list'>
print(id(a))
   
2705009846976
print(len(a))
   
8
a[2]='Sec'
   
print(a)
   
[25, 10.8, 'Sec', True, (3+4j), None, 'Hyd', 25]
print(a[2:5])
   
['Sec', True, (3+4j)]
print(a[::-1])
   
[25, 'Hyd', None, (3+4j), True, 'Sec', 10.8, 25]

#List Methods
a=[]
   
print(a)
   
[]
a.append(25)
   
a.append(10.8)
   
a.append('Hyd')
   
a.append(True)
   
print(a)
   
[25, 10.8, 'Hyd', True]
a.remove('Hyd')
   
print(a)
   
[25, 10.8, True]
a.remove('25')
   
ValueError: list.remove(x): x not in list
print(a)
   
[10.8, True]
      
#* Operator
a=[25,10.8,'Hyd']
print(a)#[25, 10.8, 'Hyd']
print(id(a))#139621793991104
print(a*3)#[25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a*2)#[25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a*1)#[25, 10.8, 'Hyd']
print(a*0)#[]
print(a*-1)3#[]
print(a*4.0)#TypeError: can't multiply sequence by non-int of type 'float'
a=a*3
print(a)#[25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(id(a))#139621792309696
a=[25]
print(a*a)#TypeError: can't multiply sequence by non-int of type 'list'      


a = list('Hyd')
print(a)#['H', 'y', 'd']
print(type(a))#<class 'list'>
print(len(a))#3
b = (10 , 20 , 15 , 18)
print(list(b))#[10, 20, 15, 18]
print(list(range(5)))#[0, 1, 2, 3, 4]
print(list(25))#TypeError: 'int' object is not iterable
a = [ ]
print(type(a))#[]
print(a)
print(len(a))#0
b = list()
print(b)#[]
print(len(b))#0

      
#Slicing in list
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[2 : 7])#[(3+4j), 'Hyd', True, None, 10.8]
print(list[ : : ])#[25, 10.8, (3+4j), 'Hyd', True, None, 10.8, 'Hyd']
print(list[:]) #  list[0 :  8 :  1]  --->  List  from  indexes  0  to  7  in  steps  of  1  i.e.  [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1])#['Hyd', 10.8, None, True, 'Hyd', (3+4j), 10.8, 25]
print(list[ : : 2])#[25, (3+4j), True, 10.8]
print(list[1 : : 2])#[10.8, 'Hyd', None, 'Hyd']
print(list[ : : -2]) #  list[-1 :  -9 : -2]  --->  List  from  indexes   -1  to  -8  in  steps  of   -2   i.e.  ['Hyd' , None , 'Hyd' , 10.8]
print(list[-2 : : -2])#[10.8, True, (3+4j), 25]
print(list[1 : 4])#[10.8, (3+4j), 'Hyd']
print(list[-4 : -1])#[True, None, 10.8]
print(list[3 : -3])#['Hyd', True]
print(list[2 : -5])#[(3+4j)]
print(list[-1:-5])#[]


#Iterating through list
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5]
print('x : ' , x)#x :  Hyd
print('y : ' , y)#y :  True
for  x  in  list[2:7]:
	print(x)#(3+4j)
#output      
#Hyd
#True
#None
#10.8

a = [10 , 20 , 30 , 40 , 50]
print(a , id(a))#[10, 20, 30, 40, 50] 137314123827648
a[1 : 4] = [60 , 70]
print(a , id(a))#[10, 60, 70, 50] 137314123827648
a[2: 4] = [100 , 200 ,  300]
print(a , id(a))#SyntaxError: invalid non-printable character U+00A0

#Index out of range      
a =  [25]
print(a[1])#IndexError: list index out of range
print(a[1:])#IndexError: list index out of range

#Tuple
a = (25)
b = 25,
c = 25
d = (25,)
print(type(a))#<class 'int'>
print(type(b))#<class 'tuple'>
print(type(c))#<class 'int'>
print(type(d))#<class 'tuple'>
print(a * 4)#100
print(b * 4)#(25, 25, 25, 25)
print(c * 4)#SyntaxError: invalid non-printable character U+00A0
print(d * 4)#SyntaxError: invalid non-printable character U+00A0

a = tuple('Hyd')
print(a)#('H', 'y', 'd')
print(type(a))#<class 'tuple'>
print(len(a))#3
b = [10 , 20 , 15 , 18]
print(tuple(b))#(10, 20, 15, 18)
print(tuple(range(5)))#(0, 1, 2, 3, 4)
print(tuple(25))#TypeError: 'int' object is not iterable


a = ()
print(type(a))#<class 'tuple'>
print(a)#()
print(len(a))#0
b = tuple()
print(b)#()
print(len(b))#0

a = (10 , 20 , 30)
print(a)#(10, 20, 30)
print(id(a))#138645167248256
a = a * 2
print(a)#(10, 20, 30, 10, 20, 30)
print(id(a))#138645168472704
      
#SET
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a)#{None, True, 25, 10.8, 'Hyd', (3+4j)}
print(type(a))#<class 'set'>
print(len(a))#6
print(a[2])#TypeError: 'set' object is not subscriptable
print(a[1 : 4])
a[2] = 'Sec'
print(a * 2)#SyntaxError: invalid non-printable character U+00A0
print(a * a)#SyntaxError: invalid non-printable character U+00A0      

a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a)#{False, 1, 'Hyd', ''}
print(len(a))#4
print(type(a))#<class 'set'>


a = set('Rama rAo')
print(a)#{'r', 'm', ' ', 'o', 'R', 'a', 'A'}
print(len(a))#7
print(set([10 , 20 , 15 , 20]))#{10, 20, 15}
print(set((25 , 10.8 , 'Hyd' , 10.8)))#{25, 10.8, 'Hyd'}
print(set(range(10 , 20 , 3)))#{16, 10, 19, 13}
print(set(25))#TypeError: 'int' object is not iterable
print(set([25 , 10.8 , [] , 'Hyd']))#TypeError: unhashable type: 'list'

a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a))#<class 'list'>
print(type(b))#<class 'tuple'>
print(type(c))#<class 'dict'>
print(type(d))#<class 'set'>
print(a)#[]
print(b)#()
print(c)#{}
print(d)#set()

      

a = set()
a . add(25)
a . add(10.8)
a . add('Hyd')
a . add(True)
a . add(None)
a . add('Hyd')
a . add(1)
print(a)#{None, True, 10.8, 'Hyd', 25}
print(len(a))#5
a . remove(25)
print(a)#{None, True, 10.8, 'Hyd'}
a . append(100)#AttributeError: 'set' object has no attribute 'append'
a . add(set())
a . add(())
a . add([])
print(a)#{None, True, 10.8, 'Hyd'}
a . add({})#SyntaxError: invalid non-printable character U+00A0


