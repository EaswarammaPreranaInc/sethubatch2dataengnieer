# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')            #   25 , 10.8 , Hyd
print(a , b , c , sep = '\t')           # 25 <tab> 10.8 <tab> Hyd
print(a , b , c , sep = '---')          # 25---10.8---Hyd
print(a , b , c , sep = '\n')           # 25 <next line> 10.8 <next line> Hyd
print(a , b , c)                        # 25 <space> 10.8 <space> Hyd
#print(a , b , c , separator = ':')     # error no seperator for print function



# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---')                      # 25 <space> 10.8 <space> hyd ---
print(a , b , c , sep = ',,,')                      # 25,,,10.8,,,Hyd
print(a , b , c , sep = ':::' , end = '\t\t\t')     # 25:::10.8:::Hyd
print(a , b , c)                                    # 25 <space> 10.8 <space> Hyd


# Find outputs  (Home  work)
print('Hyd')                # Hyd <next line>
print()                     # <next line>
print('Sec')                # Sec <next line>
print()                     # <next line>
print('Cyb')                # Cyb <next line>
print()                     # <next line>


# Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s)                # [10,20,30,40] <space> (10,20,30,40) <space> {10,40,20,30} 


#  Find  outputs (Home  work)
a = 25
b = '%f'  %a                # converts object 'a' to string float due to '%f'
print(b)                    # 25.000000
print(type(b))              # <class 'str'>
x = 10.8
y = '%d'  %x                # converts object 'x' to string int due to '%d'
print(y)                    # 10
print(type(y))              # <class 'str'>
m = [10 , 20 , 15 , 18]
n = '%s'  %m                # converts list to string list due to '%s'
print(n)                    # [10,20,15,18]
print(type(n))              # <class 'str'>


# Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f'  %a)          # <3 spaces> 10.93
print('%9.1f'  %a)          # <5 spaces> 10.9
print('%10.3f'  %a)         # <4 spaces> 10.927
print('%.2f'  %a)           # 10.93
print('%.6f'  %a)           # 10.927400
print('%f'  %a)             # 10.927400
print('%g'  %a)             # 10.9274



# Find  outputs (Home  work)
a = 'Hyd'
print('%7s'  %a)                # <4 spaces> Hyd
print('%-7s'  %a)               # Hyd <4 spaces>
print('%2s'  %a)                # Hyd and ignores smaller width 2
print('%s'  %a)                 # Hyd
print('%s' , a)                 # %s <space> Hyd
#print('%s'  a)                 # error due to comma between s and a (or) % is missing before object a
#print('%s' , %a)               # error due to comma
print(a)                        # Hyd



# Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40] 
print('%s'  %a)                 # converts [10,20,30,40] to "[10,20,30,40]"
print('%s' , a)                 # %s <space> [10,20,30,40]
#print('%s'  a)                 # error comma is missing
#print('%s' , %a)               # error due to comma
#print('%l'  %a)                # error %l format does not exist
print(a)                        # [10,20,30,40]



#Find outputs  (Home  work)
a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c))                   # 25 <4 spaces> 10.927400 <4 spaces> Hyd
print('%i    %g    %s'    %(a , b , c))                 # 25 <4 spaces> 10.9274 <4 spaces> Hyd
print('%s    %s    %s'  %(a , b , c))                   # 25 <4 spaces> 10.9274 <4 spaces> Hyd
print('%d    %g    %s'  , a , b , c)                    # %d %g %s <space> 25 <space> 10.9274 <space> Hyd
#print('%d    %g      %s'   a , b , c)                  # error comma is missing between the format and object
#print('%d    %g    %s'  ,  %(a , b , c))               # error due to comma
#print('%d    %g    %s'    %a%b%c)                      # error due to multiple %
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c)         # 25 <space> 10.927400 <space> Hyd



#  Find  outputs  (Home  work)
x = 25
y = F'{x}'                          # converts int object 'x' to string  '25'
print(y)                            # 25
print(type(y))                      # <class 'str'>
x = 10.8
y = F'{x}'                          # converts float object 'x' to string '10.8
print(y)                            # 10.8
print(type(y))                      # <class 'str'>
x = [10,20,30,40]
y = F'{x}'                          # converts list to string list '[10,20,30,40]'
print(y)                            # [10,20,30,40]
print(type(y))                      # <class 'str'




#Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}')                           # 25 <tab> 10.8 <tab> Hyd
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}')             # a=25 <tab> b=10.8 <tab> c=Hyd
print(F'{a=}  \t   {b=}   \t  {c=}')                        # a=25 <tab> b=10.8 <tab> c=Hyd
print(F'{a:}  \t   {b:}   \t  {c:}')                        # 25 <tab> 10.8 <tab> Hyd  ignores colons
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}')           # a={a} <tab> b={b} <tab> c={c}
print(F'a  =  a  \t  b  =  b  \t  c  =  c')                 # a=a <tab> b=b <tab> c=c
#print(F'{x =}  \t   {y =}   \t  {z =}')                    # no object in x , y , z




#  Find  outputs  (Home  work)
x = 25
print(F'{x}')                           #  25
print(F'{{x}}')                         #  {x}
print(F'{{{x}}}')                       #  {25}
print(F'{{{{x}}}}')                     # {{x}}
print(F'{{{{{x}}}}}')                   # {{25}}
print(F'{{{{{{x}}}}}}')                 # {{{x}}}
print(F'{{{{{{{x}}}}}}}')               # {{{25}}}
print(F'{{{{{{{{x}}}}}}}}')             # {{{{x}}}}




#F string assignment
x=25
print(F'{x}')                       # converts object 'x' to string '25
print(F'x')                         # braces are missing for object 'x'
print('{x}')                        # {x}
print('x')                          # x
print(x)                            # 25
print(F'x={x}')                     # x=25
print(F'{x=}')                      # x=25
print(F'x=')                        # x=
print(F'x:{x}')                     # x:25
print(F'{x:}')                      # 25 and ignores :



#R string 
a='Hyd is \n green \t city'
print(a)                            # Hyd is <next line> green <tab> city
b=R'Hyd is \n green \t city'
print(b)                            # Hyd is \n green \t city
c='Hyd is \\n green \\t city'
print(c)                            # Hyd is \n green \t city