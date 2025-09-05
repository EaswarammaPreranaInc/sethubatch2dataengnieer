#1) How  to  print  dictionary  in  different  ways 
a = {10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18: 'Sita'} 
print(a)   # Dictionary with print function 
for k in a.keys(): print(k) # How to print each key of dict 'a' 
for v in a.values(): print(v) # How to print each value of dict 'a' 
for i in a.items(): print(i)   # How to print each tuple of the list in dict_items object 
for i in a.items(): print(i[0], i[1]) # How to print elements of each tuple in the list of dict_items object 
for k, v in a.items(): print(k, v) # How to print each key and corresponding value in dict 'a' 

#2) Find  outputs (Home  work) 
Hyd     # print('Hyd') 
Sec     # print('Sec') 
Cyb     # print('Cyb') 
<class 'set'>     # print(type(a)) 
{None}           # print(a) 
1                
# print(len(a)) 

#3)  Anonymous  object  demo  program 
_ = 25 
print(_)      
        # 
25          
print(type(_))    # <class 'int'>     
a, _, c = 10, 20, 30 
print(a)    
          # 
print(_)      
print(c)    
        # 
          # 
for _ in range(5): 
10           
20         
30          
print(_, 'Hello') # 0 Hello    # print(_, 'Hello') where _ is loop variable 0 to 4 
# 1 Hello 
# 2 Hello 
# 3 Hello 
# 4 Hello 

#4) Find  outputs 
a = 25 
print(id(a))  # 9788896 → 'a' is referencing memory of value 25 
a = 35 
print(id(a))  # 9789216 → 'a' now references new memory of value 35 

#5 Find  outputs (Home  work) 
a = 25.7 
   # 25.7 
print(id(a))  # 140375891479888 (example ID) - reference ID of float 25.7 
print(a)    
a = 35.6 
print(id(a))  # 140375891478928 (example ID) - reference changed  
       # 35.6 
print(a)
 b = True 
print(id(b))  # 9480544 (example ID) - reference ID of bool True 
b = False 
print(id(b))  # 9479984 (example ID) - reference changed because  
c = None 
print(id(c))  # 9481024 (example ID) - reference ID of NoneType 
c = None 
print(id(c))  # 9481024 (same ID) - reference not changed, both are same object 

#6) Find  outputs  (Home  work) 
a = 'Hyd' 
print(id(a))
 a[1] = 'e'          
a = 'Sec' 
print(id(a))
       #
 140379705188528 (example ID) - reference ID of string 'Hyd' 
# Error: strings are immutable 
       #
 140379705187568 (example ID) - reference changed due to new string assignment 
b = (10, 20, 15, 18) 
print(id(b))
 b[2] = 19     
       # 
140379705189648 (example ID) - reference ID of original tuple 
      # Error: tuples are immutable, can't assign to index 
b = (30, 40, 35, 32) 
print(id(b))
 c = range(5) 
print(id(c))
 c[3] = 10   
c = range(5) 
print(id(c))
       # 
       #
 140379705190384 (example ID) - reference changed due to new tuple assignment 
 140379705191264 (example ID) - reference ID of range object 
        # Error: 'range' object does not support item assignment 
       #
 140379705191344 (example ID) - new reference, range cannot be reusable 
#7)Find  outputs  (Home  work) 
a = 25 
b = 25 
print(a is b)  
c = 'Hyd' 
d = 'Hyd' 
print(c is d)  
e = False 
f = False 
print(e is f)
 g = range(10) 
h = range(10) 
print(g is h)    
     # 
     # 
       # 
True, both refer to same memory 
True, same memory reference 
True   
   # False, range cant be resuable, even if values are same 

#8)Find  outputs(Home  work) 
a = [10, 20, 15, 18] 
b = [10, 20, 15, 18] 
print(a is b)  
     # False  # lists are mutable; new object is created 
c = {10: 20, 30: 40} 
d = {10: 20, 30: 40} 
print(c is d)  
     # False  # dicts are mutable; separate memory locations 
e = (10, 20, 15, 18) 
f = (10, 20, 15, 18) 
print(e is f)
       # 
True  # tuples with same values may be reused (immutable optimization) 
g = {10, 20, 15, 18} 
h = {10, 20, 15, 18} 
print(g is h)    
   # False  # sets are mutable; new object is created 

#9) Find  outputs(Home  work) 
print(10 + 20)                                        
print(10.8 + 20.6)                                  
print(3 + 4j + 5 + 6j)                             
print(True + False)                                
print('Hyder' + 'abad')                           
print('Sankar' + 'Dayal' + 'Sarma')        
print('10' + '20')                                    
print([10, 20, 30] + [1, 2, 3])               
# 30 
# 31.4 
# (8+10j) 
# 1  # True = 1, False = 0 
# 'Hyderabad' 
# 'SankarDayalSarma' 
# '1020'  # string concat 
# [10, 20, 30, 1, 2, 3] 
print((25, 10.8, 'Hyd') + (3 + 4j, True, None))
 print({10, 20} + {30, 40})                   
     # 
(25, 10.8, 'Hyd', (3+4j), True, None) 
# Error: unsupported operand '+' for set 
print({10: 'Hyd'} + {20: 'Sec'})           # Error: unsupported operand '+' for dict 
print(range(4) + range(5))   
                #
 print(10 + '20')                                    
 Error: unsupported operand '+' for range 
# Error: can't add int and str 
print([10, 20, 30] + 5)         
print([10, 20, 30] + (40, 50, 60)) 

#10)Find  outputs(Home  work) 
print(25 * 3)                                      
print(10.8 * 25.6)                
print(True * False)              
print((3 + 4j) * (5 + 6j))      
print(3 + 4j * 5 + 6j)                         
print('25' * 3)                      
print(3 * '25')                      
print('Hyd' * 4)                    
print([10, 20, 15] * 2)                       
print((25, 10.8, 'Hyd', True) * 3)      
print([10, 20, 15] * 3.0)      
print({10, 20, 15} * 2)        
                #
 Error: can't add list and int 
       # Error: can't add list and tuple 
# 75 
              # 
              # 
              # 
276.48 
0  # True = 1, False = 0 
(-9+38j) 
# (3 + 20j + 6j) = 3 + 26j 
              # '252525' 
              # '252525' 
             # 'HydHydHydHyd' 
# [10, 20, 15, 10, 20, 15] 
# (25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True) 
              # Error: can't multiply list by float 
              # Error: unsupported operand '*' for set 
print({10: 20, 30: 40} * 2)                # Error: unsupported operand '*' for dict 
print([10] * [20])                               # Error: can't multiply sequence by non-int of type 'list' 
 
#11)  /  operator  demo  program 
print(9.0 / 2)         # 4.5 
print(9 / 2.0)         # 4.5 
print(9.0 / 2.0)      # 4.5 
print(9 / 2)            # 4.5 
print(10.5 / 2)       # 5.25 
print(10 / 3)          # 3.333 
print(10 / 2)          # 5.0 
 
#12) //  operator  demo  program 
print(9 // 2)           # 4        # prev integer of 4.5 = 4 
print(9.0 // 2)        # 4.0      # prev integer of 4.5 = 4.0 
print(9 // 2.0)        # 4.0      # prev integer of 4.5 = 4.0 
print(9.0 // 2.0)      # 4.0      # prev integer of 4.5 = 4.0 
print(10.5 // 2)       # 5.0      # prev integer of 5.25 = 5.0 
print(10 // 3)          # 3        # prev integer of 3.33 = 3 
print(10.0 // 3)       # 3.0      # prev integer of 3.33 = 3.0 
print(8.5 // 3)         # 2.0      # prev integer of 2.83 = 2.0 
print(18 // 4)          # 4        # prev integer of 4.5 = 4 
print(-18 // 4)         # -5       # prev integer of -4.5 = -5 
print(-(18 // 4))      # -4       # 18 // 4 = 4 → -(4) = -4 
 
#13) % operator demo program 
print(9 % 5)         # 4        # remainder of 9 ÷ 5 
print(9.0 % 5)      # 4.0      # remainder of 9.0 ÷ 5 = 4.0 
print(9 % 5.0)      # 4.0      # remainder of 9 ÷ 5.0 = 4.0 
print(9.0 % 5.0)   # 4.0      # remainder of 9.0 ÷ 5.0 = 4.0 
print(10.5 % 2)    # 0.5      # 10.5 ÷ 2 = 5.0 → 10.5 - (5×2) = 0.5 
print(8.9 % 3)      # 2.9      # 8.9 ÷ 3 = 2.0 → 8.9 - (3×2) = 2.9 
 
#14) Find outputs 
print(7 / 0)        # Error: cannot divide by zero 
print(7 // 0)      # Error: cannot divide by zero 
print(7 % 0)    # Error: cannot divide by zero 
 
#15 ** operator demo program 
print(3 ** 4)                   # 81 
print(10 ** -2)               # 0.01 
print(4 ** 3 ** 2)          # 262144        # 3**2 = 9, then 4**9 = 262144 (Right-to-left) 
print(3 + 4 * 5 - 32 / 2 ** 3)  # 3 + 20 - 4.0 = 19.0 
 
#16)Relational  operators  demo  program (Home  work) 
print(9 >= 5)               # True     # > is satisfied 
print(9 >= 9)               # True     # = is satisfied 
print(9 >= 12)             # False    # Neither > nor = satisfied 
print(6 <= 8)               # True 
print(6 <= 6)               # True 
print(6 <= 4)               # False 
print(9 != 7)               # True 
print(6 == 8)              # False 
print(True > False)    # True     # 1 > 0 
print(3 + 4j == 3 + 4j)     # True 
print(3 + 4j == 5 + 6j)     # False 
print(3 + 4j != 5 + 6j)     # True 
print(10 == 10.0)           # True     # int and float comparison works if values are same 
print(3 + 4j > 3 + 4j)     # Error: complex numbers can't be compared using > or < 
 
print('Rama' > 'Rajesh')        # True     # 'm' > 'j' 
print('Rama' < 'Sita')            # True     # 'R' < 'S' 
print('Hyd' == 'Hyd')            # True 
print('Rama' <= 'Ramana')   # True     # 'Rama' is prefix of 'Ramana' 
print('Rama  Rao' >= 'Rama')  # True     # Full string longer and starts same 
print('Hyd' != 'Sec')                # True 
print('HYD' < 'hyd')               # True     # Capital letters < small letters in ASCII 
 
print(10 < 20 < 30)           # True          # All comparisons are True 
print(10 >= 20 < 30)        # False         # 10 >= 20 is False 
print(10 < 20 > 30)          # False         # 20 > 30 is False 
print(1 < 2 < 3 < 4)         # True          # All comparisons are True 
print(1 < 2 > 3 > 1)        # False         # 2 > 3 is False 
print(4 > 3 >= 3 > 2)     # True          # All comparisons are True 
 
print(True  or  False)       # True        # At least one is True 
print(False  or  True)       # True        # At least one is True 
print(True  or  True)        # True        # At least one is True 
print(False  or  False)      # False       # Both are False 
print(10  or  20)              # 10          # 10 is truthy, so returned 
print(0   or  20)               # 20          # 0 is falsy, so 20 is returned 
print(-25  or  0)              # -25         # -25 is truthy, so returned 
print(''  or  35)               # 35          # '' is falsy, so 35 is returned 
print(6j  or  'Hyd')         # 6j          # 6j is truthy, so returned 
print(0.0  or  3 + 4j)      # (3+4j)      # 0.0 is falsy, so (3+4j) is returned 
print('Hyd'   or   10.8)   # 'Hyd'       # 'Hyd' is truthy, so returned 
 
print(not  True)         # False       # not of True is False 
        # True        # not of False is True 
print(not  False)
 print(not  25)            
print(not  0)             
print(not  'Hyd')      
print(not  '')            
print(not  -10)        
# False       # 25 is truthy → not truthy = False 
# True 
       # 0 is falsy → not falsy = True 
# False 
# True   
# False  
      # Non-empty string is truthy 
     # Empty string is falsy 
     # Any non-zero number is truthy 
print(not  not  'Hyd')   # True        # 'Hyd' is truthy → not 'Hyd' = False → not False = True 
i = 10 
i = not i > 14   
print(i)              
      # 
i > 14 → False → not False = True → i = True 
 # True 
print(not(6 < 4 or 9 >= 5 and 6 != 6)) 
# Step-by-step: 
# 6 < 4 → False,# 9 >= 5 → True,# 6 != 6 → False 
# True and False → False,# False or False → False 
# not(False) → True 
# Final answer: # True 
