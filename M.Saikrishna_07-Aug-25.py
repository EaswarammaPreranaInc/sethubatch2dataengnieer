try:
    from sys import argv
    nums = [float(x) for x in argv[1:]]
    print("Args:", nums)
    print("Largest:", max(nums))
except:
    print("the input should be an float")

try:
    from sys import argv
    n = int(argv[1])
    print("even" if n % 2 == 0 else "odd")
except:
    print("the input should be  an integer")

try:
    from sys import argv
    nums = [float(x) for x in argv[1:]]  
    avg = sum(nums) / len(nums)          
    print("Average:", avg)
except :
    print("Only numeric input is valid")
try:
    from sys import argv
    print("argv:", argv)
    a = [float(x) for x in argv[1:]]
    print("list a:", a)
    print("Ascending:", sorted(a))
    print("Descending:", sorted(a, reverse=True))
except:
    print("Input type should be an int")

print( 'green'   in   'Hyd  is  green  city') # True
print('day'   in   'Sankar  dayal  sarma')    # True
print('Green'   in   'Hyd  is  green  city')  # False
print('d  is'   in   'Hyd  is  green  city')  # True
print('dis'   in   'Hyd  is  green  city')    # False
print('iniv'   in   'Srinivas')               # True
print('iniv'   not   in   'Srinivas')         # False

a = 'Rama Rao'
print(a [ : 7 : 2])    # Rm a
print(a [ : 7])        # Rama Ra
print(a [2 : 4])       # ma
print(a [2 : ])        # a Rao
print(a [ : 4 ])       # Rama
print(a [ : : 2])      # Rm a
print(a [-6 : -1])     # ma Ra
print(a [-6 : ])       # ma Rao
print(a [: -4 : -1])   # oaR
print(a [-3 : -1])     # Ra
print(a [-3 : -1]) #  a[-3 : -1 : 1]  --->  string  from  indexes  -3  to  -2  in  steps  of  1  i.e.  Ra
print(a [-3 : ])   # Rao
print(a [ : : ])   # Rama Rao
print(a [ : ])     # Rama Rao
print(a [ : : -1]) # oaR amaR
print(a [ : : -2]) # oRaa
print(a [ -2 : : -2])  #  a[-2 : -9 : -2]  --->  string  from  indexes  -2  to  -8  in  steps  of  -2  i.e.  a<space>mR
print(a [2 : 8])       # ma Rao
print(a [2 : 8 : -1])  #
print(a [ : -6 : -1])  # oaR a
print(a [2 : -3])      # ma 
print(a [1 : 6 : 2])   # aaR
print(a [ : -5 : -5])  # o 
print(a [2 : -5])      # m
print(a [2 : -5 : 2])  # m
print(a [ : 0 : -1])   # oaR ama
print(a [-5 : 0 : -2]) # aa


s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
result = s2[:2] + s1[2:] + " " + s1[:2] + s2[2:]
print(result)


s = input("Enter a string: ")

if len(s) < 4:
    print("")   # Empty string
else:
    print(s[:2] + s[-2:])

s = input("Enter a string: ")
for i in range(len(s)):
    print(f"Character at index {i} : {s[i]}")
for i in range(-1, -len(s)-1, -1):
    print(f"Character at index {i} : {s[i]}")

s = input("Enter the string: ") 
out = ""
for i in range(0, len(s), 2):   
    out += s[i] * int(s[i + 1])
print(out)

a = input("Enter first string: ")   
b = input("Enter second string: ")  
c = ""
i = 0
while i < len(a) and i < len(b):
    c += a[i] + b[i]
    i += 1
c += a[i:] + b[i:]
print(c)

print(len('Hyd'))       #  3 
print(len('Rama Rao'))  #  8 
print(len('9247'))      #  4 
print(len('+-$'))       #  3
print(len(''))          #  0 
print(len(' '))         #  1 
print(len('A2#'))       #  3
print(len(3456))        #  error
print('Sec'. len())     # SyntaxError

print(chr(65))   # A  
print(chr(90))   # Z  
print(chr(97))   # a  
print(chr(122))  # z  
print(chr(48))   # 0  
print(chr(57))   # 9  
print(chr(36))   # $  
print(chr(32))   #<space>

print(ord('A'))  # 65  
print(ord('Z'))  # 90  
print(ord('a'))  # 97  
print(ord('z'))  # 122 
print(ord('0'))  # 48 
print(ord('9'))  # 57  
print(ord('$'))  # 36 
print(ord(' '))  # 32  



