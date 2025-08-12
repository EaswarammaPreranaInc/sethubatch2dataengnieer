#Seq_DSVishnu_12-7-25
# ===================================== Sequence(string,range,list,tuple,set,dictionary) ===========================================

#===========================================String===============================
a = "Rama Rao"
print(a) #Rama Rao 
print(type(a))# <class 'str'>
print(id(a))# Address of object 'a'
b = 'Hyd'
print(b) #Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c) 

a = 'Hyd'
print(a[0])#(How  to  print  'H'  of  object  'a')
print(a[1])#(How  to  print  'y'  of  object  'a')
print(a[2])#(How  to  print  'd'  of  object  'a')
#print(a[3])#Error  IndexError: string index out of range
print(a[-1])#(How  to  print  'd'  of  object  'a')
print(a[-2])#(How  to  print  'y'  of  object  'a')
print(a[-3])#(How  to  print  'H'  of  object  'a')
#print(a[-4])#Error  IndexError: string index out of range
print(a[0] ==  a[-3])#True 
#a[2] = 'c'#Error   TypeError: 'str' object does not support item assignment
#print(25[0])#Error   SyntaxWarning: 'int' object is not subscriptable
print('25'[0])#2
#print(True[1])#Error  SyntaxWarning: 'bool' object is not subscriptable;
print('True'[1])#r 

a = 'Hyd'
print(a * 3)# HydHydHyd
print(a * 2)# HydHyd
print(a * 1)# Hyd
print(a * 0)#
print(a * -1)#
print(25 * 3)#75
print('25' * 3)# 252525 
#print('25' * 4.0)#Error  TypeError: can't multiply sequence by non-int of type 'float'
print(3 * 'Hyd')# HydHydHyd
print('25'*True)# 25

print(len('Hyd'))#3
print(len('Rama Rao'))#8
print(len('9247'))#4
print(len(''))#0
print(len(' '))#1
#print(len(689))#Error  TypeError: object of type 'int' has no len()

a = """"Hyd"""
print(a)# "Hyd
print(len(a))#4
print(a[0])# "
#print("""Hyd"""")#Error  SyntaxError: unterminated string literal
b = """""Hyd"""
print(b)# ""Hyd 
print(len(b))#5


                       #   0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17
a = 'Sankar Dayal Sarma' # S   a   n   k   a   r       D   a   y   a   l      S   a   r   m   a 
#                         -18 -17 -16 -15 -14 -13  -12 -11 -10 -9  -8  -7  -6 -5  -4  -3  -2  -1

print(a[7 : 12])# a[7 : 12 : 1] --->   string  from  indexes  7  to  11  in  steps  of   1  i.e. Dayal
print(a[7 : ])  # a[7 : 18 : 1] --->   string  from  indexes  7  to  17  in  steps  of   1  i.e. Dayal Sarma
print(a[ : 6])  # a[0 : 6 : 1] --->   string  from  indexes  0  to  5  in  steps  of   1 i.e. Sankar
print(a[ : ])  #  a[ 0 :  18  : 1]  --->   string  from  indexes  0  to  17  in  steps  of   1  i.e.  Sankar Dayal Sarma
print(a[:  : ])#  a[ 0 :  18  : 1]  --->   string  from  indexes  0  to  17  in  steps  of   1  i.e.  Sankar Dayal Sarma
print(a[1 : 10 : 2])#  a[ 1 :  10  : 2]  --->   string  from  indexes  1  to  9  in  steps  of   2  i.e.  akrDy
print(a[0 : : 2])#  a[ 0 :  18  : 2]  --->   string  from  indexes  0  to  17  in  steps  of   2  i.e.  Sna aa am
print(a[1 : : 2])#  a[ 1 :  18  : 2]  --->   string  from  indexes  1  to  17  in  steps  of   2  i.e.  akrDylSra
print(a[-5 : -1])#  a[ -5 :  -1  : 1]  --->   string  from  indexes  -5  to  -2 in  steps  of   1  i.e.  Sarm
print(a[::-1])#  a[ -1 :  -19  : -1]  --->   string  from  indexes  -1  to  -18  in  steps  of   -1  i.e. amraS layaD raknaS  
print(a[-1:-5:-1])#  a[ -1 :  -6  : -1]  --->   string  from  indexes  -1  to  -5  in  steps  of   -1  i.e.  amraS
print(a[ : : -2]) #   a[-1 :  -19 : -2]  --->  string  from  indexes  -1  to  -18  in  steps  of   -2  i.e.  arSlyDrka
print(a[3 : -3])#  a[ 3 :  -3  : 1]  --->   string  from  indexes  3  to -4   in  steps  of   1  i.e.  kar Dayal Sa
print(a[2 : -5])#  a[ 2 :  -5  : 1]  --->   string  from  indexes  2  to  -6  in  steps  of   1  i.e.  nkar Dayal 
print(a[-1:-5])#  a[ -1 :  -5  : 1]  # Empty String
print(a[3 : 3])#  a[ 3 :  3  : 1]  ---> # Empty String


#===========================================str()=============================== 
print(str(25))  #  Converts   25  to  '25'
print(str(10.8))#  Converts   10.8  to  '10.8'
print(str(3 + 4j))#  Converts 3+4j  to  '(3+4j)'
print(str(True))#  Converts   True  to  'True'
print(str(False))#  Converts  False  to  'False'
print(str(None))#  Converts   None  to  'None'


#===========================================Range===============================
a = range(10 , 50 , 5)
print(type(a)) # <class 'range'>
print(a)# range(10 , 50 , 5)
print(*a)# 10 15 20 25 30 35 40 45
print(id(a))# Address of object 'a'
print(len(a))#8
#           0  1  2  3  4  5  6  7
#           10 15 20 25 30 35 40 45
#          -8 -7 -6 -5 -4 -3 -2 -1
print(*a[2 : 7] , sep = ' , ')#  a[ 2 :  7  : 1]  --->   string  from  indexes  2  to  6  in  steps  of   1  i.e.  20,25,30,35,40
print(*a[ : : -1])# a[ -1 :  -9  : 1]  --->   string  from  indexes  -1  to  -8  in  steps  of   1  i.e.  45 40 35 30 25 20 15 10
#a[4] = 32 # Error TypeError: 'range' object does not support item assignment
#print(a*2) # Error TypeError: unsupported operand type(s) for *: 'range' and 'int'

a = range(10 , 20)# range(10,20,1)
print(*a , sep = ',')# 10,11,12,13,14,15,16,17,18,19
b = range(5)# range(0,5,1)
print(*b)#0 1 2 3 4
c = range(10 , 1 , -1)
print(*c , sep = '...')# 10...9...8...7...6...5...4...3...2
d = range(-10 , 0)# range(-10,0,1)
print(*d)# -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
e = range(-10) # range(0,-10,1)
print(*e)# Empty Range 
f = range(2,2)# range(2,2,1)
print(*f)#Empty Range
#g = range(10,11,0.1)#Error TypeError: 'float' object cannot be interpreted as an integer
#h = range('A','F')#Error TypeError: 'str' object cannot be interpreted as an integer

r = range(10,17 ,3)
a , b , c = r 
print(a , b , c) # 10 13 15
r = range(3)# range(0,3,1)
#x,y=r# Error ValueError: too many values to unpack (expected 2)
#p,q,r,s=r # Error ValueError: not enough values to unpack (expected 4, got 3)
#a,b,c=*r # Error SyntaxError: can't use starred expression here















