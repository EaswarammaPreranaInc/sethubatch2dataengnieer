1.# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function')         
How  to  print  dictionary  with  print()  function    #print(a)={10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Keys  of  dictionary')                      
How  to  print  each  key  of  dict  'a'               #print(list(a.keys()))    #10 
print('Values  of  dictionary')                                                  #20
                                                                                 #15
                                                                                 #18
How  to  print  each  value  of  dict  'a'             #print(list(a.values)))   # Ramesh
                                                                                 # kiran
                                                                                 # Amar
                                                                                 # sita
print('All  the  tuples  of  dict_items   object')
How  to  print  each  tuple  of  the  list  in  dict_items  object
print('Elements  of  each   tuple')                    #print(list(a.items()))   #(10, 'Ramesh')
                                                                                 #(20, 'kiran')
                                                                                 #(15,  'Amar')
                                                                                 #(18,  'sita')
How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object 
print('Keys  and  values  of  dictionary')                          
How  to  print  each  key  and  corresponding  value  in  dict  'a'  #print(a*.items()) key :10 value : Ramesh
                                                                                        key :20 value  : kiran
                                                                                        key :15 value  : Amar
                                                                                        key :18 value  : sita




2.#  Find  outputs (Home  work)
a = {
		print('Hyd') ,     #Hyd
		print('Sec') ,     #sec
		print('Cyb')       #cyb
	}
print(type(a))                     #<class 'set'>
print(a)                           #{None}
print(len(a))                      #1




3.#  Anonymous  object  demo  program
_ = 25
print(_)                         #25
print(type(_))                   #<class 'int'>
a , _ , c = 10 , 20 , 30
print(a)                         #10
print(_)                         #20
print(c)                         #30
for  _  in  range(5):
	print(_ , 'Hello')       #0 Hello
                                 #1 Hello
                                 #2 Hello
                                 #3 Hello
                                 #4 Hello

4.#  Find  outputs
a = 25               
print(id(a))                #Address of 'a'may be 1000
a = 35
print(id(a))                # Address of 'b may be 1050




5.# Find  outputs (Home  work)
a = 25.7
print(id(a))              # Address of 'a' may be 1000
print(a)                  # value of 'a' is 25.7
a = 35.6
print(id(a))              #Address of 'a' may be 2000
print(a)                  #value of 'a' is 35.6
b = True
print(id(b))              #Address of 'b' may be 3000
b = False                 
print(id(b))              # Address of 'b' may be 4000
c = None
print(id(c))              # Address of 'c' may be 4050
c = None
print(id(c))              # same address




6.#  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a))             # prints Address of object 'Hyd'
a[1] = 'e'               # Error because of str is immutable
a = 'Sec'                # Refers to a new string
print(id(a))             # Address of object 'a' changes to a new one
b = (10 , 20 , 15 , 18)  # Tuple object is created 
print(id(b))             # Address of 'b' is printed 
b[2] = 19                # Error because tuple is immutable
b = (30 , 40 , 35 , 32)  # Refers to a new tuple
print(id(b))             # Address of 'b' changes to a new one
c = range(5)
print(id(c))             # Address of 'c' will be printed
c[3] = 10                # Error
c = range(5)             # new range object is created
print(id(c))             # Same Address 




7.# Find  outputs  (Home  work)
a = 25          #Reference  of object 'a' is 25
b = 25          #Reference of object 'b' is 25
print(a  is  b)  # True
c = 'Hyd'
d = 'Hyd'
print(c  is  d)  # True
e = False
f = False
print(e  is  f)  #True
g = range(10)
h = range(10)    # New range object
print(g  is  h)  # False 




8.#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]  # New list object 'b'
print(a  is  b)          # False 
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}  # New Dict object 'd'
print(c  is  d)          # False
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)  # New Tuple 'f'
print(e  is  f)          # True
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h)         # False



9.# Find outputs (Home work)
print(10 + 20)  # 30
print(10.8 + 20.6) # 31.4
print(3 + 4j + 5 + 6j) #8+10j
print(True + False) # 1
print('Hyder' + 'abad')# 'Hyderabad'
print('Sankar' + 'Dayal' + 'Sarma') # 'sankarDayalsarma'
print('10' + '20')  #'1020'  
print([10 , 20 , 30] + [1 , 2 , 3])# [10, 20, 30, 1, 2, 3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None)) # (25 , 10.8 , 'Hyd',(3 + 4j) , True , None)
print({10 , 20} + {30 , 40})     # Error because of '+' operator
print({10 : 'Hyd'} + {20 : 'Sec'})# Error because of '+' operator
print(range(4) + range(5))      # Error
print(10 + '20')                #Error because cannot add str and int
print([10 , 20 , 30] + 5)       # Error because of list and int
print([10 , 20 , 30] + (40 , 50 , 60)) #Error because cannot add list and tuple




10.# Find outputs (Home work)
print(25 * 3)        # 75
print(10.8 * 25.6)   #276.48
print(True * False)  #0
print((3 + 4j) * (5 + 6j))# (3X5 - 4X6) + (3X6 + 4X5)j = (15-24)+(18+20)j= -9+38j
print(3 + 4j * 5 + 6j) # 4j*5 = 20j 3+20j+6j= 3+26j
print('25' * 3)           #'252525'
print(3 * '25')           #'252525'
print('Hyd' * 4)          #'HydHydHydHyd'
print([10 , 20 , 15] * 2)   #[10 , 20 , 15,10 , 20 , 15]
print((25, 10.8, 'Hyd', True) * 3)  #(25, 10.8, 'Hyd', True,25, 10.8, 'Hyd', True,25, 10.8, 'Hyd', True)
print([10 , 20 , 15] * 3.0) # Error 'Float' cannot be multiplied
print({10 , 20 , 15} * 2)  # Error because set cannot support multiplication.
print({10 : 20 , 30 : 40} * 2) # Error because dictionaries cannot be multiplied
print([10] * [20])     # Error cannot multiply list by other list




11.#  /  operator  demo  program
print(9.0 / 2) #4.5
print(9 / 2.0) #4.5
print(9.0 / 2.0)#4.5
print(9 / 2)   #  4.5
print(10.5 / 2) #5.25
print(10 / 3) #3.33
print(10 / 2) #5.0





12.#  //  operator  demo  program
print(9 // 2)  #   prev  integer  of (4.5) = 4
print(9.0 // 2) #4.0
print(9 // 2.0) #4.0
print(9.0 // 2.0) #4.0
print(10.5 // 2) #5.0
print(10 // 3) #3
print(10.0 // 3)  #    prev  integer  of  3.33 = 3.0
print(8.5 // 3) #2.0
print(18 // 4)  #4
print(-18 // 4) # -5
print(-(18 // 4)) # -4 





13.# % operator demo program
print(9 % 5)    #4
print(9.0 % 5)  #4.0
print(9 % 5.0)  #4.0
print(9.0 % 5.0) #4.0
print(10.5 % 2)  #   0.5
print(8.9 % 3) #2.90





14.# Find outputs
print(7 / 0) #Error
print(7 // 0)#Error
print(7 % 0) #Error




15.# ** operator demo program
print(3 ** 4)   # 81
print(10 ** -2) # 0.01
print(4 ** 3 ** 2) # 262144
print(3 + 4 * 5 - 32 / 2 ** 3) # 19.0




16.#  Relational  operators  demo  program (Home  work)
print(9 >= 5)  #   True :  >  is  satisfied
print(9 >= 9)   #   True :  =  is  satisfied
print(9 >= 12)   #  False :  Both  are  not  satisfied
print(6 <= 8)    #True
print(6 <= 6)    #True
print(6 <= 4)    #False
print(9 != 7)    #True
print(6 == 8)    #False
print(True  >  False)  #True
print(3 + 4j == 3 + 4j) #True
print(3 + 4j == 5 + 6j) #False
print(3 + 4j != 5 + 6j) #True
print(10 == 10.0) # True
print(3 + 4j >  3 + 4j)# Error Becoz both complex are same





17.#  Find  outputs  (Home  work)
print('Rama'   >  'Rajesh')  #   True :  'm' > 'j'
print('Rama'  <  'Sita') #  True : 'R' < 'S'
print('Hyd'  ==  'Hyd') #True 
print('Rama'  <=   'Ramana') #True : N a
print('Rama  Rao'  >=  'Rama')#True
print('Hyd'  != 'Sec') # True
print('HYD'  <   'hyd') # True





18.#print(10 < 20 < 30)  #   True
print(10 >= 20 < 30)  #   False : 10  is  not  >= 20
print(10 < 20 > 30)   #False
print(1 < 2 < 3 < 4)  #True
print(1 < 2 > 3 > 1)  #False
print(4 > 3 >= 3 > 2) #True




19.#  or  operator  demo program
print(True  or  False) #  True
print(False  or  True) #   True
print(True  or  True) #  True
print(False  or   False)   #  False
print(10  or  20)#  10
print(0   or  20)  #  20
print(-25  or  0) #-25
print(''  or  35) #35
print(6j  or  'Hyd') #6j
print(0.0  or  3 + 4j) #(3+4j)
print('Hyd'   or   10.8) #Hyd





20.# not  operator  demo  program
print(not  True) #   False
print(not  False) #  True
print(not  25)  # False
print(not  0)   #True
print(not  'Hyd')#False
print(not  '')  #True
print(not  -10)# False
print(not  not  'Hyd')#True





21.#  Find   outputs (Home work)
i = 10
i = not  i > 14
print(i)  # True
print(not(6 < 4  or  9 >= 5  and  6 != 6)) #True