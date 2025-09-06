
# home work on 05/09/2025 part 2 

#  Find  outputs  (Home  work)
def  change(b):
    b.append(25)
    b[2] = 17
    del  b[1]
# End  of  the  function
a = [10 , 20 , 15 , 18]
print(a)      # [10, 20, 15, 18]
change(a)
print(a)      # [10, 17, 18, 25]
'''
1)  a = [10 , 20 , 15 , 18]
    change(a)
    What  is   passed  to  change()  function ? --->
	List  itself  but  not  elements  of  list
2) Modifying  list  'b' is  as  good  as  modifying  list  'a'  becoz  'a'  and  'b'  point  to  same  list
'''
---
# Find  outputs  (Home  work)
def  change(b):
    b  = [50 , 60 , 70 , 80]
    print(b)  # [50, 60, 70, 80]
# End  of  the  function
a = [10 , 20 , 30 , 40]
print(a)      # [10, 20, 30, 40]
change(a)
print(a)      # [10, 20, 30, 40]
---
#  Find  outputs  (Home  work)
def   f1(x):
    x = 20
    print(x)  # 20
# End  of   the   function
x = 10
print(x)      # 10
f1(x)
print(x)      # 10
---
#  Find  outputs  (Home  work)
def  f1(b):
    b[2] = 25
#end  of  the  function
a = (10 , 20 , 15 , 18)
print(a)      # (10, 20, 15, 18)
f1(a)         # TypeError: 'tuple' object does not support item assignment
print(a)      # (This line is not reached due to the error)
