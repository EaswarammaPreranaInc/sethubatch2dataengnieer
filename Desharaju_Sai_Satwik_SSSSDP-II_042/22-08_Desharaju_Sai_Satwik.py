a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
try:
    i = a.index(15)
    while True:
        print('15 is found at index : ' , i)
        i = a.index(15 , i + 1)
except:
    print(F'15  is  found  {a.count(15)}  times')


a  =  10 ,  20 ,  30 ,   40 ,  50
a[2] = 35  # error
print(a)
print(id(a))
# correct way
a = a[:2] + (35,) + a[3:]
print(a)
print(id(a))


a  = 10 , 20 , 30 , 40 , 50
a.remove(30)  # error
del a[2]  # error
a.pop(2)  # error
print(a)
print(id(a))
# correct way
a = a[:2] + a[3:]
print(a)
print(id(a))


a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a)
print(type(a))
print(len(a))
print(a[0])
print(a[1])
print(a[2])
print(a[0][1])
print(a[1][2])
print(a[2][3])


a = ((10 , 20 , 30),)
print(a[0])
print(*a)
print(a[0][0])
print(a[0][1])
print(a[0][2])
b = ((),)
print(b[0])
print(*b)


a = ((10 , 20 , 30))
print(a)  # (10, 20, 30)
print(*a)  # 10 20 30
b = (())
print(b)  # ()
print(*b)  # nothing


# Suppose input: {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')  # {10 , 20 , 15 , 18 , 20 , 12 , 18}
print(a)  # {10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(a))  # <class 'str'>
b = eval(a)
print(b)  # {10, 12, 15, 18, 20}
print(type(b))  # <class 'set'>


print({(10 , 20 , 30)})
print({[10 , 20 , 30]})  # error
print({{10 , 20 , 30}})  # error
print({{}})  # error


a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a)
print('Iterate  elements  of  set  with  for  loop')
for i in a:
    print(i)


a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s)  # {'Hyd', 25, 1}
print(len(s))  # 3
print(type(s))  # <class 'set'>


s = {'Hyd', 25, True, 10.8 }
print(s)
a , b , c , d = s
print(a)
print(b)
print(c)
print(d)


s = {'Hyd', 25, True, 10.8 }
print(s)
a , *b = s
print(a)
print(b)
print(type(b))


s = {'Hyd', 25, True, 10.8 }
print(s)
a , *b , c = s
print(a)
print(b)
print(c)


s = {20 , 10 , 20 , 10}
print(s)  # {10, 20}
x , y = s
print(x)
print(y)
