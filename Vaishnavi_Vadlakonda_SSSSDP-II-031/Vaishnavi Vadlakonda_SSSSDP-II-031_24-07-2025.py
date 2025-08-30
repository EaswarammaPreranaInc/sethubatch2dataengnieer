# eval()  function  demo  program
print(eval('25')) # converts string to integer object and prints 25
print(eval('10.8')) # converts string to float object and prints 10.8
print(eval('False')) # converts string to bool object and prints False
print(eval('3+4j')) # converts string to complex object and prints (3 + 4j)
print(eval('Hyd')) # Error because 'Hyd' should be in string in string 
print(eval("     'Hyd'   ")) # prints     'Hyd'     
print(eval('3 + 4 * 5')) # converts string to integer object and prints 23
print(eval('[10 , 20 , 15 , 18]')) # converts string to list object and prints [10, 20, 15, 18]
print(eval('{10,20,15,18,20,12,18}')) # converts string to set object and removes duplicates and prints {10, 20, 15, 18, 12}
print(eval('(10 , 20 , 30)')) # converts string to tuple object and prints (10, 20, 30)
print(eval("{10 : 'Hyd' , 10 : 'Sec'}")) # converts string to dict object and prints {10 : 'Sec'}
print(eval(4 + 5)) # Error because argument should be string










#  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   ")) # prints string object i.e., hyd
hyd = 'Sec' # hyd points to string object 'Sec'
print(eval('hyd')) # prints Sec
sec = '25' # sec points to string object '25'
print(eval('sec')) # converts string object '25' to string object and prints '25'
print(eval(sec)) # converts string object '25' to integer object and prints 25
cyb = 10.8 # cyb points to float object 10.8
print(eval('cyb')) # converts string object '10.8' to float object and prints 10.8
print(eval(cyb)) # Error because must be in strings







#  Tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")')) # first it evaluates inner print i.e., eval(print("Hyd")), it gives Hyd as output and returns None and now it evaluates outer print i.e., print(None) and prints None










#  Find  outputs  (Home  work)
print(bool('False')) # prints True because it treats non empty string as True 
print(eval('False')) # converts string object to bool object and prints False
print(bool('')) # prints False because empty string treated as False
print(eval('  ""  ')) # prints a blank line
print(eval(''))  # Error  because there no argument
print(eval('  " "   ')) # prints a space
print(eval(' ')) # Error because there no argument



# What   the  advantage  of  eval(input()) ?
x = eval(input('Enter any input  :  ')) # reads string input from keyboard or user and converts string input to appropriate class object and assigns to object 'x'
print(type(x)) # prints the type of x
print(x) # prints object 'x'









# What   a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ') # reads input from user as string object and gives to 'a'
print(len(a)) # prints number of characters in object 'a'
print(a) # prints object 'a'
b = eval(input('Enter   any  string  : ')) # reads input from user as string and converts it into appropriate class object
print(len(b)) # prints number of characters or length of object 'b'
print(b) # prints object 'b'









# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd' # Ref a points to integer object 25,ref b points to float object 10.8 and ref c points to string object 'Hyd'
print(a , b , c , sep = ',')   #   25 , 10.8 , Hyd
print(a , b , c , sep = '\t')  # 25<tab>10.8<tab>Hyd
print(a , b , c , sep = '---') # 25---10.8---Hyd
print(a , b , c , sep = '\n')  # 25<nextline>10.8<nextline>Hyd<nextline>
print(a , b , c)  # prints 25<space>10.8<space>Hyd in next line
print(a , b , c , separator = ':') # Error because separator keyword not present in builtins module, only sep










# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd' # Ref a points to integer object 25,ref b points to float object 10.8 and ref c points to string object 'Hyd'
print(a , b , c , end = '---') # prints 25 10.8 Hyd--- and stays in same line
print(a , b , c , sep = ',,,') # prints 25,,,10.8,,,Hyd in same line and goes to next line
print(a , b , c , sep = ':::' , end = '\t\t\t') # prints 25:::10.8:::Hyd<tab><tab><tab> in next line and stays in same line 
print(a , b, c) # prints 25 10.8 Hyd in same line 










# Find outputs  (Home  work)
print('Hyd') # prints Hyd and moves to next line
print() # prints nothing and moves to next line
print('Sec') # prints Sec and moves to next line
print() # prints nothing and moves to next line
print('Cyb') # prints Cyb and moves to next line











# Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40] # ref l points to list
t = (10 , 20 , 30 , 40) # ref t points to tuple
s = {10 , 20 , 30 , 40} # ref s points to set
print(l , t , s) # prints [10 , 20 , 30 , 40]<space>(10 , 20 , 30 , 40)<space>{10 , 20 , 30 , 40}








#  Find  outputs (Home  work)
a = 25 # ref 'a' points to integer object 25
b = '%f'  %a # ref 'b' points object '%f' %a
print(b) # converts integer object to string object and prints '25.000000'
print(type(b)) # prints type of object i.e., <class 'str'>
x = 10.8 # ref 'x' points to integer object 25
y = '%d'  %x # ref 'y' points to object '%d' %x
print(y) # converts float object to string object and prints '10'
print(type(y))  # prints type of object i.e., <class 'str'>
m = [10 , 20 , 15 , 18] # ref 'm' points list
n = '%s'  %m # ref 'n' points object '%s' %m
print(n) # converts list to string object and prints '[10, 20, 15, 18]'
print(type(n)) # prints type of object i.e., <class 'str'>










# Find  Outputs  (Home  work)
a = 10.9274 # ref 'a' points to float object i.e., 10.9274
print('%8.2f'  %a)  # prints <3 spaces>10.93
print('%9.1f'  %a) # prints <5 spaces>10.9
print('%10.3f'  %a) # prints <4 spaces>10.930
print('%.2f'  %a) # prints 10.93
print('%.6f'  %a) # prints 10.930000
print('%f'  %a) # prints 10.9274










# Find  outputs (Home  work)
a = 'Hyd'
print('%7s'  %a)  # prints <4 spaces>Hyd
print('%-7s'  %a) # prints Hyd<4 spaces>
print('%2s'  %a) # prints Hyd and ignores smaller width
print('%s'  %a) # prints Hyd
print('%s' , a) # prints %s<space>Hyd
print('%s'  a) # Error because either comma or % should be there
print('%s' , %a) # Error because comma should not be there
print(a) # prints Hyd












# Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40] # ref 'a' points to list
print('%s'  %a) # converts list into string and prints '[10, 20, 30, 40]'
print('%s' , a) # prints %s<space>'[10, 20, 30, 40]'
print('%s'  a) # Error, either ',' or '%' should be there
print('%s' , %a) # Error because ',' should not be there ,because it single argument
print('%l'  %a) # Error because there is no %l
print(a) # prints [10, 20, 30, 40]










#Find outputs  (Home  work)
a = 25 # ref 'a' points to integer object 25
b = 10.9274 # ref 'b' points to float object 10.9274
c = 'Hyd' # ref 'c' points to string object 'Hyd'
print('%d    %f    %s'  %(a , b , c)) # prints 25<spaces>10.927400<spaces>'Hyd'
print('%i    %g    %s'    %(a , b , c)) # prints 25<spaces>10.9274<spaces>'Hyd'
print('%s    %s    %s'  %(a , b , c)) # prints '25'<spaces>'10.9274'<spaces>'Hyd'
print('%d    %g    %s'  , a , b , c) # prints %d %g %s  25<spaces>10.9274<spaces>'Hyd'
print('%d    %g      %s'   a , b , c) # Error because either comma or percentile must be there
print('%d    %g    %s'  ,  %(a , b , c)) # Error because comma should not be there, it only one argument
print('%d    %g    %s'    %a%b%c) # Error because arguments are not sufficient
print('%d'    %a  ,  '%f'     %b ,  '%s'   %c) # prints 25<space>10.927400<space>Hyd
