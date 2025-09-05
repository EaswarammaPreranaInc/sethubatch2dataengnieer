#  Find  outputs 
def  change(b):
	b . append(25) # adds 25 at the end
	b[2] = 17 # modify element at index 2
	del  b[1] # deletes element at index 1
# End  of  the  function
a = [10 , 20 , 15 , 18]
print(a) # [10,20,15,18]
change(a) # As 'a' and 'b' points to the same list, modifying 'b' modifies 'a' also
print(a) # [10,17,18,25]



# Find  outputs  
def  change(b):
	b  = [50 , 60 , 70 , 80]
	print(b)
# End  of  the  function
a = [10 , 20 , 30 , 40]
print(a) # [10,20,30,40]
change(a) # [50,60,70,80] : 'b' initially refers to same list as 'a' then b points to different list
print(a) # [10,20,30,40]



#  Find  outputs 
def   f1(x):
	x = 20
	print(x) # local variable has higher priority compare to the global
# End  of   the   function
x = 10
print(x) 
f1(x) 
print(x)
'''
10
20
10'''



#  Find  outputs  
def  f1(b):
	 #b[2] = 25 # error : tuple is immutable. so, cannot modify the value
	 pass
#end  of  the  function
a = (10 , 20 , 15 , 18)
print(a)
f1(a)
print(a)

'''
(10,20,15,18)
(10,20,15,18)
'''














