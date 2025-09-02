# Find  output (Home  work)
def   f1(a = []):
        pass
print(f1 . _defaults_) # ([],)
-----------------------------------------------
# Find  outputs (Home  work)
def   f1(x , a = []):
	a . append(x)
	print('List :  ' ,  a)
#end  of  the  function
print('_defaults_  :  ' , f1._defaults_) 

f1(3) # [3]
print('_defaults_  :  ' , f1._defaults_)  

f1(4 , [1 , 2 , 3]) # [1,2,3,4]
print('_defaults_  :  ' , f1._defaults_)  

f1(9) # [3,9]
print('_defaults_  :  ' , f1._defaults_)  

f1(40 , [10 , 20 , 30]) # [10,20,30,40]
print('_defaults_  :  ' , f1._defaults_)  

f1(5) #[3,9,5]
print('_defaults_  :  ' , f1._defaults_)  

f1([6 , 7 , 8]) # [3 , 9 , 5 [6 , 7 , 8]]
print('_defaults_  :  ' , f1._defaults_)  
--------------------------------------------------
#  Find  outputs (Home  work)
def   f1(x , a = []):
        if  a  ==  []:
                a = []
        a . append(x)
        print(a)
#end  of  the  function
print('_defaults_  :  ' , f1._defaults_) 
f1(3) # [3]
print('_defaults_  :  ' , f1._defaults_)  
f1(4 , [1 , 2 , 3]) # [1,2,3,4]
 print('_defaults_  :  ' , f1._defaults_)  
f1(4) # [4]
print('_defaults_  :  ' , f1._defaults_)  
f1(40 , [10 , 20 , 30]) # [10,20,30,40]
print('_defaults_  :  ' , f1._defaults_)  
f1(5) # [5]
print('_defaults_  :  ' , f1._defaults_) 
f1([6 , 7 , 8]) [[6,7,8]]
print('_defaults_  :  ' , f1._defaults_)  
---------------------------------------------------------
# Find  outputs(Home  work)
def     f1(x , a = []):
	for  i  in  range(x):
		a . append(i * i)
	return  a
# End  of  the  function
print('_defaults  :  ' , f1._defaults_) 
print(f1(3)) # [0, 1, 4]
print('_defaults  :  ' , f1._defaults_) 
print(f1(4 , [10 , 20 , 15 , 18])) #  [10, 20, 15, 18, 0, 1, 4, 9]
print('_defaults  :  ' , f1._defaults_)  
print(f1(5)) # [0, 1, 4, 0, 1, 4, 9, 16]
print('_defaults  :  ' , f1._defaults_)  
print(f1(a = [100 , 200 , 300],   x = 6 )) # [100, 200, 300, 0, 1, 4, 9, 16, 25]
print('_defaults  :  ' , f1._defaults_)  
print(f1(6)) # [0, 1, 4, 0, 1, 4, 9, 16, 0, 1, 4, 9, 16, 25]
print('_defaults  :  ' , f1._defaults_)  
-------------------------------------------------------------
# Find  output (Home  work)
def     f1(x , a = []):
        if   a == []:
                a = []
        for  i   in   range(x):
                a . append(i * i)
        return  a
# End  of  the  function
print(f1(3)) # [0, 1, 4]
print(f1(4 , [10 , 20 , 15 , 18])) # [10, 20, 15, 18, 0, 1, 4, 9]
print(f1(5)) #[0, 1, 4, 9, 16]
print(f1(a = [100 , 200 , 300],   x = 6 )) # [100, 200, 300, 0, 1, 4, 9, 16, 25]
print(f1(6)) # [0, 1, 4, 9, 16, 25]
--------------------------------------------------------
# Find  outputs
def   f1(a = 'Hyd' , b = []):
	a += "Sec"
	b += [1 , 2 , 3]
	print('a :  ' , a)
	print('b :  ' , b)
# End of the function
print('Default Values  :  ' , f1 . _defaults_)
f1()
print('Default Values  :  ' , f1 . _defaults_)
f1()
print('Default Values  :  ' , f1 . _defaults_)
f1()

output:-
---------
a :   HydSec
b :   [1, 2, 3]
a :   HydSec
b :   [1, 2, 3, 1, 2, 3]
a :   HydSec
b :   [1, 2, 3, 1, 2, 3, 1, 2, 3]

































