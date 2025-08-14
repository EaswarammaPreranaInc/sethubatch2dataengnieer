# eval()  function  demo  program
print(eval('25'))                #25   int object
print(eval('10.8'))              #10.8   float object
print(eval('False'))             #False    bool object
print(eval('3+4j'))              #3+4j     complex object
print(eval('Hyd'))               #Returns error as this statement is invalid(it must be eval(' 'Hyd' ')
print(eval("    'Hyd'   "))     #Hyd      String object
print(eval('3 + 4 * 5'))               #23    int object
print(eval('[10 , 20 , 15 , 18]'))              #[10, 20, 15, 18]      list object
print(eval('{10,20,15,18,20,12,18}'))        #{10, 20, 15, 18, 20, 12, 18}      set object
print(eval('(10 , 20 , 30)'))                 #(10, 20, 30)    tuple object
print(eval("{10 : 'Hyd' , 10 : 'Sec'}"))         #{10 : 'Sec'}       dict object
print(eval(4 + 5))                  #Returns error as 4+5 must be enclosed in ' '





#  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   "))               #hyd   sting object
hyd = 'Sec'
print(eval('hyd'))                          #Sec   string object
sec = '25'
print(eval('sec'))                           #25    string object
print(eval(sec))                        #25     int object
cyb = 10.8
print(eval('cyb'))                        #10.8    float object
print(eval(cyb))                        #returns error as it becomes eval(10.8) but it must be eval('10.8')







#  Tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")'))          #it is interpreted as print(eval('None')) therefore we get None as output which is a Nonetype object. The ouptput will be as follows
Hyd
None 






#  Find  outputs  (Home  work)
print(bool('False'))                         #True     bool object
print(eval('False'))                          #False     bool object
print(bool(''))                                  #False    bool object
print(eval('  ""  '))                             #""        string object
print(eval(''))                                    #Returns error as nothing is passed
print(eval('  " "   '))                            #" "       string object
print(eval(' '))                              #Returns error as noting is passed to evaluate.(space can't be evaluated)







# What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  '))                 #this can take any input and typecasts it to appropriate type
print(type(x))                                       #returns the type of x
print(x)                                                 #prints x








# What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ')
print(len(a))
print(a)
b = eval(input('Enter   any  string  : '))
print(len(b))
print(b)                              #first method is better approach for reading string input because eval eill throw error if the input string is not enclosed in quotes







# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')   #   25 , 10.8 , Hyd
print(a , b , c , sep = '\t')               #25        10.8          Hyd
print(a , b , c , sep = '---')             #25---10.8---Hyd
print(a , b , c , sep = '\n')              #25
                                                       10.8     
                                                        Hyd
print(a , b , c)                               #25 10.8 Hyd
print(a , b , c , separator = ':')      #returns error as the keyword is sep not seperator







# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---')                   #25 10.8 'Hyd'---
print(a , b , c , sep = ',,,')                      #25,,,10.8,,,'Hyd'
print(a , b , c , sep = ':::' , end = '\t\t\t')        #25:::10.8:::'Hyd'<3tab spaces>
print(a , b , c)                               #25 10.8 'Hyd'









# Find outputs  (Home  work)
print('Hyd')             #Hyd
print()                     #prints nothing
print('Sec')             #Sec
print()                     #prints nothing
print('Cyb')             #Cyb








# Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s)                 #[10 , 20 , 30 , 40] (10 , 20 , 30 , 40) {10 , 20 , 30 , 40}









#  Find  outputs (Home  work)
a = 25
b = '%f'  %a
print(b)              #25.000000
print(type(b))      #<class 'str'>
x = 10.8
y = '%d'  %x
print(y)                #10
print(type(y))          #<class 'str'>
m = [10 , 20 , 15 , 18]
n = '%s'  %m
print(n)                #[10, 20, 15, 18]
print(type(n))          #<class 'str'>








# Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f'  %a)  #  <3  spaces>10.93
print('%9.1f'  %a)       #<5 spaces>10.9
print('%10.3f'  %a)          #<4 spaces>10.927
print('%.2f'  %a)                #10.93
print('%.6f'  %a)              #10.927400
print('%f'  %a)                 #10.927400









# Find  outputs (Home  work)
a = 'Hyd'
print('%7s'  %a)   #  <4  spaces>Hyd
print('%-7s'  %a)  #  Hyd<4   spaces>
print('%2s'  %a)   #  Hyd  and  ignores  smaller width
print('%s'  %a)          #Hyd
print('%s' , a)          #%s Hyd
print('%s'  a)      #Syntax error
print('%s' , %a)    #Syntax error
print(a)             #Hyd









# Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40]
print('%s'  %a)          #[10, 20, 30, 40]
print('%s' , a)          #%s [10, 20, 30, 40]
print('%s'  a)     #Syntax error
print('%s' , %a)      #syntax error
print('%l'  %a)       #returns error as 5l is not defined
print(a)          #[10, 20, 30, 40]







#Find outputs  (Home  work)a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c))        #25    10.927400    Hyd
print('%i    %g    %s'    %(a , b , c))      #25    10.9274    Hyd
print('%s    %s    %s'  %(a , b , c))        #25    10.9274    Hyd
print('%d    %g    %s'  , a , b , c)   #%d    %g    %s 25 10.9274 Hyd
print('%d    %g      %s'   a , b , c)       #Syntax error
print('%d    %g    %s'  ,  %(a , b , c))       #Syntax error
print('%d    %g    %s'    %a%b%c)       #Syntax error
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c)    #25 10.927400 Hyd