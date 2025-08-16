#float obiects
a=10.8
print(a)      #a=10.8
print(id(a))  #i.e 9389383839
print(type(a))#<class'float'>
b=25
print(b)      #b=25
print(type(b))#<class'int'>
c=.689
print(c)      #c=0.689
d=3.4e^2
print(d)      #d=340
print(type(d))
e=9.62e^-2
print(e)      #0.096
print(9.8.2)  #syntax error
  

#complex objects
a=3+4j
print(a)      #a=3+4j
print(type(a))#<class'complex'>
print(id(a))  #2828223838
print(a.real) #3.0
print(a.imag) #4.0
print(type(a.real))#<class'float'>
print(type(a.imag))#<class'float'>


#complex objects
a=6j
print(a)      #a=6j
print(type(a))#<class'complex'>
print(a.real)  #0.0
print(a.imag)   #6.0
print(5+j6)   #error
print(3+4i)   #error
print(4+j)    #error
print(4+1j)   #4+1j
print(4+0j)   #4+0j

 # bool object demo program  (Home  work)
a = True
print(a)        #True
print(type(a))   #<class'bool'>
print(id(a))     #address of 'a'
b = False        
print(b)         #False
print(type(b))    #<class'bool'>
print(True + True)   #True  =1
print(True + False)  #True  =1
print(False + True)   #True  =1
print(False + False)  #False  =0
print(True + True + True)  #True  =3
print(25 + 10.8 + True)  #36.8
print(True > False)  #True
print(True)   #1  
print(False)  #0
print(true)   #error
print(false)  #error
