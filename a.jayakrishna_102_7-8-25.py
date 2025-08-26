#1.Write  a  program  to  determine  largest  command  line  input

from sys import argv
try:
    if len(argv)==1:
        print("Enter an integer")
    elif int(argv[1]) % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
except ValueError:
    print("Enter an integer")


#2.Write  a  program  to  determine  command  line  input  is  even  number  or  odd  number

from sys import argv
try:
    if len(argv)==1:
        print("Enter an integer")
    elif int(argv[1]) % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
except ValueError:
    print("Enter an integer")



#3.Write  a  program  to  determine  average  of  command  line  inputs

from sys import argv
try:
    s = []
    for i in range(1,len(argv)):
        s.append(int(argv[i]))
    print(sum(s)/len(s))
except (ValueError, ZeroDivisionError):
    print("Please send number input")



#4.Write  a  program  to  sort  command  line  inputs  in  ascending  order  and  descending  order

from sys import argv
try:
    s = []
    for i in range(1,len(argv)):
        s.append(eval(argv[i]))
    print(sorted(s))
    print(sorted(s,reverse=True))
except (ValueError,TypeError):
    print("Please don't send number and string input together ")
except NameError:
    print("Enter strings in single quotes or triple single quotes")



#5.# Find outputs  (Home  work)

print( 'green'   in   'Hyd  is  green  city') # True
print('day'   in   'Sankar  dayal  sarma') # True
print('Green'   in   'Hyd  is  green  city') # False
print('d  is'   in   'Hyd  is  green  city') # True
print('dis'   in   'Hyd  is  green  city') # False
print('iniv'   in   'Srinivas') # True
print('iniv'   not   in   'Srinivas') # False


#6. (Home  work)
#Slice  demo  program
#0      1       2        3      4       5       6       7
#R      a      m        a               R       a       o
#-8    -7     -6      -5     -4      -3     -2      -1


a = 'Rama Rao'
print(a [ : 7 : 2]) #  a[0 : 7 : 2]  --->  string  from  indexes  0  to  6  in  steps  of  2  i.e.  Rm<space>a
print(a [ : 7]) #  a[0 : 7 : 1]  --->  string  from  indexes  0  to  6  in  steps  of  1  i.e.  Rama<space>Ra
print(a [2 : 4]) #  a[2 : 4 : 1]  --->  string  from  indexes  2  to  3  in  steps  of  1  i.e.  ma
print(a [2 : ]) #  a[2 : 8 : 1]  --->  string  from  indexes  2  to  7  in  steps  of  1  i.e.  ma<space>Rao
print(a [ : 4 ]) #  a[0 : 4 : 1]  --->  string  from  indexes  0  to  3  in  steps  of  1  i.e.  Rama
print(a [ : : 2]) #  a[0 : 8 : 2]  --->  string  from  indexes  0  to  7  in  steps  of  2  i.e.  Rm<space>a
print(a [-6 : -1]) #  a[-6 : -1 : 1]  --->  string  from  indexes  -6  to  -2  in  steps  of  1  i.e.  ma<space>Ra
print(a [-6 : ]) #  a[-6 : 8 : 1]  --->  string  from  indexes  -6  to  7  in  steps  of  1  i.e.  ma<space>Rao
print(a [: -4 : -1]) #  a[-1 : -4 : -1]  --->  string  from  indexes  -1  to  -3  in  steps  of  -1  i.e.  oaR
print(a [-3 : -1]) #  a[-3 : -1 : 1]  --->  string  from  indexes  -3  to  -2  in  steps  of  1  i.e.  Ra
print(a [-3 : ]) #  a[-3 : 8 : 1]  --->  string  from  indexes  -3  to  7  in  steps  of  1  i.e.  Rao
print(a [ : : ]) #  a[0 : 8 : 1]  --->  string  from  indexes  0  to  8  in  steps  of  1  i.e.  Rama<space>Rao
print(a [ : ]) #  a[0 : 8 : 1]  --->  string  from  indexes  0  to  8  in  steps  of  1  i.e.  Rama<space>Rao
print(a [ : : -1]) #  a[-1 : -9 : -1]  --->  string  from  indexes  -1  to  -8  in  steps  of  -1  i.e.  oaR<space>amaR
print(a [ : : -2]) #  a[-1 : -9 : -2]  --->  string  from  indexes  -1  to  -8  in  steps  of  -2  i.e.  oRaa
print(a [ -2 : : -2])  #  a[-2 : -9 : -2]  --->  string  from  indexes  -2  to  -8  in  steps  of  -2  i.e.  a<space>mR
print(a [2 : 8]) #  a[2 : 8 : 1]  --->  string  from  indexes  2  to  7  in  steps  of  1  i.e.  ma<space>Rao
print(a [2 : 8 : -1]) #  a[2 : 8 : -1]  --->  string  from  indexes  2  to  7  in  steps  of  -1  i.e.  Nothing will print
print(a [ : -6 : -1]) #  a[-1 : -6 : -1]  --->  string  from  indexes  -1  to  -5  in  steps  of  -1  i.e.  oaR<space>a
print(a [2 : -3]) #  a[2 : -3 : 1]  --->  string  from  indexes  2  to  -4  in  steps  of  1  i.e.  ma<space>
print(a [1 : 6 : 2]) #  a[1 : 6 : 2]  --->  string  from  indexes  1  to  5  in  steps  of  2  i.e.  aaR
print(a [ : -5 : -5]) #  a[-1 : -5 : -5]  --->  string  from  indexes  -1  to  -4  in  steps  of  -5  i.e.  o
print(a [2 : -5]) #  a[2 : -5 : 1]  --->  string  from  indexes  2  to  -6  in  steps  of  1  i.e.  m
print(a [2 : -5 : 2]) #  a[2 : -5 : 2]  --->  string  from  indexes  2  to  -6  in  steps  of  2  i.e. m
print(a [ : 0 : -1]) #  a[-1 : 0 : -1]  --->  string  from  indexes  -1  to  1  in  steps  of  -1  i.e.  oaR<space>ama
print(a [-5 : 0 : -2]) #  a[-5 : 0 : -2]  --->  string  from  indexes  -5  to  1  in  steps  of  -2  i.e.  aa



#7.Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  first  two
#characters  of  the  two  strings.Assume  that  each  string  has  a   minimum  of  two  characters.

a = input("Enter first string :")
b = input("Enter second string :")
if len(a) >= 2 and len(b) >= 2:
    print(b[:2] + a[2:], a[:2] + b[2:] , sep=" ")
else:
    print("Input should be a minimum of 2-char string")



#8.Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
#Print  an  empty  string  if  string  has  less  than  four  characters

a = input("Enter a string :")
if len(a) >= 4:
    print(a[:2] + a[len(a)-2:])
else:
    print("[]")



#9.Write  a  program  to  print  characters  of  the  string  in  forward  and  reverse
#directions  without  slice

a = input("Enter a string :")
for i in range(len(a)):
    print(f'Character at index {i} :' ,a[i])
print()
for j in range(-1,(-len(a)-1),-1):
    print(f'Character at index {j}:',a[j])




#10.Write  a  program  to  print  characters  at  even  and  odd  indexes  without  slice

a = input("Enter a string :")
even = ''
odd = ''
for i in range(len(a)):
    if i % 2 == 0:
        even += a[i]
    else:
        odd += a[i]
print("String at even indexes : ",even)
print("String at odd indexes : ",odd)




"""#11.Let  input  be    A   4   B   3   C   2   $   5
                      0   1    2   3   4   5   6   7

#What  is  the  output ?  --->  AAAABBBCC$$$$$
"""
a = input("Enter any string with alternate character and digit :")
result = ''
try:
    for i in range(0,len(a),2):
        result += a[i] * int(a[i+1])
    print("Result : ",result)
except:
    print("String should have alterate character and digit")




#12.Write  a  program  to  merge  two  strings  to  form  a  new  string

a = input("Enter first string :")
b = input("Enter second string :")
result = ''
mini = min(a, b)
maxi = max(a, b)
i = 0
minn = len(mini)
while minn != 0 :
    result += (a[i] + b[i])
    i += 1
    minn -= 1
print(result + maxi[len(mini):])




#13.Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set

a = input("Enter any string :")
result = ''
for i in range(len(a)):
    if a[i] not in a[:i]:
        result += a[i]
print("String without duplicates : " , result)




#14.# len()  function  demo  program  (Home  work)

print(len('Hyd'))  #  3
print(len('Rama Rao')) # 8
print(len('9247')) # 4
print(len('+-$')) # 3
print(len('')) # 0
print(len(' ')) # 1
print(len('A2#')) # 3
print(len(3456)) #Error due do non sequences does not have lengths
print('Sec'. len())  # Error 



#15.# chr()  function  demo  program

print(chr(65))  #   Converts  unicode  value  65  to  'A'
print(chr(90))  #   Converts  unicode  value  90  to  'Z'
print(chr(97))  #   Converts  unicode  value  97  to  'a'
print(chr(122))  #   Converts  unicode  value  122  to  'z'
print(chr(48))  #   Converts  unicode  value  48  to  '0'
print(chr(57))  #   Converts  unicode  value  57  to  '9'
print(chr(36))  #   Converts  unicode  value  36  to  '$'
print(chr(32))  #   Converts  unicode  value  32  to  '<space>'




#16.# ord()  function  demo  program

print(ord('A'))  #  Converts  'A'  to  unicode  value  65
print(ord('Z'))  #  Converts  'Z'  to  unicode  value  90
print(ord('a'))  #  Converts  'a'  to  unicode  value  97
print(ord('z'))  #  Converts  'z'  to  unicode  value  122
print(ord('0'))  #  Converts  '0'  to  unicode  value  48
print(ord('9'))  #  Converts  '9'  to  unicode  value  57
print(ord('$'))  #  Converts  '$'  to  unicode  value  36
print(ord(' '))  #  Converts  '<space>'  to  unicode  value  32




#17.Let  input  be  A4M3Z5D2
#What  is  the  output ?  --->  AEMPZ_DF

a = input("Enter any string with alternate character and digit : ")
result = ''
try:
    for i in range(0,len(a),2):
        result += (a[i] + chr(ord(a[i]) + int(a[i+1])))
    print(result)
except:
    print("Please Enter string with alternate character and digit")