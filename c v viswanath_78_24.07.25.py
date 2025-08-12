print(eval('25'))                     # 25
print(eval('10.8'))                   # 10.8
print(eval('False'))                  # False
print(eval('3+4j'))                   # (3+4j)
print(eval('Hyd'))                    # Error: name 'Hyd' is not defined, treated as variable
print(eval("    'Hyd'   "))           # 'Hyd'
rint(eval('3 + 4 * 5'))              # 23
print(eval('[10 , 20 , 15 , 18]'))    # [10, 20, 15, 18]
print(eval('{10,20,15,18,20,12,18}')) # {10, 12, 15, 18, 20}
print(eval('(10 , 20 , 30)'))         # (10, 20, 30)
print(eval("{10 : 'Hyd' , 10 : 'Sec'}"))  # {10: 'Sec'}
print(eval(4 + 5))                    # Error: eval() argument must be a string, not int

print(eval("    'hyd'   "))        # hyd    => Treated as string literal (with quotes, so it's valid)
hyd = 'Sec'
print(eval('hyd'))                 # sec       => Variable name, evaluates to 'Sec'
sec = '25'
print(eval('sec'))                # 25       => Variable name, evaluates to '25' (still string)
print(eval(sec))                  # 25      => Now evaluates string '25' as number => 25 (int)
cyb = 10.8
print(eval('cyb'))                # 10.8       => Variable name, evaluates to 10.8 (float)
print(eval(cyb))                  # 10.8      => Already float, evaluates to 10.8

print(eval('print("Hyd")'))  #Hyd
    #None

print(bool('False'))       # True     # Non-empty string is always True
print(eval('False'))       # False    # Boolean keyword False (no quotes)
print(bool(''))            # False    # Empty string is False
print(eval('  ""  '))      # ""       # Empty string literal => prints nothing
print(eval(''))            # Error    # Error: empty expression, nothing to evaluate
print(eval('  " "   '))    # " "      # A string with space character => prints one space
print(eval(' '))           # Error    # Error: Non-breaking space (U+00A0) is invalid syntax

x = eval(input('Enter any input: '))     #25
print(type(x))                                     #<class 'int'>
print(x)			            #25
advantage of eval(input()) reads user input and auto-converts it into the correct Python object (int, str, list, etc.) based on what was entered.

a = input('Enter  any  string  :  ')
print(len(a))
print(a)
b = eval(input('Enter   any  string  : '))
print(len(b))
print(b)
Let’s break this down clearly with output and give the better approach:
# Using input()
a = input('Enter any string: ')
print(len(a))
print(a)
# Using eval(input())
b = eval(input('Enter any string: '))
print(len(b))
print(b)
Example Input:
For a: Hyd
For b: 'Hyd'
Output:
Enter any string: Hyd
3
Hyd
Enter any string: 'Hyd'
3
Hyd
⚠️ Key Difference:
•	input() always returns a string as typed — no quotes needed.
•	eval(input()) expects a valid Python string literal (with quotes), or else gives an error.
✅ Better Approach?
input() is better and safer for reading string input, since:
•	It works without requiring quotes.
•	It doesn't evaluate code (so it's more secure).
•	It's the standard method used for user input.
✔️ One-line Summary:
Use input() to read strings — it's simpler and avoids eval() errors or security risks.

a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')       # 25,10.8,Hyd
print(a , b , c , sep = '\t')      # 25<TAB>10.8<TAB>Hyd
print(a , b , c , sep = '---')     # 25---10.8---Hyd
print(a , b , c , sep = '\n')      # 25
                                   # 10.8
                                   # Hyd
print(a , b , c)             # 25 10.8 Hyd
print(a , b , c , separator = ':') # Error: 'separator' is not a valid keyword in print()

a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---')               # 25 10.8 Hyd---
print(a , b , c , sep = ',,,')               # 25,,,10.8,,,Hyd
print(a , b , c , sep = ':::' , end = '\t\t\t')  # 25:::10.8:::Hyd<tab><tab><tab>
print(a , b , c)                             # 25 10.8 Hyd

print('Hyd')       # Hyd
print()            # (prints a blank line)
print('Sec')       # Sec
print()            # (prints a blank line)
print('Cyb')       # Cyb

l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s)   # [10, 20, 30, 40] (10, 20, 30, 40) {40, 10, 20, 30},set may appear in any order

a = 25
b = '%f'  %a
print(b)               # 25.000000
print(type(b))         # <class 'str'>
x = 10.8
y = '%d'  %x
print(y)               # 10
print(type(y))         # <class 'str'>
m = [10 , 20 , 15 , 18]
n = '%s'  %m
print(n)               # [10, 20, 15, 18]
print(type(n))         # <class 'str'>

a = 10.9274
print('%8.2f'  %a)   #   10.93    # Total width 8, 2 digits after decimal (3 spaces before)
print('%9.1f'  %a)   #    10.9    # Total width 9, 1 digit after decimal (4 spaces before)
print('%10.3f' %a)   #   10.927   # Total width 10, 3 after decimal (4 spaces before)
print('%.2f'   %a)   # 10.93      # Only precision, no width
print('%.6f'   %a)   # 10.927400  # 6 digits after decimal
print('%f'     %a)   # 10.927400  # Default: 6 digits after decimal

print('%7s'  % a)        #     Hyd     → right-aligned in 7-width (4 spaces + 'Hyd')
print('%-7s' % a)        # Hyd     → left-aligned in 7-width ('Hyd' + 4 spaces)
print('%2s'  % a)        # Hyd     → width < length, so ignored
print('%s'   % a)        # Hyd     → simple substitution
print('%s' , a)          # ('%s', 'Hyd')  → prints tuple, no formatting applied
print('%s'  a)           # Error: Missing comma between format and value
print('%s' , %a)         # Error: Invalid syntax (`%a` used wrongly)
print(a)                 # Hyd     → direct print

print('%s' % a)       # [10, 20, 30, 40]
print('%s', a)          # ('%s', [10, 20, 30, 40])
print('%s' a)           # Error: invalid syntax
print('%s' , %a)     # Error: invalid syntax
print('%l' % a)     # Error: unsupported format character 'l'
print(a)                # [10, 20, 30, 40]

print('%d    %f    %s'  % (a, b, c))         # 25    10.927400    Hyd
print('%i    %g    %s'  % (a, b, c))         # 25    10.9274    Hyd
print('%s    %s    %s'  % (a, b, c))         # 25    10.9274    Hyd
print('%d    %g    %s' , a , b , c)          # ('%d    %g    %s', 25, 10.9274, 'Hyd')
# print('%d    %g      %s'   a , b , c)      # Error: invalid syntax
# print('%d    %g    %s'  ,  %(a , b , c))   # Error: invalid syntax
# print('%d    %g    %s'    %a%b%c)          # Error: unsupported operand type(s)
print('%d' % a, '%f' % b, '%s' % c)          # 25 10.927400 Hyd
