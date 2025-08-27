


'''
Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  single  if  with  3  conditions  and  else
'''


try:
    l=int(input('enter year'))
    if l%4==0 and l%100!=0 or l%400==0:
        print("Leap Year")
    else:
        print("Not a Leap Year")
except:
    print("enter integer only")


# In[7]:


'''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions
'''

try:
    a=int(input("enter 1st no"))
    b=int(input("enter 1st no"))
    c=int(input("enter 1st no"))
    if a>b and a>c:
        print(a)
    elif b>c:
        print(b)
    else:
        pritn(c)
except:
    print("enter integer values only")


# In[17]:


'''
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8
'''

try:
    a=int(input('Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius : '))
    if a==1:
        temp=float(input("Enter  celsius  temperature :  "))
        print(1.8* temp +32)
    elif a==2:
        temp=float(input("Enter  fahrenheit  temperature : "))
        print((temp-32)/1.8)
    else:
        print("Invalid input")
except:
    print("enter float or int value only")

# Find  outputs  (Home  work)
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye')
#output
Bye# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _:           # _ should be last case
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye')# Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	case  _:     # _ should be last case
		print('Hello')
	case  _:     # _ should be last case and only one _ should be use in one program
		print('Bye')
print('End')#  Find  outputs  (Home  work)
m = 1
match  m:
	case  1:
		print('Hyd')
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye')

#output
Hyd
Bye# Find  outputs  (Home  work)
ch = 'B'
match  ch:
	case   'A':
		print('Apple')
	case  'B':
		print('Book')
	case  'C':
		print('Cafe')
	case  _:
		print('None of  the  above')
print('Bye')


#output
Book
Bye'''
1) What  are  the  outputs  if  input  is  -6 ? --->     #Hyd <nextline>Sec <nextline>Cyd<nextline>Bye
2) What  are  the  outputs  if  input  is  15  ?  --->   #One <nextline>Two<nextline>Three<nextline>Bye
3) What  are  the  outputs  if  input  is  10.8  ?  ---> #India<nextline>China<nextline>Usa<nextline>Bye
4) What  are  the  outputs  if  input  is  0  ?  --->    #Hyd <nextline>Sec <nextline>Cyd<nextline>Bye
5) What  are  the  outputs  if  input  is  -10  ?  ---> #One <nextline>Two<nextline>Three<nextline>Bye
6) What  are  the  outputs  if  input  is  7  ?  --->#Hyd <nextline>Sec <nextline>Cyd<nextline>Bye
'''
x = eval(input('Enter any  number :  '))
match  x:
	case  7 |  -6  |  0:
		print('Hyd')
		print('Sec')
		print('Cyb')
	case  -10 | 15:
		print('One')
		print('Two')
		print('Three')
	case  _:
		print('India')
		print('China')
		print('Usa')
# End  of  match
print('Bye')'''
1) What  is  the  output  when  input  is  (-10 , -20) ?  --->  Quadrant
2) What  is  the  output  when  input  is  (10 , 0) ?  --->  x - axis
3) What  is  the  output  when  input  is  (0 , -20) ?  --->y - axis
4) What  is  the  output  when  input  is  (0 , 0) ?  --->Origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  --->Not  a  point
6) What  is  the  output  when  input  is  [10 , 20]  ?  --->Quadrant
7) What  is  the  output  when  input  is  [0 , -25]  ?  --->y - axis
8) What  is  the  output  when  input  is  ()  ?  --->Not  a  point
9) What  is  the  output  when  input  is  {10 , 20} ?  --->Not  a  point
10) What  is  the  output  when  input  is  (25,) ?  --->Not  a  point
11) What  is  the  output  when  input  is  {10 : 20} ?  --->Error
'''
tpl = eval(input('Enter  any  point  in  the  form  of  (x , y) :  '))
match  tpl:
	case  (0 , 0):
		print('Origin')
	case   (0 , y):
		print('y - axis')
	case   (x , 0):
		print('x - axis')
	case   (x , y):
		print('Quadrant')
	case  _:
		print('Not  a  point')
# In[4]:


'''
Write  a  program  to  add  two  lists  and  store  results  in  3rd  list

1st  list  --->  [10 , 20 , 15 , 18]

2nd  list  --->  [30 , 40 , 35 , 12 , 100 , 200 , 300]

3rd  list ?  ---> [10 + 30 , 20 + 40 , 15 + 35 , 18 + 12]  =  [40 , 60 , 50 , 30]

Hint:  Use  append()  method
'''
a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []
for i in range(min(len(a),len(b))):
    c.append(a[i]+b[i])
print(c)
for i in a:
    for j in b:
        c.append(i+j)


# In[9]:


#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
#How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
for i in range(2,4):
    print(a[i])
#How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice
for i in a[2:4]:
    print(i)

#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a)      #[11, 21, 16, 19]
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :',b)          #[10, 20, 15, 18]
# In[ ]:



