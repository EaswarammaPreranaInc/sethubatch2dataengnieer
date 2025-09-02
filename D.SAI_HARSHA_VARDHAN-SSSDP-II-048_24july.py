# eval() function demo program
print(eval('25')) #25 int
print(eval('10.8'))#10.8 float
print(eval('False'))# False bool
print(eval('3+4j'))#3+4j complex
#print(eval('Hyd'))#Name Error
print(eval(" 'Hyd' ")) # 'Hyd' 
print(eval('3 + 4 * 5')) # 23 int
print(eval('[10 , 20 , 15 , 18]'))# list [10, 20, 15, 18]
print(eval('{10,20,15,18,20,12,18}'))# set {10,15,18,20,12}
print(eval('(10 , 20 , 30)'))#tuple(10,20,30)
print(eval("{10 : 'Hyd' , 10 : 'Sec'}"))#dict {10: 'Sec'}
#print(eval(4 + 5))# error
# Tricky program
# Find outputs (Home work)
print(eval(" 'hyd' ")) # hyd
hyd = 'Sec'
print(eval('hyd'))#Sec
sec = '25'
print(eval('sec'))#25
print(eval(sec))#25
cyb = 10.8
print(eval('cyb'))#10.8
#print(eval(cyb))#error
# Tricky program
# Find output (Home work)
#print(eval('print("Hyd")'))#error
# Find outputs (Home work)
print(bool('False'))#True
print(eval('False'))#False
print(bool(''))#False
print(eval(' "" '))#blank
#print(eval(''))#error
print(eval(' " " '))#single space
#print(eval(' '))#error
# What is the advantage of eval(input()) ?
x = eval(input('Enter any input : '))#12
print(type(x))#<class 'int'>
print(x)#12
# What is a better approach to read string input ?
a = input('Enter any string : ')#Sairam
print(len(a))#6
print(a)#Sairam
b = eval(input('Enter any string : '))#'Sairam'
print(len(b))#6
print(b)#Sairam
# sep argument demo program (Home work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',') # 25 , 10.8 , Hyd
print(a , b , c , sep = '\t') # 25 10.8 Hyd
print(a , b , c , sep = '---')# 25---10.8---Hyd
print(a, b, c, sep='\n') # Output:
                         # 25
                         # 10.8
                         #Hyd
print(a , b , c)# 25 10.8 Hyd
#print(a , b , c , separator = ':')#error
# Find outputs (Home work)
print('Hyd') #Hyd
print()# blank line
print('Sec')#Sec
print()#blank line
print('Cyb')#Cyb
# Find outputs (Home work)
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s)# [10 , 20 , 30 , 40] list (10 , 20 , 30 , 40) tuple {10 , 20 , 30 , 40}set
a = 25
b = '%f' %a # 25.000000
print(b) # 25.000000
print(type(b)) # <class 'str'>
x = 10.8
y = '%d' %x # 10
print(y) # 10
print(type(y)) # <class 'str'>
m = [10, 20, 15, 18]
n = '%s' %m # [10, 20, 15, 18]
print(n) # [10, 20, 15, 18]
print(type(n)) # <class 'str'>
a = 10.9274
print('%8.2f' %a) # 10.93
print('%9.1f' %a) # 10.9
print('%10.3f' %a) # 10.927
print('%.2f' %a) # 10.93
print('%.6f' %a) # 10.927400
print('%f' %a) # 10.927400
a = 'Hyd'
print('%7s' %a) # Hyd
print('%-7s' %a) # Hyd
print('%2s' %a) # Hyd
print('%s' %a) # Hyd
print('%s' , a) # ('%s', 'Hyd')
#print('%s' a) # SyntaxError: invalid syntax
#print('%s' , %a) # SyntaxError: invalid syntax
print(a) # Hyd
a = [10, 20, 30, 40]
print('%s' %a) # [10, 20, 30, 40]
print('%s' , a) # ('%s', [10, 20, 30, 40])
#print('%s' a) # SyntaxError: invalid syntax
#print('%s' , %a) # SyntaxError: invalid syntax
#print('%l' %a) # ValueError: unsupported format character 'l'
print(a) # [10, 20, 30, 40]
a = 25
b = 10.9274
c = 'Hyd'
print('%d %f %s' %(a , b , c)) # 25 10.927400 Hyd
print('%i %g %s' %(a , b , c)) # 25 10.9274 Hyd
print('%s %s %s' %(a , b , c)) # 25 10.9274 Hyd
print('%d %g %s' , a , b , c) # ('%d %g %s', 25, 10.9274, 'Hyd')
#print('%d %g %s' a , b , c) # SyntaxError: invalid syntax
#print('%d %g %s' , %(a , b , c)) # SyntaxError: invalid syntax
#print('%d %g %s' %a%b%c) # TypeError: not enough arguments for format string
print('%d' %a , '%f' %b , '%s' %c) # 25 10.927400 Hyd
