# eval()  function  demo  program
print(eval('25'))#25
print(eval('10.8'))#10.8
print(eval('False'))#False
print(eval('3+4j'))#3+4j
print(eval('Hyd'))#Hyd
print(eval("    'Hyd'   "))#error
print(eval('3 + 4 * 5'))#23
print(eval('[10 , 20 , 15 , 18]'))#[10 , 20 , 15 , 18]
print(eval('{10,20,15,18,20,12,18}'))#{10,20,15,18,12}
print(eval('(10 , 20 , 30)'))#(10 , 20 , 30)
print(eval("{10 : 'Hyd' , 10 : 'Sec'}"))#{10 : 'Hyd' , 10 : 'Sec'}
print(eval(4 + 5))#9

#  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   "))#error
hyd = 'Sec'
print(eval('hyd'))#Sec
sec = '25'
print(eval('sec'))#25
print(eval(sec))#25
cyb = 10.8
print(eval('cyb'))#10.8
print(eval(cyb))#10.8

#  Tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")'))#Hyd

#  Find  outputs  (Home  work)
print(bool('False'))#True
print(eval('False'))#False
print(bool(''))#False
print(eval('  ""  '))#False
print(eval(''))#False
print(eval('  " "   '))#error
print(eval(' '))#" "

# What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  '))
print(type(x))#object class
print(x)#object value

# What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ')#nari
print(len(a))#4
print(a)#nari
b = eval(input('Enter   any  string  : '))#24
print(len(b))#error
print(b)#24

# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')   #   25 , 10.8 , Hyd
print(a , b , c , sep = '\t') # 25  10.8   Hyd
print(a , b , c , sep = '---')#25---10.8---Hyd
print(a , b , c , sep = '\n')#25 newline 10.8 newline Hyd
print(a , b , c)#25 , 10.8 , Hyd
print(a , b , c , separator = ':')#25 :10.8 :Hyd

# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---')#25 10.8 Hyd ---
print(a , b , c , sep = ',,,')#25,,,10.8,,,Hyd
print(a , b , c , sep = ':::' , end = '\t\t\t')#25---10.8---Hyd
print(a , b , c)#25 , 10.8 , Hyd

# Find outputs  (Home  work)
print('Hyd')#Hyd
print()#newline
print('Sec')#Sec
print()#newline
print('Cyb')#Cyb

# Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s)#[10 , 20 , 30 , 40] , (10 , 20 , 30 , 40) , {10 , 20 , 30 , 40}

a = 10.9274
print('%8.2f' % a)  #    10.93
print('%9.1f' % a)  #      10.9
print('%10.3f' % a) #    10.927
print('%.2f' % a)   # 10.93
print('%.6f' % a)   # 10.927400
print('%f' % a)     # 10.927400

a = 'Hyd'
print('%7s' % a)    #     Hyd
print('%-7s' % a)   # Hyd    
print('%2s' % a)    # Hyd
print('%s' % a)     # Hyd
print('%s' , a)     # ('%s', 'Hyd')
print('%s'  a)     # SyntaxError
print('%s' , %a)   # SyntaxError
print(a)            # Hyd

a = [10 , 20 , 30 , 40]
print('%s' % a)     # [10, 20, 30, 40]
print('%s' , a)     # ('%s', [10, 20, 30, 40])
print('%s'  a)     # SyntaxError
print('%s' , %a)   # SyntaxError
print('%l' % a)    # ValueError: unsupported format character 'l'
print(a)            # [10, 20, 30, 40]

a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s' % (a , b , c))  # 25    10.927400    Hyd
print('%i    %g    %s' % (a , b , c))  # 25    10.9274    Hyd
print('%s    %s    %s' % (a , b , c))  # 25    10.9274    Hyd
print('%d    %g    %s' , a , b , c)    # ('%d    %g    %s', 25, 10.9274, 'Hyd')
print('%d    %g      %s' a , b , c)   # SyntaxError
print('%d    %g    %s' ,  %(a , b , c)) # SyntaxError
print('%d    %g    %s' %a%b%c)        # TypeError
print('%d' % a , '%f' % b , '%s' % c)  # 25 10.927400 Hyd
