
# 1)Find  outputs  
def  change(b):
	b . append(25)
	b[2] = 17
	del  b[1]
# End  of  the  function
a = [10 , 20 , 15 , 18]
print(a)#[10, 20, 15, 18]
change(a)
print(a)#[10, 17, 18, 25]





#2)  Find  outputs  
def  change(b):
	b  = [50 , 60 , 70 , 80]
	print(b)
# End  of  the  function
a = [10 , 20 , 30 , 40]
print(a)#[10, 20, 30, 40]
change(a)#[50, 60, 70, 80]
print(a)#[10, 20, 30, 40]





# 3)  Find  outputs  
def   f1(x):
	x = 20
	print(x)
# End  of   the   function
x = 10
print(x)#10
f1(x) #20
print(x)#10





# 4) Find  outputs  
def  f1(b):
	b[2] = 25
#end  of  the  function
a = (10 , 20 , 15 , 18)
print(a) #(10, 20, 15, 18)
#f1(a)#Throws error as tuple is immutable
print(a) #(10, 20, 15, 18)