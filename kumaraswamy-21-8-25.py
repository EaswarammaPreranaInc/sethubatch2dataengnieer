'''
# Find  outputs   (Home  work)
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a)          # (25, 10.8, (3+4j), 'Hyd', True, None, 'Hyd', 25)
print(type(a))    # <class 'tuple'>
a[3] = 'Sec'      # TypeError: 'tuple' object does not support item assignment
a[3 : 6] = 60 , 70 , 80   # cmd Not executed (program stops at above error)

#  Find  outputs
a = (1,2,3)
b = (4,5,6)
print(a , id(a)) # (1,2,3) address of a
a += b # a = a + b
print(a , id(a)) # (1,2,3,4,5,6) new address of a 


#  Find  outputs
a = (1,2,3)
b = (4,5,6)
print(a , id(a))      # (1, 2, 3)  id1
a = a + b
print(a , id(a))      # (1, 2, 3, 4, 5, 6)  id2   (different from id1)


#  What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)
a = input('Enter  Tuple  :  ') # (10 , 20 , 30 , 40)
print(a) # (10 , 20 , 30 , 40)
print(type(a)) # <class 'str'>
b = eval(a)
print(b) # (10 , 20 , 30 , 40)
print(type(b)) # <class 'tuple'>
print(len(b)) # 4

# Find  outputs  (Home  work)
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70
print(a) # (10 , [70 , 30 , 40] , 50 , 60)

a[1] = [80 , 90 , 100]
print(a) # Error becoz tuple is immutable


# Find  outputs  (Home  work)
a = [10 , (20 , 30 , 40) , 50 , 60]
a[1][0] = 70
print(a) # Error
a[1] = [80 , 90]
print(a) # [10 , [80 , 90] , 50 , 60]

# Find  outputs   (Home  work)
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x) # (25,10.8,'Hyd',True)
print(type(x))#<class 'tuple'>

# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a)#25
print(b)#10.8
print(c)'Hyd'
print(d)True
p , q , r =  x#error becoz of excess elements
a , b , c , d  , e = x # error becoz of few elements


# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a) # 25
print(b) # [10.8,'Hyd']
print(c) # True


# Find  outputs   (Home  work)
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl
print(a) # 25
print(b) #10.8
print(c) # []
print(d)# Hyd
print(e)# True

# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x
print(a) # 25
print(b)#10.8
print(_)#3+4j
print(d)#True
print(_)#3+4j


# tuple()  function  demo  program   (Home  work)
a = range(100 , 150 , 10)
b = tuple(a)
print(b)#(100,110,120,130,140)
print(type(b))#<class 'tuple'>
c = [10 , 20 , 15, 18]
d = tuple(c)
print(d) # (10,20,15,18)
e = tuple('Vamsi')
print(e)#('V','a','m','s','i')
print(tuple(25))#error becoz of  25 is non sequence int
print(tuple())# ()


