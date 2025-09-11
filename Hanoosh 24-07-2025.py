# eval()  function  demo  program
print(eval('25')) # 25
print(eval('10.8')) # 10.8
print(eval('False')) # False
print(eval('3+4j')) # (3+4j)
print(eval('Hyd')) # 'Hyd'
print(eval("    'Hyd'   ")) #     'Hyd'   
print(eval('3 + 4 * 5')) # 23
print(eval('[10 , 20 , 15 , 18]')) # [10 , 20 , 15 , 18]
print(eval('{10,20,15,18,20,12,18}')) # {10,20,15,18,20,12,18}
print(eval('(10 , 20 , 30)')) # (10 , 20 , 30) 
print(eval("{10 : 'Hyd' , 10 : 'Sec'}")) # {10 : 'Hyd' , 10 : 'Sec'}
print(eval(4 + 5)) # error





#  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   ")) # 'hyd'
hyd = 'Sec'
print(eval('hyd')) # 'Sec
sec = '25'
print(eval('sec')) # '25'
print(eval(sec)) # 25
cyb = 10.8
print(eval('cyb')) # '10.8'
print(eval(cyb)) # error




#  Tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")')) # None




#  Find  outputs  (Home  work)
print(bool('False')) # True
print(eval('False')) # False
print(bool('')) # False
print(eval('  ""  ')) # 
print(eval('')) # 
print(eval('  " "   ')) # ' '
print(eval(' ')) #




# What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  ')) # None
print(type(x)) # <class 'None type'>
print(x) # None




# What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ') # Sairam
print(len(a)) # 6
print(a) # Sairam
b = eval(input('Enter   any  string  : ')) # 'Sairam'
print(len(b)) # 6
print(b) # Sairam




# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')   #   25 , 10.8 , Hyd
print(a , b , c , sep = '\t')  #  25	10.8	Hyd
print(a , b , c , sep = '---') #  25---10.8---Hyd
print(a , b , c , sep = '\n')  # 25 <next line> 10.8 <next line> Hyd <next line>
print(a , b , c) # 25 <next line> 10.8 <next line> Hyd <next line>
print(a , b , c , separator = ':') # error




# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---') # error
print(a , b , c , sep = ',,,') # 25,,,10.8,,,Hyd,,,
print(a , b , c , sep = ':::' , end = '\t\t\t') # 25	10.8	Hyd
print(a , b , c) # 25 <next line> 10.8 <next line> Hyd <next line> 





# Find outputs  (Home  work)
print('Hyd')
print()
print('Sec')
print()
print('Cyb')

'''
Hyd

Sec

Cyb

'''




# Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s) # [10 , 20 , 30 , 40] (10 , 20 , 30 , 40) {30 , 20 , 40 , 10}





#  Find  outputs (Home  work)
a = 25
b = '%f'  %a
print(b) # 25.000000
print(type(b)) # string float
x = 10.8
y = '%d'  %x
print(y) # 10
print(type(y)) # string decimal integer
m = [10 , 20 , 15 , 18]
n = '%s'  %m
print(n) # '10' '20' '30' '40'
print(type(n)) # string 





# Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f'  %a)  #  <3  spaces>10.93
print('%9.1f'  %a)  #  <5  spaces>11.0
print('%10.3f'  %a) #  <4  spaces>10.928
print('%.2f'  %a)   #  10.93
print('%.6f'  %a)   # 10.927400
print('%f'  %a)     # 10.927400





# Find  outputs (Home  work)
a = 'Hyd'
print('%7s'  %a)   #  <4  spaces>Hyd
print('%-7s'  %a)  #  Hyd<4   spaces>
print('%2s'  %a)   #  Hyd  and  ignores  smaller width
print('%s'  %a)    #  Hyd  and  ignores  smaller width
print('%s' , a)    #  Hyd  and  ignores  smaller width
print('%s'  a)     #  error
print('%s' , %a)   #  error
print(a)           #  Hyd





# Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40]
print('%s'  %a)   # '10' '20' '30' '40'
print('%s' , a)   # '10' '20' '30' '40'
print('%s'  a)    # error
print('%s' , %a)  # error
print('%l'  %a)   # error
print(a)          # [10 , 20 , 30 , 40]





#Find outputs  (Home  work)
a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c))            # 25 10.927400 Hyd
print('%i    %g    %s'    %(a , b , c))          # 25 10.9274 Hyd
print('%s    %s    %s'  %(a , b , c))            # '25' '10.9274' 'Hyd'
print('%d    %g    %s'  , a , b , c)             # 25 10.9274 Hyd
print('%d    %g      %s'   a , b , c)		 # error
print('%d    %g    %s'  ,  %(a , b , c))	 # error
print('%d    %g    %s'    %a%b%c)		 # error
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c)  # 25 10.927400 Hyd


