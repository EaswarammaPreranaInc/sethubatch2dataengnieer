print(eval('25')) #converts string to integer 25
print(eval('10.8')) #converts string to float 10.8
print(eval('False')) #converts string to boolean False
print(eval('3+4j'))     #converts string to complex number 3+4j
print(eval('Hyd')) #converts string to string Hyd
print(eval("    'Hyd'   ")) #converts string to string 'Hyd'
print(eval('3 + 4 * 5')) #evaluates the expression 3 + 4 * 5
print(eval('[10 , 20 , 15 , 18]')) #converts string to list [10, 20, 15, 18]
print(eval('{10,20,15,18,20,12,18}')) #converts string to set {10, 12, 15, 18, 20}
print(eval('(10 , 20 , 30)')) #converts string to tuple (10, 20, 30)
print(eval("{10 : 'Hyd' , 10 : 'Sec'}")) # converts string to dict
print(eval(4+5)) # error because the argument of eval function should be string


print(eval("    'hyd'   "))
hyd = 'Sec' #assigns object hyd to string 'Sec'
print(eval('hyd')) # so here argument of eval is a object hyd which is value Sec
sec = '25' # assigns object sec to string '25'
print(eval('sec')) # so here argument of eval is a object sec which is value 25
print(eval(sec))   #the object sec has value is string 25 so prints 
cyb = 10.8 # assigns object cyb to float 10.8
print(eval('cyb')) # so here argument of eval is a object cyb which is value 10.8
print(eval(cyb)) # error because cyb is not in string or value of cyb is string


print(eval('print("Hyd")')) # we will evaluate inside print function prints Hyd so string Hyd is there in eval function which returns 'hyd'


print(bool('False')) # true because false is a non empty string
print(eval('False')) # converts string false to bool false
print(bool('')) # false because it is a enpty string
print(eval('  ""  ')) # eval function prints nothing beccause empty string so prints empty line
print(eval('')) # error because no expression to evaluate
print(eval('  " "   ')) # eval function prints a space because it evaluates to a string with a space
print(eval('')) # error because no expression to evaluate


x = eval(input('Enter  any  input  :  '))  # takes the input from the user and evaluates  if input is 25 input function 
                                         ##automatically takes it as string so if we eval function again converted to class int
print(type(x)) # class int
print(x) #25


# What  is  a  better  approach  to  read  string  input 
a = input('Enter  any  string  :  ') # takes the input as a string
print(len(a)) # prints the length of the string
print(a) # and print its length and content?
b = eval(input('Enter   any  string  : ')) # takes the input as a string and converts to the relavent object
print(len(b)) # prints the length of the object
print(b) # and print its length and content?
# 1st approach is better as we are unnecessarily ceval function in 2nd method as 1st one takes input as string 


a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')   #   25 , 10.8 , Hyd
print(a , b , c , sep = '\t') # prints 25 10.8 Hyd with a tab space i.e 25  10.8    Hyd   
print(a , b , c , sep = '---') # prints 25 10.8 Hyd with --- between them 25---10.8---Hyd
print(a , b , c , sep = '\n') #prints each one in new line
print(a , b , c) # prints 25 10.8 Hyd with a space between them
print(a , b , c , separator=':') # error because we should use sep not separator


a , b , c = 25 , 10.8 , 'Hyd' # multiple assignment assigns 25 to a, 10.8 to b, and 'Hyd' to c
print(a , b , c , end = '---') #prints 25 10.8 Hyd with '---' at the end
print(a , b , c , sep = ',,,') # prints 25,,,10.8,,,Hyd with ',,,' as separator
print(a , b , c , sep = ':::' , end = '\t\t\t') # prints 25:::10.8:::Hyd with ':::' as separator and tabs at the end
print(a,b,c) # prints 25 10.8 Hyd with default space separator and newline at the end


print('Hyd') #printing the first line
print()#prints a empty line
print('Sec') #printing the second line
print()#prints a empty line
print('Cyb') #printing the third line


l = [10 , 20 , 30 , 40] # assignment of list
t = (10 , 20 , 30 , 40) # assignment of tuple
s = {10 , 20 , 30 , 40} # assignment of set
print(l,t,s) # Output: [10, 20, 30, 40] (list), (10, 20, 30, 40) (tuple), {10, 20, 30, 40} (set)


a = 25 # assigns a to object 25
b = '%f'  %a # converts a to string float with 6 digits
print(b) # printing b 25.000000
print(type(b)) #cls str
x = 10.8 #assign x to 10.8
y = '%d'  %x # converts x to string integer
print(y) # 10
print(type(y)) #class str
m = [10 , 20 , 15 , 18] # list of integers
n = '%s'  %m # converts m to string list
print(n) #' [10, 20, 15, 18]'
print(type(n)) #class str


a = 10.9274 # float variable
print('%8.2f'  %a)  #  <3  spaces>10.93
print('%9.1f'  %a) #  <5  spaces>10.9
print('%10.3f'  %a) #  <4  spaces>10.927
print('%.2f'  %a) # 10.93
print('%.6f'  %a) # 10.927400
print('%f' %a) # 10.927400


a = 'Hyd'
print('%7s'  %a)   #  <4  spaces>Hyd
print('%-7s'  %a)  #  Hyd<4   spaces>
print('%2s'  %a)   #  Hyd  and  ignores  smaller width
print('%s'  %a)  #  Hyd
print('%s' , a) # prints %s an object a
print('%s'  a)#error because missing comma or %
print('%s',%a) # error because % is not used correctly
print(a) # prints the string a


a = [10 , 20 , 30 , 40] # assigns list
print('%s'  %a) # converts list to string
print('%s' , a) # prints %s and list with space
print('%s'  a) # error because , or % is missing
print('%s' , %a) # format is a single object so no comma 
print('%l'%a) #error
print(a) # prints a

a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c)) # convets a into int b to float c to string
print('%i    %g    %s'    %(a , b , c)) # converts a into int b to float c to string
print('%s    %s    %s'  %(a , b , c))# converts a into string b to string c to string
print('%d    %g    %s'  , a , b , c) # this will give an error
print('%d    %g      %s'   a , b , c) # this will give an error
print('%d    %g    %s'  ,  %(a , b , c))# this will give an error
print('%d    %g    %s'    %a%b%c)# this will give an error
print('%d'    %a  ,  '%f'     %b,'%s'%c) #