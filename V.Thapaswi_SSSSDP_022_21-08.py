#1)  Find  outputs   
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a)#(25, 10.8, (3+4j), 'Hyd', True, None, 'Hyd', 25)
print(type(a))#<class 'tuple'>
#a[3] = 'Sec'#Error cannot modify element
#a[3 : 6]=60,70,80#Error cannot modify element


# 2)  Find  outputs
a = (1,2,3)
b = (4,5,6)
print(a , id(a))#(1, 2, 3) ,address of a
a += b
print(a , id(a))#(1, 2, 3, 4, 5, 6),address of a



# 3) Find  outputs
a = (1,2,3)
b = (4,5,6)
print(a , id(a))#(1, 2, 3) ,address of a
a = a + b
print(a , id(a))#(1, 2, 3, 4, 5, 6),address of a

''' 
# 4) What   are  the  outputs  if  input  is (10 , 20 , 30 , 40) ?  
a = input('Enter  Tuple  :  ')
print(a)#(10 , 20 , 30 , 40)
print(type(a))#<class 'str'>
b = eval(a)
print(b)#(10, 20, 30, 40)
print(type(b))#<class 'tuple'>
print(len(b))#4
'''

# 5) Find  outputs  
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70
print(a)#(10, [70, 30, 40], 50, 60)
#a[1] = [80 , 90 , 100]#Error value cannot be modified
print(a)#(10, [70, 30, 40], 50, 60)


# 6) Find  outputs  
a = [10 , (20 , 30 , 40) , 50 , 60]
#a[1][0] = 70#Error because value cannot be modified
print(a)#[10 , (20 , 30 , 40) , 50 , 60]
a[1] = [80 , 90]
print(a)#[10, [80, 90], 50, 60]


# 7) Find  outputs  
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x)#(25, 10.8, 'Hyd', True)
print(type(x))#<class 'tuple'>


# 8) Find  outputs   
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a)#25
print(b)#10.8
print(c)#Hyd
print(d)#True
#p , q , r =  x#Error because too many values to unpack
#a , b , c , d  , e = x# Error because  not enough values to unpack


#9)  Find  outputs  
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a)#25
print(b)#[10.8, 'Hyd']
print(c)#True


#10) Find  outputs   
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl
print(a)#25
print(b)#10.8
print(c)#[]
print(d)#Hyd
print(e)#True


#11) Find  outputs   
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x
print(a)#25
print(b)#10.8
print(_)#(3+4j)
print(d)#True
print(_)#(3+4j)


#12)  tuple()  function   
a = range(100 , 150 , 10)
b = tuple(a)
print(b)#(100, 110, 120, 130, 140)
print(type(b))#<class 'tuple'>
c = [10 , 20 , 15, 18]
d = tuple(c)
print(d)#(10, 20, 15, 18)
e = tuple('Vamsi')
print(e)#('V', 'a', 'm', 's', 'i')
#print(tuple(25))#Error
print(tuple())#()
