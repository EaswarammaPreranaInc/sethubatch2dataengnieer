


# Find outputs  (Home  work)
print( 'green'   in   'Hyd  is  green  city') #True
print('day'   in   'Sankar  dayal  sarma') #True
print('Green'   in   'Hyd  is  green  city') #False
print('d  is'   in   'Hyd  is  green  city') #True
print('dis'   in   'Hyd  is  green  city') #False
print('iniv'   in   'Srinivas') #True
print('iniv'   not   in   'Srinivas') #False



'''  (Home  work)
Slice  demo  program
0      1       2        3      4       5       6       7
R      a      m        a               R       a       o
-8    -7     -6      -5     -4      -3     -2      -1
'''
a = 'Rama Rao'
print(a [ : 7 : 2]) #Rm a
print(a [ : 7]) #Rama Ra
print(a [2 : 4]) #ma
print(a [2 : ]) #ma Rao
print(a [ : 4 ]) #Rama
print(a [ : : 2]) #Rm a
print(a [-6 : -1])#ma Ra
print(a [-6 : ]) #ma Rao
print(a [: -4 : -1])#oaR
print(a [-3 : -1]) #  a[-3 : -1 : 1]  --->  string  from  indexes  -3  to  -2  in  steps  of  1  i.e.  Ra
print(a [-3 : ])#Rao
print(a [ : : ])#Rama Rao
print(a [ : ]) #Rama Rao
print(a [ : : -1])#oaR amaR
print(a [ : : -2])#oRaa
print(a [ -2 : : -2])  #  a[-2 : -9 : -2]  --->  string  from  indexes  -2  to  -8  in  steps  of  -2  i.e.  a<space>mR
print(a [2 : 8]) #ma Rao
print(a [2 : 8 : -1]) # Nothig
print(a [ : -6 : -1]) #oaR a
print(a [2 : -3]) #ma
print(a [1 : 6 : 2]) #aaR
print(a [ : -5 : -5])#o
print(a [2 : -5]) #m
print(a [2 : -5 : 2])#m
print(a [ : 0 : -1]) #oaR ama
print(a [-5 : 0 : -2]) #aa

print(ord('A'))  #  Converts  'A'  to  unicode  value  65
print(ord('Z')) #90
print(ord('a')) #97
print(ord('z')) #122
print(ord('0')) #48
print(ord('9')) #57
print(ord('$')) #36
print(ord(' ')) #32


print(chr(65))  #   Converts  unicode  value  65  to  'A'
print(chr(90)) #Z 
print(chr(97)) #a
print(chr(122)) #z
print(chr(48)) #0
print(chr(57)) #9
print(chr(36)) #$
print(chr(32)) #' '


print(len('Hyd'))  #  3
print(len('Rama Rao')) #8
print(len('9247')) #4
print(len('+-$')) #3
print(len(''))#0 
print(len(' ')) #1
print(len('A2#')) #3
print(len(3456)) #Error  because of nonsequence
print('Sec'. len()) Error due to sytax



