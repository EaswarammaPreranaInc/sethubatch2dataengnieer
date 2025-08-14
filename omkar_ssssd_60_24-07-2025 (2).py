\############################################# 224



\# eval()  function  demo  program

print(eval('25')) # 25 

print(eval('10.8')) # 10.8 

print(eval('False')) # False 

print(eval('3+4j')) # 3+4j

print(eval('Hyd')) # Hyd 

print(eval("    'Hyd'   ")) # Hyd

print(eval('3 + 4 \* 5')) # 23 

print(eval('\[10 , 20 , 15 , 18]')) # \[10,20,15,18]

print(eval('{10,20,15,18,20,12,18}')) # {10,20,15,18,12}

print(eval('(10 , 20 , 30)')) #(10,20,30)

print(eval("{10 : 'Hyd' , 10 : 'Sec'}")) # {10:'Sec'}

print(eval(4 + 5)) # error 



\###########################################



\#  Tricky  program

\# Find  outputs  (Home  work)

print(eval("    'hyd'   ")) # hyd

hyd = 'Sec'

print(eval('hyd')) # Sec  -----------print hyd but hyd = 'Sec'

sec = '25'

print(eval('sec')) # 25

print(eval(sec)) # 25

cyb = 10.8

print(eval('cyb')) # 10.8

print(eval(cyb)) # error 



\##########################################



\#  Tricky  program

\#  Find  output  (Home  work)

print(eval('print("Hyd")')) # Hyd 



\#########################################



\#  Find  outputs  (Home  work)

print(bool('False')) # True

print(eval('False')) # False 

print(bool('')) **# False**

print(eval('  ""  ')) # empty-str

print(eval('')) # error

print(eval('  " "   ')) # a single <space> character 

print(eval(' ')) **# error

####################################**



# What  is  the  advantage  of  eval(input()) ?

x = eval(input('Enter  any  input  :  ')) ## enter any input 123  , input takes it as '123' , then eval function removes '' strings 

print(type(x))  ## <class 'int'>

print(x) ## 123

####################################



# What  is  a  better  approach  to  read  string  input ?

a = input('Enter  any  string  :  ') ## \[10,20,30] it takes the as '\[10,20,30]'

print(len(a)) # 3 

print(a) <class 'list'>

b = eval(input('Enter   any  string  : ')) ## ('True') 

print(len(b))  # 4 

print(b) # <class boolan>



#######################################

# sep  argument  demo  program  (Home  work)

a , b , c = 25 , 10.8 , 'Hyd' 

print(a , b , c , sep = ',')   ##  25 , 10.8 , Hyd

print(a , b , c , sep = '\\t')  ## 25<tab>10.8<tab>Hyd

print(a , b , c , sep = '---') ## 25---10.8---Hyd

print(a , b , c , sep = '\\n')  ## 25<nextline>10.8<nextline>Hyd

print(a , b , c) ## 25 10.8 Hyd

print(a , b , c , separator = ':') ## 25:10.8:Hyd

#######################################

# Find outputs  (Home  work)

print('Hyd') ## Hyd 

print() # 

print('Sec') # Sec

print() # 

print('Cyb') # Cyb

############################################
# Find  outputs  (Home  work)

a , b , c = 25 , 10.8 , 'Hyd'

print(a , b , c , end = '---') ##  25 , 10.8 , Hyd---

print(a , b , c , sep = ',,,') ## 25,,,10.8,,,Hyd

print(a , b , c , sep = ':::' , end = '\\t\\t\\t') 25:::10.8:::Hyd'\\t\\t\\t'

print(a , b , c) ## 25 , 10.8 , Hyd

##############################################

#  Find  outputs (Home  work)

a = 25

b = '%f'  %a ## 25.0

print(b) ## '25.000000'

print(type(b)) ## <class 'Str'> 

x = 10.8

y = '%d'  %x ## 10.0000

print(y) ## '10.0000'

print(type(y)) # < class 'Str' > 

m = \[10 , 20 , 15 , 18]

n = '%s'  %m ## '\[10,20,15,18]'

print(n) ## \[10 , 20 , 15 , 18]

print(type(n)) # <class 'str'>

#############################################


\# Find  Outputs  (Home  work)

a = 10.9274

print('%8.2f'  %a)  #  <3  spaces>10.93

print('%9.1f'  %a) # <6 spaces >10.9 

print('%10.3f'  %a)  # <4 spaces>10.927

print('%.2f'  %a) # 10.93 

print('%.6f'  %a) # 10.927400

print('%f'  %a) # 10.927400


###########################################

# Find  outputs (Home  work)
a = 'Hyd'
print('%7s'  %a)   #  <4  spaces>Hyd 
print('%-7s'  %a)  #  Hyd<4   spaces>
print('%2s'  %a)   #  Hyd  and  ignores  smaller width
print('%s'  %a) # Hyd 
print('%s' , a) # '%s' , Hyd
print('%s'  a) # error 
print('%s' , %a) # Hyd
print(a) # Hyd

######################################################


# Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40]
print('%s'  %a) ## [10,20,30,40]
print('%s' , a) ## '%s' , [10,20,30,40]
print('%s'  a) ## error 
print('%s' , %a) ## error
print('%l'  %a) ## error due to %l
print(a) ## [10,20,30,40]

###################################################

#Find outputs  (Home  work)
a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c))  ## 25  10.927400  Hyd 
print('%i    %g    %s'    %(a , b , c)) ## 25 10.9274 Hyd
print('%s    %s    %s'  %(a , b , c))  ## 25 10.9274 Hyd
print('%d    %g    %s'  , a , b , c) ## ('%d %g %s',25,10.9274,'Hyd')
print('%d    %g      %s'   a , b , c) ## error 
print('%d    %g    %s'  ,  %(a , b , c)) ## error 
print('%d    %g    %s'    %a%b%c) ## error 
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c) ## 25 10.927400 Hyd 
