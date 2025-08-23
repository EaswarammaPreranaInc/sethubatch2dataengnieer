# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)           #{'Hyd', 25, True, 10.8} order may vary
a , b , c , d = s
print(a)           #25
print(b)           #10.8
print(c)           #Hyd
print(d)           #True


 # Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)     #{'Hyd',  25,  True,  10.8 }
a , *b = s   
print(a)    #Hyd
print(b)    #[25, True, 10.8]
print(type(b)) #class list


# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)        #{25, 10.8, 'Hyd', True}
a , *b , c = s  
print(a)        #25
print(b)        #[10.8, 'Hyd']
print(c)        #True


# Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s)        #{10, 20}
x , y = s       #
print(x)        #10
print(y)        #20


# set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a)
print(b)        #{130, 100, 140, 110, 150, 120}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d)        #{10, 12, 15, 18, 50, 20}
e = set('Rama  rAo')
print(e)        #{' ', 'o', 'R', 'r', 'm', 'A', 'a'}
print(set([25,20]))  #error
print(set())         #set()


'''
set()  function
-----------------
1) What  does  set(sequence)  do ?  ---> Converts  sequence  to  set

2) What  does  set(No-args)  do ?  --->  Returns  an  empty  set

3) How  many  arguments  can  set()  function  take ?  ---> Zero  (or) One  but  not  more  than  one

4) Is  set(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence
'''