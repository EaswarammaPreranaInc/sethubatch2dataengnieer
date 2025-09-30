#Range Function

#  Find  outputs    (Home  work)
a = range(10 , 50 , 5)         #Object  contains  elements  from  10 to  49  in  steps  of  5
print(type(a))                 #<class   'range'>
print(a)                       #range(10 , 50 , 5)
print(*a)                      #Unpacks  object  'a'  to elements  i.e.  10<space>15<space>20<space>25<space>30<space>35<space>40<space>45
print(id(a))                   #Address of  range object
print(len(a))                  #8
print(*a[2 : 7] , sep = ' , ') #Elements  of  object  'a'  from  indexes   2 to 6  in steps  of  1   i.e.  20  ,  25  , 30  ,  35  ,  40
print(*a[ : : -1])             #a[-1 :  -9 : -1]   --->Elements of object 'a' from indexes -1 to -8 in steps of -1 i.e. 45<sp>40<sp>..10
#a[4] = 32                     #TypeError: 'range' object does not support item assignment, it  is  immutable
#print(a * 2)                  #TypeError: unsupported operand type(s) for *: 'range', range object can'nt be repeated as duplicate elements are not permitted

#  Find  outputs  (Home  work)
a = range(10 , 20)        #range(10 , 20 , 1)  --->   Object contains  elements  from  10  to  19  in steps  of  1
print(*a , sep = ',')     #10 , 11 , 12 , ....  19
b = range(5)              #range(0 , 5 ,  1)   --->   Object contains  elements  from  0  to  4  in steps  of  1
print(*b)                 #0 <space>    1  <space>  2  <space>  3  <space> 4
c = range(10 , 1 , -1)    #Object contains  elements  from  10  to  2  in steps  of  -1
print(*c , sep = '...')   #10  ...  9  ...  8  ...   ....   2
d = range(-10 , 0)        #range(-10 , 0 , 1)  --->   Object contains  elements  from  -10  to   -1   in steps  of  1
print(*d)                 #-10  <space>   -9  <space>  -8  <space>  ...  -1
e = range(-10)            #range(0 ,  -10 , 1)  --->   Empty  object  due  to  0 >=  -10
print(*e)                 #Unpacks  empty  object   i.e.  Nothing
f = range(2 , 2)          #range(2 , 2 , 1)  ---> Empty  object  due  to  2 >=  2
print(*f)                 #Unpacks  empty  object   i.e.  Nothing
#g = range(10 , 11 , 0.1) #TypeError: 'float' object cannot be interpreted as an integer, range object can not hold float elements
h = range('A' , 'F')     #TypeError: 'str' object cannot be interpreted as an integer, range object can not hold str elements

#  Find  outputs  (Home  work)
r = range(10 ,  17 , 3)  #Object  contains  elements  from  10  to  16  in  steps  of  3
a , b , c = r            #Unpacks  range  object  to  3  elements
print(a , b , c)         #10 <space>  13  <space>  16
r = range(3)             #Object  contains  elements  from   0   to  2   in  steps  of  1
#x , y = r               #ValueError: too many values to unpack (expected 2),  Excess  elements  in  range  object
#p , q  , r , s = r      #ValueError: not enough values to unpack (expected 4, got 3), Few  elements  in range  object
#a , b , c = *r          #SyntaxError: can't use starred expression here
m = r                    #Ref  'm'  points  to  object  'r'
print(id(r))             #Address  of  range  object  'm'
print(id(m))             #Same  address