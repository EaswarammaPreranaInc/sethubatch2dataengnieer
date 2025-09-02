
#HOME WORK 18/08/2025 

#  len()  function demo   program  (Home  work)
a = [ 25, 10.8, 'Hyd', True]
print(len(a)) # 4 
b = []
print(len(b)) # 0
c = [[10 , 20] , 30 , 40]
print(len(c)) # 3


'''
What  does  len(list)  do ?  --->  Returns  number  of  elements  in  the  list
'''
###########################################################

# sum()  function  demo  program  (Home  work)
a = [25 , 10.8 , True]
print(sum(a)) # 36.8
b= [3 + 4j , 5 + 6j]
print(sum(b)) # 8+10j
c = [25 , 10.8 , True , 3 + 4j , False]
print(sum(c)) # 39.8+4j
d = [10 , 20 , 15 , 18]
print(sum(d)) # 63
e = [25 , 10.8 , 'Hyd' , True]
print(sum(e)) # error because string cannot be added


'''
What  does  sum(list)  do ?  ---> Returns  sum  of  list  elements
'''
############################################################ ??????????????
#  Find  outputs
a = [[10 , 20 , 15 , 18]]
#print(sum(a)) # error
print(sum(a[0]) # How  to  determine  sum  of  inner  list  elements)
print(sum(x for x in a)) #How  to  determine  sum  of  inner  list  elements  in  another  way)

########################################################

# max()  and  min()  functions  demo  program  (Home  work)
a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a)) # 30
print(min(a)) # 5
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b)) # Vamsi
print(min(b)) # Amar
c = [25 , 10.8 ,  3 + 4j , True]
print(max(c)) # error BECAUSE WE HAVE COMPLEX NUMBER
d = [25 , '35']
print(max(d)) # error STR AND INT CAN'T BE ADDED 
print(max([])) # error BECAUSE MAX() ARGS IS EMPTY
print(min([])) # error BECAUSE MIN() ARGS IS EMPTY


'''
1) What  does  max(list)  do ?  --->  Returns  largest  element  of  the  list

2) What  does  min(list)  do ?  --->  Returns  smallest  element  of  the  list
'''

############################################################################
# list()  function  demo  program
a = (10 , 20 , 15, 18)
b = list(a) #CONVERTS TUPLE a TO lIST 
print(b) # [10,20,15,18]
print(type(b)) # <class 'list'>
print(a  is  b) # False 
print(a == b) # True

##############################################################################

#  Find  outputs (Home  work)
a = range(4 , 10 , 2)
b = list(a) # CONVERTS THE TUPLE TO LIST
print(b) # [4,6,8]
print(type(b)) # class list
a = list('Vamsi') # CONVERTS THE STR OF CHARACTERS IN LIST OF ELEMENTS I.E MEANS ['V' ,'a' ,'m' ,'s' ,'i']
print(a) # ['V' ,'a' ,'m' ,'s' ,'i']
a = list() # empty list
print(a) # Empty list not an error 
print(list(25)) # 25
print(list(10.8)) # TypeError int object not  iterable
print(list(True)) # TypeError bool object not  iterable
print(list(None)) # TypeError NoneType object not  iterable


'''
1) What  does  list(sequence)  do ?  --->  Converts  sequence  to  list  and  returns  list

2) What  does  list(no-args)  do ?  ---> Returns  an  empty  list

3) What  does  list(non-sequence)  do ?  --->  Throws  error 
'''

#######################################################################################

# Find  outputs (Home  work)
a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90))
print(list(a)) #converts the tuple a to list --  [(10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)]
b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)}
print(list(b)) # converts the tuple a to list --  [(10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)]
c = ([10 , 20] , (30 , 40) , {50 , 60})
print(list(c)) # [[10 , 20] , (30 , 40) , {50 , 60}]


# for printing the list of list we use and out we get [[10 , 20] , [30 , 40] , [50 , 60]]
# list_of_lists = [list(x) for x in a]
#print(list_of_lists)
########################################################################################

# sorted()  function   demo  program
a = [10 , 20 , 15 , 5 , 12]
b = sorted(a)   
print(b) # [5,10,12,15,20]
print(type(b)) # <class 'list'>
c = sorted(a , reverse = True)
print(c) # [20,15,12,10,5]
print(a) # [10 , 20 , 15 , 5 , 12]

#sorted() returns a new list that is sorted, leaving the original list unchanged.


'''
sorted()  function 
----------------------
1) What  does  sorted(list)  do  ?  ---> Returns  another  sorted  list

2) Is  argument  list  modified ?  --->  No  and  it  remains  unchanged

3) How  to  sort  list  in  descending  order ?  --->  sorted(list , reverse = True)

4) What  are  the  two  arguments  of  sorted()  function ?  --->  List  to  be  sorted
																												and
																					                  reverse = True  which  is  an  optional  argument
'''

##############################################################################################

# Find  outputs  (Home  work)
a = ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']
b = sorted(a)
print(b) # ['Amar' ,'Kiran' ,'Rajesh' ,'Rama' ,'Rama Rao' ,'Sita' ,'Vamsi']
c = sorted(a , reverse = True)
print(c) # ['Vamsi' , 'Sita' ,'Rama Rao', 'Rama' ,'Rajesh' , 'Kiran' , 'Amar']
print(a) # ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']

##########################################################################################

# all()  function demo  program  (Home  work)
a = [12 > 10 , 5 < 20 , 30 == 30]
print(all(a)) # True
b = [9 >= 6 , 12 <= 9 , 6 == 6]
print(all(b)) #False
c = [25 , 10.8 , '' , True , 3+4j , 'Hyd']
print(all(c)) #  false because '' is empty element 
d = [10 , 0 , 20]
print(all(d)) # false because 0 is false 
e = []
print(all(e)) # True it is an empty list


'''
all()  function
-----------------
1) What  does  all(list)  do ?  --->  Returns  True  when  every  element of  the  list  is  True  and  False  otherwise

2) When  does  it  return  False ?  --->  When  at  least  one  element  of  the  list  is  False

3) if  cond1  and  cond2  and  cond3  and  cond4:
    How  to  reduce  the  four  conditions  to  a  single  condition ?  --->  if  all([cond1 , cond2 , cond3 , cond4]):
'''
#################################################################################################

# any()  function demo program  (Home  work)
a  = [12 > 18 , 5 < 20 , 35 == 30]
print(any(a)) # True
b = [12 > 18 , 25 < 20 , 35 == 30]
print(any(b)) # False
c = [0 , 0.0 , '' , 25 , 0 + 0j , False]
print(any(c)) # True
d = [0 , 0.0 , '' , 0 + 0j , False]
print(any(d)) # True
e = []
print(any(e)) # False


'''
any()   function
-------------------
1) What  does  any(list)  do ?  ---> Returns  True  when  at  least  one  element  of  the  list  is  True  and  False  otherwise

2) When  does  it  return  False ?  ---> When  every  element  of  the  list  is  false

3) if  cond1  or  cond2  or  cond3  or  cond4:
     How  to  reduce  the  four  conditions  to  a  single  condition ?  ---> if  any([cond1 , cond2 , cond3 , cond4]):

4) all()  and  any()  functions  are  used  as  an  alternative  when  there  are  too  many  conditions  in  if  and  while
'''
####################################################################################################

# del  operator  demo  program (Home  work)
a = [10 , 20 , 15 , 18]
print(a) # [10 , 20 , 15 , 18]
del    a[2]
print(a) # [10 , 20 , 18]
del  a[3] # error out of range because we have only 
del  a 
print(a) # NameError nothing is assigned to a or a is not defined 

####################################################################################################

#  append()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18]
print(list) # [10 , 20 , 15 , 18]
list . append(19)
print(list) [10 , 20 , 15 , 18,19]

##################################################################################################
#  Find  outputs (Home  work)
list = []
print(list) # []
list . append(25)  # [25]
list . append(10.8) # [25 , 10.8]
list . append('Hyd') # [25 , 10.8 ,Hyd]
list . append(True) # [25 , 10.8 ,Hyd ,True]
print(list) #  [25 , 10.8 ,Hyd ,True]

###################################################################
# Find  outputs  (Home  work)
list = []
for  x  in   range(0 , 50 , 10):
	list . append(x)
print(list) # [0,10,20,30,40]

#################################################################

#  Find  outputs  (Home  work)
a = [10 , 20 , 30]
a . append('Hyd')
print(a) # [10 , 20 , 30 ,'Hyd']
print(len(a)) # 4
print(How  to  print  4th  element  of  list  'a') # print(a(3))
print(How  to  print  'H') # print(a[3][1])
print(How  to  print  'y') # print(a[3][2])
print(How  to  print  'd') # print(a[3][3])

############################################################

# remove()  method  demo  program  (Home  work)
try:
	list = [10 , 20 , 15 , 18 , 15 , 12 , 15 , 19]
	list . remove(15) # [10 , 20 , 18 , 15 , 12 , 15 , 19]
	print(list) # [10 , 20 , 18 , 15 , 12 , 15 , 19]
	list . remove(25) # ValueError 25 IS NOT IN LIST 
except:
	print('25  is   not  in  the  list') # EXECUTES THESE LINE



'''
remove()   method
---------------------
1) What  does  remove(x)  do ?  --->  Removes   first  occurance  of  'x'  from  the  list

2) What  does  remove()  method  do  if  'x'  is  not   in  the  list ?  --->  Throws  ValueError

3) How  to  remove  all  ocurances  of  'x'  from  the  list ?  --->   Call  remove()  method  in  a  loop
'''
########################################################################




