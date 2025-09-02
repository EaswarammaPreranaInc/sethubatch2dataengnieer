# input function()
x=input('Enter input:')     # reads string input to object 'x'
print(type(x))              # <class 'str'>
print(x)                    # user input


#How to read integer input
try:
    x=int(input('Enter any integer number:'))       # read string input and converts to integer
    print(type(x))                                  # <class 'int'>
    print(x)                                        # user input
except:
    print('Input should be integer')


#How to read float input 
try:
    x=float(input('Enter float number:'))           # reads string input and converts to float
    print(type(x))                                  # <class 'float'>
    print(x)                                        # user input
except:
    print('Input should be float or integer')


#bool input
x=bool(input('Enter boolean input:'))       
print(type(x))                          # <class 'bool'>
print(x)                                # True or False


# How to read complex input
try:
    x=complex(input('Enter complex number:'))           # reads string input and converts to complex
    print(type(x))                                      # <class 'complex'>
    print(x)                                            # user input
except:
    print('Input should be a complex number')


# input(no-args)
x=input()               # reads string input
print(type(x))          # <class 'str'>
print(x)                # user input


# eval()  function  demo  program
print(eval('25'))                           # converts '25' to 25
print(eval('10.8'))                         # converts '10.8' to 10.8
print(eval('False'))                        # converts 'False' to False
print(eval('3+4j'))                         # converts '3+4j' to 3+4j
#print(eval('Hyd'))                         # error
print(eval("    'Hyd'   "))                 # converts " 'Hyd' " to 'Hyd'
print(eval('3 + 4 * 5'))                    # converts '23' to 23
print(eval('[10 , 20 , 15 , 18]'))          # converts '[10 , 20 , 15 , 18]' to [10 , 20 , 15 , 18]
print(eval('{10,20,15,18,20,12,18}'))       # converts '{10,20,15,18,20,12,18}' to {10,20,15,18,12}
print(eval('(10 , 20 , 30)'))               # converts '(10 , 20 , 30)' to (10 , 20 , 30)
print(eval("{10 : 'Hyd' , 10 : 'Sec'}"))    # converts "{10 : 'Hyd' , 10 : 'Sec'}" to {10 : 'Sec'}
#print(eval(4 + 5))                         # error argument should be string


#  assignment 2
print(eval("    'hyd'   "))                 # converts " 'hyd' " to 'hyd'
hyd = 'Sec'
print(eval('hyd'))                          # converts 'hyd' to object hyd which is 'Sec'
sec = '25'
print(eval('sec'))                          # converts 'sec' to object sec which is '25
print(eval(sec))                            # converts object sec '25' to integer 25
cyb = 10.8
print(eval('cyb'))                          # converts 'cyb' to object cyb to 10.8
#print(eval(cyb))                           # error 



#  Find  output  (Home  work)
print(eval('print("Hyd")'))             # print(print("Hyd")) --> print(None) --> None

#output
'''
Hyd
None
'''


#  Find  outputs  (Home  work)
print(bool('False'))                # True : 'False' is a non-empty string
print(eval('False'))                # converts 'False' to False
print(bool(''))                     # converts '' to False
print(eval('  ""  '))               # converts ' "" ' to ""
#print(eval(''))                    # converts '' to nothing
print(eval('  " "   '))             # converts ' " " ' to " "
#print(eval(' '))                   # converts ' ' to nothing


# What  is  the  advantage  of  eval(input()) ?
try:
    x = eval(input('Enter  any  input  :  '))
    print(type(x))
    print(x)
except:
    print('Input string should be in quotes')

'''
it can read any kind of input
'''

# What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ')                # 'Hyd'
print(len(a))                                       # 3
print(a)                                            # Hyd
b = eval(input('Enter   any  string  : '))          # 'Hyd'
print(len(b))                                       # 3
print(b)                                            # Hyd
