# eval()  function  demo  program
print(eval('25')) # 25
print(eval('10.8')) # 10.8
print(eval('False')) # false
print(eval('3+4j')) # (3+4j)
print(eval('Hyd')) # error
print(eval("    'Hyd'   ")) # Hyd
print(eval('3 + 4 * 5')) # 23
print(eval('[10 , 20 , 15 , 18]'))# string list converts to list [10 , 20 , 15 , 18]
print(eval('{10,20,15,18,20,12,18}')) # string set converts to set  {10,20,15,18,20,12,18}
print(eval('(10 , 20 , 30)')) # string tuple converts to tuple (10 , 20 , 30) 
print(eval("{10 : 'Hyd' , 10 : 'Sec'}")) # string dict converts to dict  {10 : 'Hyd' , 10 : 'Sec'}
print(eval(4 + 5)) # error 

#  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   ")) # hyd
hyd = 'Sec'
print(eval('hyd')) # Sec
sec = '25'
print(eval('sec')) # 25
print(eval(sec))  # 25
cyb = 10.8
print(eval('cyb')) # 10.8
print(eval(cyb)) # error not sting format

#  Tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")')) # Hyd
            			       # None

#  Find  outputs  (Home  work)
print(bool('False')) # True
print(eval('False')) # False
print(bool('')) # False
print(eval('  ""  ')) # empty
print(eval('')) # error
print(eval('  " "   ')) # empty tab space
print(eval(' '))# error
# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')   #   25 , 10.8 , Hyd
print(a , b , c , sep = '\t')  # output will printed with tab space   25	10.8		Hyd	
print(a , b , c , sep = '---') #output will printed with  ---   25---10.8---Hyd
print(a , b , c , sep = '\n') # output will printed in new line   25
											10.8
											Hyd
print(a , b , c) # 25 10.8 Hyd
print(a , b , c , separator = ':') # error

# Find outputs  (Home  work)
print('Hyd') # Hyd
print()
print('Sec') # Sec
print()
print('Cyb')# Cyb

# Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s)  # [10 , 20 , 30 , 40]  (10 , 20 , 30 , 40)  {10 , 20 , 30 , 40}

#  Find  outputs (Home  work)
a = 25
b = '%f'  %a
print(b) # 25.00
print(type(b)) # <class 'str'>
x = 10.8
y = '%d'  %x
print(y) # 10
print(type(y)) # <class 'str'>
m = [10 , 20 , 15 , 18]
n = '%s'  %m
print(n) # [10,20,15,18]
print(type(n)) # <class 'str'>

# Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40]
print('%s'  %a) # [10,20,30,40]
print('%s' , a)  # %s [10,20,30,40]
print('%s'  a)# error
print('%s' , %a) # error
print('%l'  %a) # error
print(a) # [10,20,30,40]

# Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f'  %a)  #  <3  spaces>10.93
print('%9.1f'  %a) #				10.9
print('%10.3f'  %a) #				10.927
print('%.2f'  %a) #10.93
print('%.6f'  %a) # 10.927
print('%f'  %a)#10.9274
