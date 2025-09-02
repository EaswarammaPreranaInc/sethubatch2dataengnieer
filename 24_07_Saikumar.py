# eval() function demo program

print(eval('25'))                         # Converts string '25' to integer 25
print(eval('10.8'))                       # Converts string '10.8' to float 10.8
print(eval('False'))                      # Converts string 'False' to boolean False
print(eval('3+4j'))                       # Converts string '3+4j' to complex number (3+4j)
print(eval('Hyd'))                        # Error 'Hyd' is not defined
print(eval("    'Hyd'   "))               # Converts string to string value 'Hyd', spaces ignored
print(eval('3 + 4 * 5'))                  # Converts string expression to result 3 + (4*5) = 23
print(eval('[10 , 20 , 15 , 18]'))        # Converts string to list [10, 20, 15, 18]
print(eval('{10,20,15,18,20,12,18}'))     # Converts string to set {10, 12, 15, 18, 20}
print(eval('(10 , 20 , 30)'))             # Converts string to tuple (10, 20, 30)
print(eval("{10 : 'Hyd' , 10 : 'Sec'}"))  # Converts string to dictionary {10: 'Sec'}
# print(eval(4 + 5))                      # Error argument to eval must be a string, not int


# Tricky program
# Find outputs (Home work)

print(eval("    'hyd'   "))       # Converts string to string value 'hyd', output: 'hyd'
hyd = 'Sec'                       # Assigns string 'Sec' to variable hyd
print(eval('hyd'))                # Converts string 'hyd' to variable name hyd, output: 'Sec'
sec = '25'                        # Assigns string '25' to variable sec
print(eval('sec'))                # Converts string 'sec' to variable sec output: '25'  
print(eval(sec))                  # Converts value of sec i.e. '25' to integer output: 25
cyb = 10.8                        # Assigns float 10.8 to variable cyb
print(eval('cyb'))                # Converts string 'cyb' to variable cyb, output: 10.8
print(eval(cyb))                  # Error eval() expects a string, but 10.8 is float


# Tricky program
# Find output (Home work)

print(eval('print("Hyd")'))   # First, eval() converts the string to a statement print("Hyd")
                              # This prints "Hyd" to the console
                              # The print() function returns None, so outer print(None) is executed


# Find outputs (Home work)

print(bool('False'))           # True 
print(eval('False'))           # False 
print(bool(''))                # False 
print(eval('  ""  '))          # "", eval evaluates to an empty string
# print(eval(''))              # Error  empty string is not valid 
print(eval('  " "   '))        # " ", eval evaluates to a string with a single space
# print(eval(' '))             # Error contains a invalid character 


# What is the advantage of eval(input())?

x = eval(input('Enter any input : '))  # Accepts any value and converts to equivalent object
print(type(x))                         # Prints the type of the x
print(x)                               # Prints the actual value entered


# What is a better approach to read string input?

a = input('Enter any string : ')        # Always returns input as a string
print(len(a))                           # Prints the number of characters in the string
print(a)                                # Prints the entered string
b = eval(input('Enter any string : '))  # Evaluates the input as a Python expression
print(len(b))                           # Prints length only if input is a valid string object
print(b)                                # Prints the evaluated result


# sep argument demo program (Home work)

a, b, c = 25, 10.8, 'Hyd'                     # Assign values to objects a, b and c
print(a, b, c, sep=',')                       # Uses ',' as separator 25,10.8,Hyd
print(a, b, c, sep='\t')                      # Uses tab space between values
print(a, b, c, sep='---')                     # Uses '---' as separator 25---10.8---Hyd
print(a, b, c, sep='\n')                      # Prints each value on a new line
print(a, b, c)                                # Default separator is a space 25 10.8 Hyd
print(a, b, c, separator=':')                 # Error 'separator' is not a valid 


# Find outputs (Home work)

a, b, c = 25, 10.8, 'Hyd'                # Assign values to variables a, b, and c
print(a, b, c, end='---')                # Prints a, b, c with default space separator, ends with '---'
print(a, b, c, sep=',,,')                # Prints a, b, c separated by ',,,' and ends with a newline 
print(a, b, c, sep=':::', end='\t\t\t')  # Prints a, b, c separated by ':::' and ends with 3 tabs
print(a, b, c)                           # Prints a, b, c with space separator and newline


# Find outputs (Home work)

print('Hyd')     # Prints 'Hyd' moves to nextline
print()          # Prints a blank line
print('Sec')     # Prints 'Sec' moves to nextline
print()          # Prints another blank line
print('Cyb')     # Prints 'Cyb' moves to nextline


# Find outputs (Home work)

l = [10, 20, 30, 40]          # Creates a list
t = (10, 20, 30, 40)          # Creates a tuple
s = {10, 20, 30, 40}          # Creates a set
print(l, t, s)                # Prints the [10, 20, 30, 40]<space>(10, 20, 30, 40)<space>{10, 20, 30, 40}


# Find outputs (Home work)

a = 25
b = '%f' % a                  # Converts integer 25 to float string format '25.000000'
print(b)                      # Prints 25.000000
print(type(b))                # Prints <class 'str'> 
x = 10.8
y = '%d' % x                  # Converts float 10.8 to integer format '10'
print(y)                      # Prints 10
print(type(y))                # Prints <class 'str'>
m = [10, 20, 15, 18]
n = '%s' % m                  # Converts the list to string format '[10, 20, 15, 18]'
print(n)                      # Prints [10, 20, 15, 18]
print(type(n))                # Prints <class 'str'>


# Find Outputs (Home work)

a = 10.9274
print('%8.2f' % a)     # Prints float a with 2 decimal places, total width = 8 characters "   10.93"
print('%9.1f' % a)     # Prints float a with 1 decimal place, total width = 9 characters "     10.9"
print('%10.3f' % a)    # Prints float a with 3 decimal places, total width = 10 characters "    10.927"
print('%.2f' % a)      # Prints float a with 2 decimal places, no width constraint "10.93"
print('%.6f' % a)      # Prints float a with 6 decimal places "10.927400"
print('%f' % a)        # Default float "10.927400"


# Find outputs (Home work)

a = 'Hyd'
print('%7s' % a)     # Prints the string right-aligned in a field of width 7 "    Hyd"
print('%-7s' % a)    # Prints the string left-aligned in a field of width 7 "Hyd    "
print('%2s' % a)     # Since length of 'Hyd' is 3, width 2 is ignored "Hyd"
print('%s' % a)      # Prints the string as is "Hyd"
print('%s' , a)      # prints the '%s' and then value a ("%s", "Hyd")
print('%s' a)        # Error Missing operator %
print('%s' , %a)     # Error invalid syntax
print(a)             # Prints the value of a "Hyd"


# Find outputs (Home work)

a = [10, 20, 30, 40]
print('%s' % a)       # Converts the list to string and prints "[10, 20, 30, 40]"
print('%s', a)        # Prints the string '%s' and the list separately as a tuple ("%s", [10, 20, 30, 40])
print('%s' a)         # Error comma between format string and object
print('%s' , %a)      # Error use of % symbol
print('%l' % a)       # Error use of character 'l'
print(a)              # Directly prints the list -> [10, 20, 30, 40]


# Find outputs (Home work)

a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  % (a, b, c))           # prints 25<space>10.927400<space>'Hyd' 
print('%i    %g    %s'  % (a, b, c))           # prints 25<space>10.927400<space>'Hyd'
print('%s    %s    %s'  % (a, b, c))           # prints 25<space>10.927400<space>'Hyd'
print('%d    %g    %s', a, b, c)               # prints ("%d    %g    %s", 25, 10.9274, 'Hyd')
print('%d    %g      %s'   a , b , c)          # Error missing '%' between string and objects
print('%d    %g    %s'  ,  %(a , b , c))       # Error comma before '%'
print('%d    %g    %s'    %a%b%c)              # Error invalid usage of '%' chaining
print('%d' % a, '%f' % b, '%s' % c)            # Each value formatted separately