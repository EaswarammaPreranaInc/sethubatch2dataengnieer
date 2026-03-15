
# Find  output (Home  work)

def   f1(a = []):
        pass
print(f1 . __defaults__) # Output: ([],)



# Find  outputs (Home  work)

def   f1(x , a = []):
	a . append(x)
	print('List :  ' ,  a)
#end  of  the  function
print('_defaults_  :  ' , f1.__defaults__) # Output: _defaults_  :   ([],)
f1(3) # Output: List :   [3]
print('_defaults_  :  ' , f1.__defaults__) # Output: _defaults_  :   ([3],)
f1(4 , [1 , 2 , 3]) # Output: List :   [1, 2, 3, 4]
print('_defaults_  :  ' , f1.__defaults__) # Output: _defaults_  :   ([3],)
f1(9) # Output: List :   [3, 9]
print('_defaults_  :  ' , f1.__defaults__) # Output: _defaults_  :   ([3, 9],)
f1(40 , [10 , 20 , 30]) # Output: List :   [10, 20, 30, 40]
print('_defaults_  :  ' , f1.__defaults__) # Output: _defaults_  :   ([3, 9],)
f1(5) # Output: [3, 9, 5]
print('_defaults_  :  ' , f1.__defaults__) # Output: _defaults_  :    ([3, 9, 5],)
f1([6 , 7 , 8]) # Output: List :   [3, 9, 5, [6, 7, 8]]
print('_defaults_  :  ' , f1.__defaults__) # Output: _defaults_  :   ([3, 9, 5, [6, 7, 8]],)



#  Find  outputs (Home  work)

def   f1(x , a = []):
        if  a  ==  []:
                a = []
        a . append(x)
        print(a)
#end  of  the  function
print('_defaults_  :  ' , f1.__defaults__) # Output: _defaults_  :   ([],)
f1(3) # Output: [3]
print('_defaults_  :  ' , f1.__defaults__) # Output: _defaults_  :   ([],)
f1(4 , [1 , 2 , 3]) # Output: [1, 2, 3, 4]
print('_defaults_  :  ' , f1.__defaults__) # Output: _defaults_  :   ([],)
f1(4) # Output: [4]
print('_defaults_  :  ' , f1.__defaults__) # Output: _defaults_  :   ([],)
f1(40 , [10 , 20 , 30]) # Output: [10, 20, 30, 40]
print('_defaults_  :  ' , f1.__defaults__) # Output: _defaults_  :   ([],)
f1(5) # Output: [5]
print('_defaults_  :  ' , f1.__defaults__) # Output: _defaults_  :   ([],)
f1([6 , 7 , 8]) # Output: [[6, 7, 8]]
print('_defaults_  :  ' , f1.__defaults__) # Output: _defaults_  :   ([],)



# Find  outputs(Home  work)

def     f1(x , a = []):
	for  i  in  range(x):
		a . append(i * i)
	return  a
# End  of  the  function
print('_defaults  :  ' , f1.__defaults__) # Output: _defaults  :   ([],)
print(f1(3)) # Output: [0, 1, 4]
print('_defaults  :  ' , f1.__defaults__) # Output: _defaults  :   ([0, 1, 4],)
print(f1(4 , [10 , 20 , 15 , 18])) # Output: [10, 20, 15, 18, 0, 1, 4, 9]
print('_defaults  :  ' , f1.__defaults__) # Output: _defaults  :   ([0, 1, 4],)
print(f1(5)) # Output: [0, 1, 4, 0, 1, 4, 9, 16]
print('_defaults  :  ' , f1.__defaults__) # Output: _defaults  :   ([0, 1, 4, 0, 1, 4, 9, 16],)
print(f1(a = [100 , 200 , 300],   x = 6 )) # Output: [100, 200, 300, 0, 1, 4, 9, 16, 25]
print('_defaults  :  ' , f1.__defaults__) # Output: _defaults  :   ([0, 1, 4, 0, 1, 4, 9, 16],)
print(f1(6)) # Output: [0, 1, 4, 0, 1, 4, 9, 16, 0, 1, 4, 9, 16, 25]
print('_defaults  :  ' , f1.__defaults__) # Output: _defaults  :   ([0, 1, 4, 0, 1, 4, 9, 16, 0, 1, 4, 9, 16, 25],)



# Find  output (Home  work)

def     f1(x , a = []):
        if   a == []:
                a = []
        for  i   in   range(x):
                a . append(i * i)
        return  a
# End  of  the  function
print(f1(3)) # Output: [0, 1, 4]
print(f1(4 , [10 , 20 , 15 , 18])) # Output: [10, 20, 15, 18, 0, 1, 4, 9]
print(f1(5)) # Output: [0, 1, 4, 9, 16]
print(f1(a = [100 , 200 , 300],   x = 6 )) # Output: [100, 200, 300, 0, 1, 4, 9, 16, 25]
print(f1(6)) # Output: [0, 1, 4, 9, 16, 25]



# Find  outputs

def   f1(a = 'Hyd' , b = []):
	a += "Sec"
	b += [1 , 2 , 3]
	print('a :  ' , a)
	print('b :  ' , b)
# End of the function
print('Default Values  :  ' , f1 . __defaults__) # Output: Default Values  :   ('Hyd', [])
f1() 
'''
# Output: 
a :   HydSec
b :   [1, 2, 3]
'''
print('Default Values  :  ' , f1 . __defaults__) # Output: Default Values  :   ('Hyd', [1, 2, 3])
f1() 
'''
# Output: 
a :   HydSec
b :   [1, 2, 3, 1, 2, 3]
'''
print('Default Values  :  ' , f1 . __defaults__) # Output: Default Values  :   ('Hyd', [1, 2, 3, 1, 2, 3])
f1() 
'''
# Output: 
a :   HydSec
b :   [1, 2, 3, 1, 2, 3, 1, 2, 3]
'''