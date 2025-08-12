a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a) #prints the list object as it is like [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(*a) # unpacks the list and printas it with default seperator space 25 10.8 'Hyd' True 3 + 4j None 'Hyd' 25
print(type(a)) # prints the type of object a i.e class 'list'
print(id(a)) # prints the address of the object a
print(len(a)) # counts the elements in a and prints the length
a[2] = 'Sec'  # replaces the 2nd index element 'hyd' with 'sec'
print(a) # prints a [25 , 10.8 , 'Sec' , True , 3 + 4j , None , 'Hyd' , 25]
print(a[2:5]) #slices the list and ceates new list object from 2 to 4 index ['Sec', True, (3+4j)]

a = [ ] #assigning empty list to a
print(a) # prints an empty list 
a . append(25) # inserts 25 at end 
a . append(10.8) # inserts 10.8 at the end
a . append('Hyd') # inserts 'Hyd' at end
a . append(True) #inserts True at the end
print(a) #prints a with all added objects i.e [25, 10.8, 'Hyd', True]
a . remove('Hyd') # removes the 'Hyd'
print(a) # [25, 10.8, True]
a . remove('25') #error because we dont have '25' in the list but we have 25 int
print(a) # as we didnt remove any element list remains same  [25, 10.8, True]

a = [25 , 10.8 , 'Hyd'] # assigns list to a
print(a) #prints the list object [25, 10.8, 'Hyd']
print(id(a)) #prints the address of a
print(a * 3) # repeats the list 3 times and stores inn a single list and print them
print(a * 2) # repeats the list 2 times and stores in a single list and print them
print(a * 1)# repeats the list 1 times and stores in a single list and print them
print(a * 0) # repeats the list 0 times and stores in a single list and print them
print(a * -1) # empty string if we give negative number for repetition
print(a * 4.0) # error beacuse we cant repeat the list with float number
a = a * 3 # repeats the list 3 times and stores inn a single list and stores again it in a
print(a)  #prints the list object [25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(id(a)) #prints the address of a
a = [25]  # assigns list to a
print(a*a) # error because we shouls use * operator with int object only for repition

a = list('Hyd')  # converts the string 'Hyd' into a list of its characters
print(a) # prints characters as list ['h','y','d']
print(type(a)) #prints the type of object a i.e class list
print(len(a)) # counts the chars of the liste i.e 3
b = (10 , 20 , 15 , 18) #assigns the tuple to b
print(list(b)) # converts the tuple b to list and prints it [10, 20, 15, 18]
print(list(range(5))) # converts the range object which has elements from 0 to 4 to list
print(list(25)) # error  because argument  should  be  sequence  only but int is non sequence

a = [ ] # assigning empty list to a
print(type(a)) # prints the type of the a i.e class list
print(a) # prints the list a which is empty list
print(len(a)) # returns 0 because the list is empty
b = list() # assigns the list to b
print(b) # Returns  an  empty  list because there are no args given to the list
print(len(b)) # 0 beacuse empty list

#        0      1   2         3         4   5       6         7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8     -7       -6        -5         -4      -3       -2        -1
print(list[2 : 7]) # prints the elements of list from index 2 to 6 in step of 1 [(3+4j), 'Hyd', True, None, 10.8]
print(list[ : : ])# as there is no begin end and step it takes default values i.e 0 to length-1 in steps of 1 i.e whole list
print(list[:]) #  list[0 :  8 :  1]  --->  List  from  indexes  0  to  7  in  steps  of  1  i.e.  [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1]) # we dont have start and end but we have negative step so we take begin as -1 and end as -9 so we get list in reverse order
print(list[ : : 2]) # as there is no begin end it takes default values i.e 0 to length-1 in steps of 2 [25, (3+4j), True, 10.8]
print(list[1 : : 2]) # as the begin is 1 and there is no end it takes default value length-1 in steps of 2 i.e [10.8, 'Hyd', None, 'Hyd']
print(list[ : : -2]) #  list[-1 :  -9 : -2]  --->  List  from  indexes   -1  to  -8  in  steps  of   -2   i.e.  ['Hyd' , None , 'Hyd' , 10.8]
print(list[-2 : : -2]) # start is -2 we dont have end but we have negative step so we take end as -9 in step of -2 [10.8, True, (3+4j), 25]
print(list[1 : 4]) # prints 1 to 3 in steps of 1(default step) i.e [10.8, (3+4j), 'Hyd']
print(list[-4 : -1]) # prints from -4 to -2 in step of 1(default) i.e [True, None, 10.8]
print(list[3 : -3]) #prints from 3 to -4(4 index) in step of 1 ['Hyd', True]
print(list[2 : -5]) # prints from 2 to -6(3 )i.e [(3+4j)]
print(list[-1:-5]) # prints from -1 to -6 in step of 1 but we get empty string because if we go on with step 1 to-1 we get 0,1,2.. but not -6

#        0       1      2          3         4        5         6        7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5] # assigns the values of the list from index 3 to 4 to x,y
print('x : ' , x) # prints x i.e in 3rd index i.e Hyd
print('y : ' , y) # prints y i.e in 4th index i.e True
for  x  in  list[2:7]:
	print(x) # prints from index 2 to 6 line by line
	
#     0     1     2    3     4
a = [10 , 20 , 30 , 40 , 50]# assigns the list to a
print(a , id(a)) # prints the list itdels and its id
a[1 : 4] = [60 , 70] # removes the elements from 1 to 3 and add the elements  60,70
print(a , id(a)) #[10, 60, 70, 50]
a[2: 4] = [100 , 200 ,  300] #  removes the elements from 2 to 3 and add the elements 100, 200, 300
print(a , id(a)) # prints the a [10, 60, 100, 200, 300] and its id

a =  [25]  # error  because argument  should  be  sequence  only but int is non sequence
print(a[1]) # error because we dont have any element at 1 and list a is not created
print(a[1:]) # we will get empty list not error

a = (25) # it becomes int because after a single element in tuple we should keep ','
b = 25, # assigns tuple to b because we have ',' after 25
c = 25 # c becomes int because after a single element in tuple we should keep ','
d = (25,) # assigns tuple to d because we have ',' after 25
print(type(a)) # class 'int'
print(type(b)) # class 'tuple'
print(type(c)) # class 'int'
print(type(d)) # class 'tuple'
print(a * 4) # we get as a is int 25 so * acts as multiplicator
print(b * 4) # tuple b is repeated 4 times and stored in same tuple
print(c *4)  # we get as a is int 25 so * acts as multiplicator
print(d*4) # tuple d is repeated 4 times and stored in same tuple

a = tuple('Hyd') # converts the string 'Hyd' into a tuple of its characters
print(a) # prints characters as tuple ['h','y','d']
print(type(a)) # prints the class of a i.e class tuple
print(len(a)) # counts the chars of the tuple i.e 3
b = [10 , 20 , 15 , 18] #assigns the list to b
print(tuple(b)) # converts the sequence type list to tuple
print(tuple(range(5))) # converts the range object which has elements from 0 to 4 to tuple
print(tuple(25)) # error  because argument  should  be  sequence  only but int is non sequence

a = () # assigns the empty tuple to a 
print(type(a)) # class tuple because we have given '()'
print(a) # empty tuplebecause there are no values inside tuple
print(len(a)) # 0 because we have empty tuple
b = tuple() # assigns tuple to b
print(b) # Returns  an  empty  tuple because there are no args given to the tuple
print(len(b)) # 0 because we have empty tuple

a = (10 , 20 , 30) # assigns the tuple to a
print(a) # prints the tuple a
print(id(a)) # prints the id of tuple a
a = a * 2 # repeate the tuple a 2 times and stores agaian into a 
print(a) # prints the tuple after repeating 2 times
print(id(a))  # prints the id of tuple a

a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'} #assigns set to a
print(a) # prints the set a if there are any duplicates they are removed and then printed
print(type(a)) # type of a is class set
print(len(a)) # counts the elements of a after remving duplicates i.e
print(a[2]) # error because set is unordered and doesnt have indexing so we cant access
print(a[1 : 4]) # error becaues set is unordered and not indexed
a[2] = 'Sec' # we cant assign values to set because set is unordered and partially muatble only
print(a *2) # repetition is not possible in set because set doesnt allow duplicates
print(a*a) # error because we shouls use * operator with int object only for repition

a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0} # assigns set to a
print(a) # prints the set with removing duplicates here true ,1,1.0 are same so any 1 will remain in same way false,0.0,0 are same
print(len(a)) # counts the elements i.e 4 {1,'hyd',false,''}
print(type(a)) # prints tpe of a i.e class set

a = set('Rama rAo') # converts the string 'Rama rAo' into a set of its characters
print(a) # prints characters as set i.e {'r', 'm', 'a', 'R', 'A', ' ', 'o'}
print(len(a)) # prints the elements in set a i.e 7
print(set([10 , 20 , 15 , 20])) # prints the set after removing duplicates i.e 20
print(set((25 , 10.8 , 'Hyd' , 10.8)))  # prints the set after removing duplicates i.e 10.8
print(set(range(10 , 20 , 3))) # initally rnage from 10 to 19 in step of 3 i.e 10,13,16,19 is converted to set
print(set(25)) #error because  argument  should  be  sequence  only 25 is int non sequence
print(set([25 , 10.8 , [] , 'Hyd'])) # error because set should have only immutable elements as arguments but lists are there which is mutable

a =   [ ]  #assigns empty list to a
b =   ( ) #assigns empty tuple to b
c =   {} #assigns empty dict to c
d =   set() #assigns empty set to c
print(type(a)) #<class 'list'>
print(type(b)) #<class 'tuple'>
print(type(c)) #<class 'dict'>
print(type(d)) #<class 'set'>
print(a) # empty list
print(b) # empty tuple
print(c) # empty dict
print(d) # empty set object i.e set()

a = set()  # creates empty set a
a . add(25) # inserts 25 to a
a . add(10.8) # inserts 10.8 to a
a . add('Hyd') # inserts 'Hyd' to a
a . add(True) # inserts True to a
a . add(None) # inserts None to a
a . add('Hyd') # inserts 'Hyd' to a
a . add(1) # inserts 1 to a
print(a) # prints a after removing duplicates i.e true and 1 are same 'Hyd' is repeated twice
print(len(a)) # counts the elemnts after removing duplicates
a . remove(25) # removing 25
print(a) # prints the set after removing 25
a . append(100) # error becuase append is not a method of set
a . add(set()) # error because nested set is not possible
a . add(()) # add empty tuple inside because tuple is immutable object
a . add([]) # eror because set cannot have mutable objects inside it
print(a) # prints a after adding empty tuple
a.add({}) # eror becuase dict is mutable

a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')  # print (a)
print(How  to  print  set) # print (a)
print('Iterate  thru  set  with  for  loop')
#How  to  iterate  thru  set with for loop
for i in a:
    print(i)