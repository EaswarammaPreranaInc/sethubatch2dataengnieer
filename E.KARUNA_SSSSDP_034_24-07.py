# eval()  function  demo  program
print(eval('25'))#25
print(eval('10.8'))#10.8
print(eval('False'))#False
print(eval('3+4j'))#(3+4j)
#print(eval('Hyd'))#Error
print(eval("    'Hyd'   "))#Hyd
print(eval('3 + 4 * 5'))#23
print(eval('[10 , 20 , 15 , 18]'))#[10,20,15,18]
print(eval('{10,20,15,18,20,12,18}'))#{10,20,15,18,12}
print(eval('(10 , 20 , 30)'))#(10,20,30)
print(eval("{10 : 'Hyd' , 10 : 'Sec'}"))#{10,'sec'}
#print(eval(4 + 5))
print()
#  Tricky  program
print(eval("    'hyd'   "))#hyd
hyd = 'Sec'
print(eval('hyd'))#sec
sec = '25'
print(eval('sec'))#25
print(eval(sec))#25
cyb = 10.8
print(eval('cyb'))#10.8
#print(eval(cyb))#error
print()
#  Tricky  program
print(eval('print("Hyd")'))#Hyd<nextline>None
print()
print(bool('False'))#True
print(eval('False'))#False
print(bool(''))#false
print(eval('  ""  '))#Empty string
#print(eval(''))#Error
print(eval('  " "   '))#Empty string
#print(eval(''))#Error
print()
# What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  '))#contverts into appropriate object.
print(type(x))#class on appropriate.
print(x)#prints the value of x.
print ()
# What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ')
print(len(a))
print(a)
b = eval(input('Enter   any  string  : '))
print(len(b))#non sequences are not permitted only sequences are premitted.
print(b)
print ()
# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')   #   25 , 10.8 , Hyd
print(a , b , c , sep = '\t')#25<tab>10.8<tab>Hyd
print(a , b , c , sep = '---')#25---10.8---Hyd
print(a , b , c , sep = '\n')#25<nextline>10.8<nextline>Hyd
print(a , b , c)# 25 10.8 Hyd
#print(a,b,c,separator = ':')#Error
print()
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---')#25 10.8 hyd--- 
print(a , b , c , sep = ',,,')#25,,,10.8,,,hyd
print(a , b , c , sep = ':::' , end = '\t\t\t')#25:::10.8:::hyd
print(a,b,c)#25 10.8 hyd
print()
print('Hyd')#hyd
print()
print('Sec')#sec
print()
print('Cyb')#cyb
print()
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l,t,s)#[10,20,30,40] (10,20,30,40) {10,20,30,40}
print()
a = 25
b = '%f'  %a
print(b)#25.000000
print(type(b))#<class 'str'>
x = 10.8
y = '%d'  %x
print(y)#10
print(type(y))#<class 'str'>
m = [10 , 20 , 15 , 18]
n = '%s'  %m
print(n)#[10,20,15,18]
print(type(n))#<class 'str'>
print()
a = 10.9274
print('%8.2f'  %a)  #  <3  spaces>10.93
print('%9.1f'  %a)#<5 spaces>10.9
print('%10.3f'  %a)#<4 spaces>10.927
print('%.2f'  %a)#10.93
print('%.6f'  %a)#10.927400
print('%f' %a)#10.927400
print()
a = 'Hyd'
print('%7s'  %a)   #  <4  spaces>Hyd
print('%-7s'  %a)  #  Hyd<4   spaces>
print('%2s'  %a)   #  Hyd  and  ignores  smaller width
print('%s'  %a) # hyd
print('%s' , a)#%s hyd
#print('%s' a)#error
#print('%s' , %a)#error
print(a)#hyd
print()
a = [10 , 20 , 30 , 40]
print('%s'  %a)#[10,20,30,40]
print('%s' , a)#%s [10,20,30,40]
#print('%s'  a)#error
#print('%s' , %a)#error
#print('%l'  %a)#error
print(a)#[10,20,30,40]
print()
a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c))#25 10.927400 hyd
print('%i    %g    %s'    %(a , b , c))#25 10.9274 hyd
print('%s    %s    %s'  %(a , b , c))#25  10.9274 hyd
print('%d    %g    %s'  , a , b , c)#%d    %g    %s 25 10.9274 Hyd  
#print('%d    %g      %s'   a , b , c)
#print('%d    %g    %s'  ,  %(a , b , c))
#print('%d    %g    %s'    %a%b%c)

print('%d' %a,'%f' %b,'%s' %c)#25 10.927400 hyd
