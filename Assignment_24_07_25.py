#Eval Statement

print(eval("25"))#25
print(eval('10.8'))#10.8
print(eval('False'))#False
print(eval('3+4j'))#(3+4j)
print(eval('Hyd'))#NameError: name 'Hyd' is not defined
print(eval(" 'Hyd' "))#Hyd
print(eval("3+4*5"))#23
print(eval("[10,20,15,18]"))#[10,20,25,18]
print(eval("{10,20,15,18,20,12,18}"))#{18,20,10,12,15}
print(eval("(10,20,30)"))#(10,20,30)
print(eval("{10:'Hyd',10:'Sec'}"))#{10:'Sec'}
print(eval(4+5))#TypeError: eval() arg 1 must be a string, bytes or code object

print(eval(" 'hyd' "))#hyd
hyd='Sec'
print(eval('hyd'))#sec
sec='25'
print(eval('sec'))#25
print(eval(sec))#25
cyb=10.8
print(eval('cyb'))#10.8
print(eval(cyb))#TypeError: eval() arg 1 must be a string, bytes or code object
print(eval('print("Hyd")'))#Hyd
                        #None

x=eval(input('Enter any String: '))
print(type(x))#Enter any String: '10'<class 'str'>
print(x)#10

a=input("enter anay string: ")
print(len(a))#enter anay string: python 6
print(a)#python
b=eval(input('Enter any string:'))
print(len(b))#enter anay string: 'python' 6
print(b)#python

a,b,c=25,10.8,'Hyd'
print(a,b,c,sep=',')#25,10.8,Hyd
print(a,b,c,sep='\t')#25	10.8	Hyd
print(a,b,c,sep='')#25_10.8_Hyd
print(a,b,c,sep='\n')#25
                     #10.8
                     #Hyd
print(a,b,c)#25 10.8 Hyd
print(a,b,c,sep=':')#25 10.8 Hyd

a,b,c=25,10.8,'Hyd'
print(a,b,c,end='')#25 10.8 Hyd__25,,,10.8,,,Hyd
print(a,b,c,sep=',,,')
print(a,b,c,sep=':::',end='\t\t\t')#25:::10.8:::Hyd			25 10.8 Hyd
print(a,b,c)

l=[10,20,30,40]
t=(10,20,30,400)
s={10,20,30,40}
print(l,t,s)#[10, 20, 30, 40] (10, 20, 30, 400) {40, 10, 20, 30}

a=25
b='%f' %a
print(b)#25.000000
print(type(b))#<class 'str'>
x=10.8
y='%d' %x
print(y)#10
print(type(y))#<class 'str'>
m=[10,20,15,18]
n='%s' %m
print(n)#[10, 20, 15, 18]
print(type(n))#<class 'str'>

a=10.9247
print('%8.2f' %a)#<space><space><space>10.92
print('%9.1f' %a)#<space><space><space><space><space>10.9
print('%10.3f' %a)#<space><space><space><space>10.925
print('%.2f' %a)#10.92
print('%.6f' %a)#10.924700
print('%f' %a)#10.924700

a='Hyd'
print('%7s' %a)#<4 spaces>Hyd
print('%-7s' %a)#Hyd
print('%2s' %a)#Hyd
print('%s' %a)#Hyd
print('%s', a)#%s Hyd
print('%s' a)#SyntaxError: invalid syntax. Perhaps you forgot a comma?
print('%l', %a)#SyntaxError: invalid syntax
print(a)#Hyd

a=[10,20,30,40]
print('%s' %a)#[10, 20, 30, 40]
print('%s', a)#%s [10, 20, 30, 40]
print('%s' a)#SyntaxError: invalid syntax.
print('%s', %a)#SyntaxError: invalid syntax
print('%l' %a)#ValueError: incomplete format
print(a)#[10, 20, 30, 40]

a=25
b=10.9274
c='Hyd'
print('%d %f %s' %(a,b,c))#25 10.927400 Hyd
print('%i %g %s' %(a,b,c))#25 10.9274 Hyd
print('%s %s %s' %(a,b,c))#25 10.9274 Hyd
print('%d %g %s', a,b,c)#%d %g %s 25 10.9274 Hyd
print('%d %s %s' a,b,c)#SyntaxError: invalid syntax
print('%d %g %s', %(a,b,c))#SyntaxError: invalid syntax
print('%d %g %s' %a%b%c)#TypeError: not enough arguments for format string
print('%d' %a,'%f' %b, '%s' %c)#25 10.927400 Hyd
