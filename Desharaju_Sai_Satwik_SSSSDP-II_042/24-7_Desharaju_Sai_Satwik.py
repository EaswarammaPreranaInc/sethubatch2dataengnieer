
print(eval('25'))                                     # 25
print(eval('10.8'))                                   # 10.8
print(eval('False'))                                  # False
print(eval('3+4j'))                                   # (3+4j)
print(eval('Hyd'))  #Error
print(eval("    'Hyd'   "))                           # Hyd
print(eval('3 + 4 * 5'))                              # 23
print(eval('[10 , 20 , 15 , 18]'))                    # [10, 20, 15, 18]
print(eval('{10,20,15,18,20,12,18}'))                 # {10, 12, 15, 18, 20}
print(eval('(10 , 20 , 30)'))                         # (10, 20, 30)
print(eval("{10 : 'Hyd' , 10 : 'Sec'}"))              # {10: 'Sec'}
print(eval(4 + 5))  # Error

print(eval("    'hyd'   "))                           # hyd
hyd = 'Sec'
print(eval('hyd'))                                    # Sec
sec = '25'
print(eval('sec'))                                    # 25
print(eval(sec))                                      # 25
cyb = 10.8
print(eval('cyb'))                                    # 10.8
print(eval(cyb))                                      # 10.8

print(eval('print("Hyd")'))                           # Hyd + None

print(bool('False'))                                  # True
print(eval('False'))                                  # False
print(bool(''))                                       # False
print(eval('  ""  '))                                 # ''
print(eval(''))  # Error
print(eval('  " "   '))                               # ' '
print(eval(' '))  # Error


x = eval(input('Enter any input: '))
print(type(x))#class <int>
print(x) #25

a = input('Enter any string: ')
print(len(a)) #5
print(a)#Hello
b = eval(input('Enter any string: '))
print(len(b))#5
print(b)#Hello

a, b, c = 25, 10.8, 'Hyd'
print(a, b, c, sep=',')                               # 25,10.8,Hyd
print(a, b, c, sep='\t')
print(a, b, c, sep='---')
print(a, b, c, sep='\n')
print(a, b, c)
print(a, b, c, separator=':')  #Error

a, b, c = 25, 10.8, 'Hyd'
print(a, b, c, end='---')
print(a, b, c, sep=',,,')
print(a, b, c, sep=':::', end='\t\t\t')
print(a, b, c)

print('Hyd')
print()
print('Sec')
print()
print('Cyb')
#Hyd

#Sec

#Cyb


l = [10, 20, 30, 40]
t = (10, 20, 30, 40)
s = {10, 20, 30, 40}
print(l, t, s)
#10, 20, 30, 40 10, 20, 30, 40 10, 20, 30, 40

a = 25
b = '%f' % a
print(b)                                              # '25.000000'
print(type(b))                                        # <class 'str'>
x = 10.8
y = '%d' % x
print(y)                                              # '10'
print(type(y))                                        # <class 'str'>
m = [10, 20, 15, 18]
n = '%s' % m
print(n)                                              # '[10, 20, 15, 18]'
print(type(n))                                        # <class 'str'>

# Find outputs
a = 10.9274
print('%8.2f' % a)                                    # '   10.93'
print('%9.1f' % a)                                    # '     10.9'
print('%10.3f' % a)                                   # '    10.927'
print('%.2f' % a)                                     # '10.93'
print('%.6f' % a)                                     # '10.927400'
print('%f' % a)                                       # '10.927400'

a = 'Hyd'
print('%7s' % a)                                      # '    Hyd'
print('%-7s' % a)                                     # 'Hyd    '
print('%2s' % a)                                      # 'Hyd'
print('%s' % a)                                       # 'Hyd'
print('%s', a)                                        # ('%s', 'Hyd')
# print('%s' a)  # Error
# print('%s' , %a)  # Error
print(a)                                              # 'Hyd'

# Find outputs
a = [10, 20, 30, 40]
print('%s' % a)                                       # '[10, 20, 30, 40]'
print('%s', a)                                        # ('%s', [10, 20, 30, 40])
# print('%s' a)  # Error
# print('%s' , %a)  # Error
# print('%l' % a)  # Error
print(a)                                              # [10, 20, 30, 40]

# Find outputs
a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s' % (a, b, c))
print('%i    %g    %s' % (a, b, c))
print('%s    %s    %s' % (a, b, c))
print('%d    %g    %s', a, b, c)                      # Tuple printed
# print('%d    %g      %s'   a , b , c)  # Error
# print('%d    %g    %s'  ,  %(a , b , c))  # Error
# print('%d    %g    %s'    %a%b%c)  # Error
print('%d' % a, '%f' % b, '%s' % c)
