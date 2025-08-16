#  Find  outputs
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a . keys())    #dict_keys([10 , 20 , 15 , 18])
print(a . values())  #dict_values(['Ramesh' , 'Kiran' , 'Amar' , 'Sita'])
print(a .  items())  #dict_items([(10 , 'Ramesh') , (20 , 'Kiran') , (15 , 'Amar') , (18 , 'Sita')])
print(a)             #{10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}



#Immutable vs Mutable Objects


#  Find  outputs
a = 25        #Ref  'a'  points  to  object  25
print(id(a))  #Address  of object  25  (may be   1000)
a = 35        #Modifies   ref  'a'   to  object   35
print(id(a))  #Address  of object  35  (may be   2000)


# Find  outputs (Home  work)
a = 25.7        #Ref  'a'  points  to  object  25.7
print(id(a))    #Address  of  object   25.7  (may  be  1000)
print(a)        #25.7
a = 35.6        #Modifies  ref  'a'   to   object  35.6
print(id(a))    #Address  of  object  35.6   (may  be  2000)
print(a)        #35.6
b = True        #Ref  'b'  points  to  object  True
print(id(b))    #Address  of  object   True   (may  be  3000)
b = False       #Modifies  ref  'b'  to   object  False
print(id(b))    #Address  of  object  False   (may  be  4000)
c = None        #Ref  'c'  points  to  object  None
print(id(c))    #Address  of  object   None  (may  be  5000)
c = None        #Nothing  is  modified  :  'c'  already  points  to  None
print(id(c))    #Address  of  object   None  (5000)

# Find  outputs  (Home  work)
a = 'Hyd'                #Ref 'a'  points  to  object  'Hyd'
print(id(a))             #Address of object  'Hyd'
#a[1] = 'e'              #TypeError: 'str' object does not support item assignment, char of string can't be modified as str is immutable
a = 'Sec'                #Modifies  ref  'a'  to  object  'Sec'
print(id(a))             #Address of object  'Sec'
b = (10 , 20 , 15 , 18)  #Ref 'b'  points  to   tuple
print(id(b))             #Address of   tuple
#b[2] = 19               #TypeError: 'tuple' object does not support item assignment, element of tuple can't be modified as tuple is immutable
b = (30 , 40 , 35 , 32)  #Modifies  ref   'b'  to  another  tuple
print(id(b))             #Address of   2nd  tuple
c = range(5)             #Ref 'c'  points  to   1st   range  object
print(id(c))             #Address  of  1st  range  object
#c[3] = 10               #TypeError: 'range' object does not support item assignment, element of tuple can't be modified as tuple is immutable
c = range(5)             #Ref  'c'  is  modified  to   2nd  range  object
print(id(c))             #Address  of  2nd  range  object


# Find  outputs  (Home  work)
a = 25           #Ref  'a'  points  to  object  25
b = 25           #Ref  'b'  points  to  same  object   25  as  int  object  is  immutable  and  reusable
print(a  is  b)  #True  :  References  'a'  and  'b'  point  to  same  object  25
c = 'Hyd'        #Ref  'c'  points  to  object  'Hyd'
d = 'Hyd'        #Ref  'd'  points  to  same  object   'Hyd'  as   str  object  is  immutable  and  reusable
print(c  is  d)  #True :  References  'c'  and  'd'  point  to  same  object  'Hyd'
e = False        #Ref  'e'  points  to  object   False
f = False        #Ref  'f'  points  to  same  object  False as  bool  object  is  immutable  and  reusable
print(e  is  f)  #True :  References  'e'  and  'f'  point  to  same  object   False
g = range(10)    #Ref  'g'  points  to  range  object
h = range(10)    #Ref  'h'  points to different range object as range object is immutable but not reusable
print(g  is  h)  #False   :  References  'g'  and  'h'  point  to  different  range    objects

#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]   #Ref   'a'  points  to  list
b = [10 , 20 , 15 , 18]   #Ref 'b'  points  to  another  list  as   list  is  mutable  and  not  reusable
print(a  is  b)           #False  :  References  'a'  and  'b'  point  to  different  lists
c =  {10 : 20, 30 : 40}   #Ref   'c'  points  to   dict
d =  {10 : 20, 30 : 40}   #Ref 'd'  points  to  another  dictionary  as   dict  is  mutable  and  not  reusable
print(c  is  d)           #False :  References  'c'  and  'd'  point  to  different  dictionaries
e = (10 , 20 , 15 , 18)   #Ref   'e'  points  to   tuple
f = (10 , 20 , 15 , 18)   #Ref 'f'  points  to  same   tuple  as  tuple  is  immutable  and  reusable
print(e  is  f)           #True :  References  'e'  and  'f'  point  to  same  tuple
g = {10 , 20 , 15 , 18}   #Ref   'g'  points  to   a   set
h = {10 , 20 , 15 , 18}   #Ref 'h'  points  to  another  set   as   set  is  mutable  and  not  reusable
print(g  is  h)           #False  :  References  'g'  and   'h'   point  to  different  sets







#Arithmetic Operators


# Find outputs (Home work)
print(10 + 20)                                       #30
print(10.8 + 20.6)                                   #31.4
print(3 + 4j + 5 + 6j)                               #8+10j
print(True + False)                                  #1 + 0 = 1
print('Hyder' + 'abad')                              #Hyderabad
print('Sankar' + 'Dayal' + 'Sarma')                  #SankarDayalSarma
print('10' + '20')                                   #1020
print([10 , 20 , 30] + [1 , 2 , 3])                  #[10, 20, 30, 1, 2, 3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None))  #(25, 10.8, 'Hyd', (3+4j), True, None)
#print({10 , 20} + {30 , 40})            #TypeError: unsupported operand type(s) for +: 'set' and 'set', sets can't be concatanated with +
#print({10 : 'Hyd'} + {20 : 'Sec'})      #TypeError: unsupported operand type(s) for +: 'dict' and 'dict', dicts..(same as above)
#print(range(4) + range(5))              #TypeError: unsupported operand type(s) for +: 'range' and 'range',range obj can't be concatanated
#print(10 + '20')                        #TypeError: unsupported operand type(s) for +: 'int' and 'str'
                                                    #op2 should be non-sequece as op1 is non-sequence
#print([10 , 20 , 30] + 5)               #TypeError: can only concatenate list (not "int") to list
                                                    #list  and  int  can  not  be  concatenated
#print([10 , 20 , 30] + (40 , 50 , 60))  #TypeError: can only concatenate list (not "tuple") to list,
                                                    #list  and   tuple  can  not  be  concatenated


# Find outputs (Home work)
print(25 * 3)                      #75
print(10.8 * 25.6)                 #276.48
print(True * False)                #1 * 0 = 0
print((3 + 4j) * (5 + 6j))         #15+18j+20j-24 = -9 + 38j
print(3 + 4j * 5 + 6j)             #3 + 20j + 6j = 3 + 26j
print('25' * 3)                    #252525
print(3 * '25')                    #252525
print('Hyd' * 4)                   #HydHydHydHyd
print([10 , 20 , 15] * 2)          #[10, 20, 15, 10, 20, 15]
print((25, 10.8, 'Hyd', True) * 3) #(25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True)
#print([10 , 20 , 15] * 3.0)       #TypeError: can't multiply sequence by non-int of type 'float', due to float operand 3.0
#print({10 , 20 , 15} * 2)         #TypeError: unsupported operand type(s) for *: 'set' and 'int', set can't be repeated
#print({10 : 20 , 30 : 40} * 2)    #TypeError: unsupported operand type(s) for *: 'dict' and 'int', dict can't be repeated
#print([10] * [20])                #TypeError: can't multiply sequence by non-int of type 'list', 2nd operator is non int i.e. list


#  /  operator  demo  program
print(9.0 / 2)    #4.5
print(9 / 2.0)    #4.5
print(9.0 / 2.0)  #4.5
print(9 / 2)      #4.5
print(10.5 / 2)   #5.25
print(10 / 3)     #3.3333
print(10 / 2)     #5.0
#print(10 / 0)    #ZeroDivisionError: division by zero
#division always returns a float quotient

#  //  operator  demo  program
print(9 // 2)      #Previous  integer  of  4.5 = 4
print(9.0 // 2)    #Prev  integer  of  4.5 = 4.0
print(9 // 2.0)    #Prev  integer  of  4.5 = 4.0
print(9.0 // 2.0)  #Prev  integer  of  4.5 = 4.0
print(10.5 // 2)   #Prev  integer  of  5.25 = 5.0
print(10 // 3)     #Prev  integer  of   3.333 = 3
print(10.0 // 3)   #Prev  integer  of  3.33 = 3.0
print(8.5 // 3)    #Prev  integer  of  2.8 = 2.0
print(18 // 4)     #Prev  integer  of  4.5  = 4
print(-18 // 4)    #Prev  integer  of  -4.5  = -5
print(-(18 // 4))  #-(prev  integer  of  4.5) =  -4
#print( 24.0 // 0) #ZeroDivisionError: float floor division by zero
#print( 34 // 0)   #ZeroDivisionError: integer division or modulo by zero
#divides and returns floor value, if both int then int else float

# % operator demo program
print(9 % 5)      #4
print(9.0 % 5)    #4.0
print(9 % 5.0)    #4.0
print(9.0 % 5.0)  #4.0
print(10.5 % 2)   #0.5, 2*5=10, 10.5-10=0.5
print(8.9 % 3)    #2.9, 3*2=6, 8.9-6=2.9
#return int if both int else float


# Find outputs
#print(7 / 0)   #ZeroDivisionError: division by zero
#print(7 // 0)  #ZeroDivisionError: integer division or modulo by zero
#print(7 % 0)   #ZeroDivisionError: integer modulo by zero

# ** operator demo program
print(3 ** 4)                   #3 ^ 4 = 81
print(10 ** -2)                 #10 ^ -2 = 0.01
print(4 ** 3 ** 2)              #4 ^ 3 ^ 2 = 4 ^ 9 = 262144
print(3 + 4 * 5 - 32 / 2 ** 3)  # 3 + 4*5 - 32 /8 => 3 + 20 - 32/8 => 3+20-4.0 => 23-4.0 => 19.0
#first precedence is matched then associvity(unary: right to left, binary:left to right)




#Relational Operators
#  Relational  operators  demo  program (Home  work)
print(9 >= 5)            #True : > is satisfied
print(9 >= 9)            #True : = is satisfied
print(9 >= 12)           #False : Both are not satisfied
print(6 <= 8)            #True: < is satisfied
print(6 <= 6)            #True: = is satisfied
print(6 <= 4)            #False: both not satisfied
print(9 != 7)            #True: 9 is not equal to 7
print(6 == 8)            #False
print(True  >  False)    #True: 1 is greater than 0
print(3 + 4j == 3 + 4j)  #True: real and imag are equal
print(3 + 4j == 5 + 6j)  #False: real an imag both are not equal
print(3 + 4j != 5 + 6j)  #True: real and imag both are not equal
print(10 == 10.0)        #True: both are equal
#print(3 + 4j >  3 + 4j) #TypeError: complex numbers can only be compared for == and !=


#  Find  outputs  (Home  work)
print('Rama'   >  'Rajesh')    #True :  'm' > 'j', compares first not matching char's unicodes
print('Rama'  <  'Sita')       #True : 'R' < 'S', compares first not matching char's unicodes
print('Hyd'  ==  'Hyd')        #True: all chars equal
print('Rama'  <=   'Ramana')   #True: '' < n , unicode of '' is 0
print('Rama  Rao'  >=  'Rama') #True: ' ' > '', unicode of '' is 0
print('Hyd'  != 'Sec')         #True: all chars not equal
print('HYD'  <   'hyd')        #True: unicode of uppercase are less than unicode of lowercase

#relational operators for string compare only 1(first non matching char)


# Chaining  relational  opeartors  (Home work)
print(10 < 20 < 30)    #  True :  Both  are  True
print(10 >= 20 < 30)   #  False  :  10  is  not  >= 20
print(10 < 20 > 30)    #  False  :   20  is  not  > 30
print(1 < 2 < 3 < 4)   #  True :  All conditions  are  True
print(1 < 2 > 3 > 1)   #  False  :  2  is  not  > 3
print(4 > 3 >= 3 > 2)  #  True : All conditions  are  True