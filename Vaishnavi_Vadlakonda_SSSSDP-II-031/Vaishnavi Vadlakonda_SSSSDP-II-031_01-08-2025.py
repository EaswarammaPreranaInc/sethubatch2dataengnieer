# Find  output (Home  work)
def   f1(a = []): 
        pass
print(f1 . __defaults__) # prints ([],)
      





 


# Find  outputs (Home  work)
def   f1(x , a = []):
	a . append(x)
	print('List :  ' ,  a)
#end  of  the  function
print('_defaults_  :  ' , f1.__defaults__) # prints _defaults_ : ([],)
f1(3) # appends 3 to default list and prints List : [3]
print('_defaults_  :  ' , f1.__defaults__) # prints _defaults_ ([3],)
f1(4 , [1 , 2 , 3]) # appends 4 to actual list [1, 2, 3] i.e.,List : [1, 2, 3, 4]
print('_defaults_  :  ' , f1.__defaults__) # prints _defaults_ : ([3],)
f1(9) # appends 9 to default list i.e., List : [3,9]
print('_defaults_  :  ' , f1.__defaults__) # prints _defaults_ : ([3, 9],)
f1(40 , [10 , 20 , 30]) # appends 40 to actual list [10, 20, 30] i.e.,List : [10, 20, 30, 40]
print('_defaults_  :  ' , f1.__defaults__) # prints _defaults_ : ([3, 9],)
f1(5) # appends 5 to default list i.e., List : [3,9,5]
print('_defaults_  :  ' , f1.__defaults__) # prints _defaults_ : ([3, 9, 5],)
f1([6 , 7 , 8]) # appends [6, 7, 8] to default list i.e., List : [3, 9, 5, [6, 7, 8]]
print('_defaults_  :  ' , f1.__defaults__) # prints _defsults_ : ([3,4,5,[6, 7, 8]],)









#  Find  outputs (Home  work)
def   f1(x , a = []):
        if  a  ==  []:
            a = []
        a . append(x)
        print(a)
#end  of  the  function
print('_defaults_  :  ' , f1.__defaults__) # prints _defaults_ : ([],)
f1(3) # appends 3 to local list 'a' and prints List : [3]
print('_defaults_  :  ' , f1.__defaults__) # prints _defaults_ : ([],)
f1(4 , [1 , 2 , 3]) # appends 4 to actual list and prints List : [1, 2, 3, 4]
print('_defaults_  :  ' , f1.__defaults__) # prints _defaults_ : ([],)
f1(4) # appends 4 to local list 'a' and prints List : [4]
print('_defaults_  :  ' , f1.__defaults__) # prints _defaults_ : ([],)
f1(40 , [10 , 20 , 30]) # appends 40 to actual list and prints List : [10, 20, 30, 40]
print('_defaults_  :  ' , f1.__defaults__) # prints _defaults_ : ([],)
f1(5) # appends 5 to local list 'a' and prints List : [5]
print('_defaults_  :  ' , f1.__defaults__) # prints _defaults_ : ([],)
f1([6 , 7 , 8]) # appends [6, 7, 8] to local list and prints List : [[6, 7, 8]]
print('_defaults_  :  ' , f1.__defaults__) # prints _defaults_ : ([],)









# Find  outputs(Home  work)
def f1(x , a = []):
	for  i  in  range(x):
		a . append(i * i)
	return  a
# End  of  the  function
print('_defaults  :  ' , f1.__defaults__) # prints _defaults_ : ([],)
print(f1(3)) # prints [0, 1, 4]
print('_defaults  :  ' , f1.__defaults__) # prints _defaults_ : ([0, 1, 4],)
print(f1(4 , [10 , 20 , 15 , 18])) # prints [10, 20, 15, 18, 0, 1, 4, 9]
print('_defaults  :  ' , f1.__defaults__) # prints _defaults : ([0, 1, 4],)
print(f1(5)) # [0, 1, 4, 0, 1, 4, 9, 16]
print('_defaults  :  ' , f1.__defaults__) # prints _defaults_ ([0, 1, 4, 0, 1, 4, 9, 16],)
print(f1(a = [100 , 200 , 300],   x = 6 )) # [100, 200, 300, 0, 1, 4, 9, 16, 25]
print('_defaults  :  ' , f1.__defaults__) # prints _defaults_ : ([0, 1, 4, 0, 1, 4, 9, 16],)
print(f1(6)) # [0, 1, 4, 0, 1, 4, 9, 16, 0, 1, 4, 9, 16, 25]
print('_defaults  :  ' , f1.__defaults__) # prints _defaults_ : ([0, 1, 4, 0, 1, 4, 9, 16, 0, 1, 4, 9, 16, 25],)









# Find  output (Home  work)
def     f1(x , a = []):
        if   a == []:
                a = []
        for  i   in   range(x):
                a . append(i * i)
        return  a
# End  of  the  function
print(f1(3)) # prints [0, 1, 4]
print(f1(4 , [10 , 20 , 15 , 18])) # prints [10, 20, 15, 18, 0, 1, 4, 9]
print(f1(5)) # prints [0, 1, 4, 9, 16]
print(f1(a = [100 , 200 , 300],   x = 6)) # prints [100, 200, 300, 0, 1, 4, 9, 16, 25]
print(f1(6)) # prints [0, 1, 4, 9, 16, 25]









# Find  outputs
def   f1(a = 'Hyd' , b = []):
	a += "Sec"
	b += [1 , 2 , 3]
	print('a :  ' , a)
	print('b :  ' , b)
# End of the function
print('Default Values  :  ' , f1.__defaults__) # prints Default Values : ('Hyd', [])
f1() # prints a : HydSec<nextline>b : [1, 2, 3]
print('Default Values  :  ' , f1.__defaults__) # prints Default Values : ('Hyd', [1, 2, 3])
f1() # prints a : HydSec<nextline>b : [1, 2, 3, 1, 2, 3]
print('Default Values  :  ' , f1.__defaults__) # prints Default Values : ('Hyd', [1, 2, 3, 1, 2, 3])
f1() # prints a : HydSec<nextline>b : [1, 2, 3, 1, 2, 3, 1, 2, 3]