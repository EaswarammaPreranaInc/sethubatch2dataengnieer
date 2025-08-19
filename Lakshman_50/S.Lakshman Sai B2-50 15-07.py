# float  object  demo  program (Home  work)
a = 10.8
print(a)          # 10.8
print(type(a))    # <class 'float'>
print(id(a))      #Some address EX.2000
b = 25.
print(b)          # 25.0      
print(type(b))    # <class 'float'>
c = .689    
print(c)          # 0.689
d = 3.4E2
print(d)          # 340.0
print(type(d))    # <class 'float'>
e = 9.62e-2          
print(e)          # 0.0962
print(9.8.2)      #Error because of extra point 





# complex object demo program
a = 3 + 4j
print(a)                # (3+4j)     
print(type(a))          # <class 'complex'>
print(id(a))            # some addess EX.3000
print(a . real)         # 3.0
print(a . imag)         # 4.0
print(type(a . real))   # <class 'float'>
print(type(a . imag))   # <class 'float'>


# Find outputs (Home work)
a = 6j
print(a)           # 6j          
print(type(a))     #< class 'complex'>        
print(a.real)      # 0.0
print(a.imag)      # 6.0
print(5 + j6)      # Error because j is before 6
print(3 + 4i)      # Error because 'i' in imag 
print(4+j)         # Error because no imag value
print(4 + 1j)      # (4+1j)
print(4 + 0j)      # (4+0j)





# bool object demo program  (Home  work)
a = True
print(a)                      # True      
print(type(a))                # <class 'bool'>
print(id(a))                  # some address EX.4000
b = False      
print(b)                      # False
print(type(b))                # <class 'bool'>
print(True + True)            # 2
print(True + False)           # 1
print(False + True)           # 1
print(False + False)          # 0
print(True + True + True)     # 3
print(25 + 10.8 + True)       # 36.8
print(True > False)           # True
print(True)                   # True
print(False)                  # False
print(true)                   #Error because of small 't'
print(false)                  #Error because of small 'f'



# Find  outputs (Home  work)
a = 0O6247
print(a)            '''
                       In octal base is 8. So, '8^ will be multiplied by number from right to left
                       So it will be (8^3 *6)+(8^2 *2)+(8^1 *4)+(8^0 *7) 
                       3239
                     '''
print(type(a))       # <class 'int'>
print(id(a))         # some address EX.5000
b = 0o6247           
print(id(b))         # same address will be allocated  to 'b' because of reusable object 'a'
print(b)             # 3239   
c = 3239
print(c)             # 3239
print(id(c))         # same address will be allocated  to 'c' because of reusable object 'a'
print(0o9248)        # Error because 8 and 9 is not in octal base 



# Find  outputs  (Home  work)
a = 0XA7B9         
print(a)           '''
                       In hexadecimal base is 16. So, '16^ will be multiplied by number from right to left
                       So it will be (16^3 *10)+(16^2 *7)+(16^1 *11)+(16^0 *9) 
                       43033
                        '''
                     
print(type(a))       # <class 'int'>
b = 0xBEEF           
print(b)             # 48879      
print(A7B9)          # Error because of there is no prefix 
print('A7B9')        # A7B9
print(0XBEER)        # Error because of 'R' is not in hexadecimal base
print(0XHYD)         # Error because of 'Y' and 'D' is not in hexadecimal base
print(0xA7G9B)       # Error because of 'G' is not in hexadecimal base

# Find outputs (Home  work)
a = 9248 
print(a)          # 9248
print(type(a))    # <class 'int'>