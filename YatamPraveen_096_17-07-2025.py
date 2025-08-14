# int() function demo program 
print(int(10.8))		 # Converts float object 10.8 to int object 10 
print(int(True))		 # Converts bool object True to int object 1 
print(int(False))		 # 0 
print(int('25')) 		 # 25 
print(int('0075'))		 # Returns error as the string has 00 at beginning 
print(int(0B11010))		 #26 
print(0B11010)			 #26 
print(int(0O6247))		 #3247 
print(0O6247) 			 #3247 
print(int(0XA7B9))		 #42937 
print(0XA7B9) 			 #42937 
print(int(3 + 4j)) 		 # returns error as comp can't be converted into int 
print(int('25.4'))               # returns error since there is a decimal print(int('Ten')) # returns error since if is a string

 ''' int() function ---------------- 1) What does int(x) do ? ---> Converts object 'x' to integer



# float() function demo program 
print(float(25))                  # Converts int object 25 to float object 25.0 
print(float(True))                 # Converts bool object True to float object 1.0 
print(float(False))                # 0.0 
print(float('92'))                 # 92.0 
print(float('36.4'))                # 36.4 
print(float('0075'))               # returns error as there are 0's at beginning 
print(float(0B1010101))            # 85.0 
print(float(0O6247))               # 3247.0 
print(float(0XA7B9))               # 42937.0 
print(float(3 + 4j))                # returns error as complex can't be converted 
print(float('Ten'))                 # returns error as it is a string


''' float() function -------------------- 1) What does float(x) do ? ---> Converts object 'x' to float




# bool() function demo program 
print(bool(0))             # False 
print(bool(10))            # True : 10 is non-zero 
print(bool(-25))           # True 
print(bool(0.0))           # False 
print(bool(0.1))           # True 
print(bool(0 + 0j))        # False 
print(bool(10 + 20j))      # True 
print(bool(-15j))          # True 
print(bool('False'))       # True 
print(bool(''))            # False 
print(bool('Hyd'))         # True 
print(bool(' '))           # True 
print(bool('True'))        # True


''' bool() function ------------------ 
1) What does bool(x) do ? ---> Converts object 'x' to True / False 
2) Is 0 True (or) False ? ---> False What about non-zero ? ---> True 
3) Is ''(i.e. Empty string) True (or) False ? ---> False What about non-empty string ? ---> True 
4) When is x + yj treated as False ? ---> When both 'x' and 'y' are zeroes When is x + yj treated as True ? ---> When either 'x' is non-zero (or) 'y' is non-zero '''




# str() function demo program 
print(str(25)) # Converts 25 to '25' 
print(str(10.8)) # '10.8' 
print(str(3 + 4j)) # '3 + 4j' 
print(str(True)) # 'True' 
print(str(False)) # 'False' 
print(str(None)) # 'None' 

''' What does str(x) do ? ---> Converts object 'x' to string '''




# oct() function demo program 
print(oct(195)) # 0o303 
print(oct(0B10101110010)) # 002722 
print(oct(0xA7B9)) # 0o247371 

''' oct() function ----------------- 1) What does oct(x) do ? ---> Converts object 'x' to octal number where 'x' can be binary / decimal / hexa-decimal number




# hex() function demo program 
print(hex(25)) # 0x19 
print(hex(0B10101111010111)) # 0xAFD7 
print(hex(0O6247)) # 0xCAF

 ''' hex() function ------------------ 1) What does hex(x) do ? ---> Converts object 'x' to hexa-decimal number where 'x' can be binary / decimal / octal number




# Find  outputs    (Home  work)
a = range(10 , 50 , 5)
print(type(a))     #<class 'range'>
print(a)      #range(10, 50, 5)
print(*a)     #10 15 20 25 30 35 40 45
print(id(a))     # Returns the address of object range(10, 50, 5)
print(len(a))       #8
print(*a[2 : 7] , sep = ' , ')  #20, 25, 30, 35, 40
print(*a[ : : -1])      #45 40 35 30 25 20 15 10
a[4] = 32     # This statement causes error as range object is immutable
print(a * 2)    #This operation is invalid for range objects.





#  Find  outputs  (Home  work)
a = range(10 , 20)
print(*a , sep = ',')     #10, 11, 12, 13, 14, 15, 16, 17, 18, 19
b = range(5)
print(*b)         #0 1 2 3 4
c = range(10 , 1 , -1)
print(*c , sep = '...')       #10...9...8...7...6...5...4...3...2
d = range(-10 , 0)
print(*d)         #-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
e = range(-10)
print(*e)         # No output as beginning is 0 and ending -10 and step is 1 by default. But 0 can never reach -10 with 1 as step.
f = range(2 , 2)
print(*f)               # No output as range is empty.
g = range(10 , 11 , 0.1)     # returns error as range is homogeneous and can't have float values 
h = range('A' , 'F')     #returns error as range can't have string values.




#  Find  outputs  (Home  work)
r = range(10 ,  17 , 3)
a , b , c = r
print(a , b , c)      #10 13 16
r = range(3)
x , y = r               #r has values 0, 1 and 2. But it is being assigned only to x and y. So this line causes error
p , q  , r , s = r   # 4 variables are used to assign 3 values. So this line also causes error.
a , b , c = *r     #when more than one variable is used for assigning a range object, automatically the values are assigned to respective variables. No need of *. Hence this raises error.