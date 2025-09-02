a = [25, 10.8, 'Hyd', True]
print(len(a))   # 4

b = []
print(len(b))   # 0

c = [[10, 20], 30, 40]
print(len(c))   # 3


'''
What does len(list) do ?  --->  Returns number of elements in the list
'''





a = [25, 10.8, True]
print(sum(a))   
# 25 + 10.8 + 1(True) = 36.8

b = [3 + 4j, 5 + 6j]
print(sum(b))   
# (3+4j) + (5+6j) = (8+10j)

c = [25, 10.8, True, 3 + 4j, False]
print(sum(c))   
# 25 + 10.8 + 1(True) + (3+4j) + 0(False) = (39.8+4j)

d = [10, 20, 15, 18]
print(sum(d))   
# 63

e = [25, 10.8, 'Hyd', True]
print(sum(e))   
#  TypeError'





 a = [[10, 20, 15, 18]]

print(sum(a))  # Error
# Because sum() tries to add [] to 0, but 'a' contains a list inside a list.

print(sum(a[0]))        # 63
print(sum(*a))          # 63





 a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a))     # 30
print(min(a))     # 5

b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b))     # Vamsi
print(min(b))     # Amar

c = [25 , 10.8 ,  3 + 4j , True]
print(max(c))     # Error

d = [25 , '35']
print(max(d))     # Error
print(max([]))    # Error
print(min([]))    # Error




# list()  function  demo  program
a = (10 , 20 , 15, 18)
b = list(a)
print(b)          # [10, 20, 15, 18]
print(type(b))    # <class 'list'>
print(a is b)     # False
print(a == b)     # False




 #  Find  outputs (Home  work)
a = range(4 , 10 , 2)
b = list(a)
print(b)          # [4, 6, 8]
print(type(b))    # <class 'list'>

a = list('Vamsi')
print(a)          # ['V', 'a', 'm', 's', 'i']

a = list()
print(a)          # []

print(list(25))   # Error
print(list(10.8)) # Error
print(list(True)) # Error
print(list(None)) # Error
[19/08, 12:20 am] .: a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90))
print(list(a))    
# [(10, 20), (30, 40, 50), (60, 70, 80, 90)]

b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)}
print(list(b))    
# Order may vary because set is unordered, e.g.
# [(10, 20), (30, 40, 50), (60, 70, 80, 90)]

c = ([10 , 20] , (30 , 40) , {50 , 60})
print(list(c))    
# [[10, 20], (30, 40), {50, 60}]




 a = [10 , 20 , 15 , 5 , 12]
b = sorted(a)
print(b)          # [5, 10, 12, 15, 20]
print(type(b))    # <class 'list'>

c = sorted(a , reverse = True)
print(c)          # [20, 15, 12, 10, 5]
print(a)          # [10, 20, 15, 5, 12]





a = ['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama  Rao']
b = sorted(a)
print(b)  
# ['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']

c = sorted(a , reverse = True)
print(c)  
# ['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']

print(a)  
# ['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama  Rao']





a = [12 > 10 , 5 < 20 , 30 == 30]
print(all(a))    # True

b = [9 >= 6 , 12 <= 9 , 6 == 6]
print(all(b))    # False

c = [25 , 10.8 , '' , True , 3+4j , 'Hyd']
print(all(c))    # False   (because '' is False)

d = [10 , 0 , 20]
print(all(d))    # False   (0 is False)

e = []
print(all(e))    # True    (vacuous truth)





a  = [12 > 18 , 5 < 20 , 35 == 30]
print(any(a))    # True

b = [12 > 18 , 25 < 20 , 35 == 30]
print(any(b))    # False

c = [0 , 0.0 , '' , 25 , 0 + 0j , False]
print(any(c))    # True

d = [0 , 0.0 , '' , 0 + 0j , False]
print(any(d))    # False

e = []
print(any(e))    # False



a = [10 , 20 , 15 , 18]
print(a)         # [10, 20, 15, 18]

del a[2]
print(a)         # [10, 20, 18]

del a[3]         # Error (list has only 3 elements now)
del a            # Deletes the whole list
print(a)         # Error (a is deleted)
[19/08, 12:21 am] .: list = [10 , 20 , 15 , 18]
print(list)          # [10, 20, 15, 18]

list.append(19)
print(list)          # [10, 20, 15, 18, 19]
[19/08, 12:21 am] .: list = []
print(list)          # []

list.append(25)
list.append(10.8)
list.append('Hyd')
list.append(True)
print(list)          # [25, 10.8, 'Hyd', True]
[19/08, 12:21 am] .: list = []
for x in range(0 , 50 , 10):
    list.append(x)
print(list)          # [0, 10, 20, 30, 40]




 a = [10 , 20 , 30]
a.append('Hyd')
print(a)             # [10, 20, 30, 'Hyd']
print(len(a))        # 4

# Printing individual elements
print(a[3])          # Hyd
print(a[3][0])       # H
print(a[3][1])       # y
print(a[3][2])       # d
[19/08, 12:22 am] .: try:
    list = [10 , 20 , 15 , 18 , 15 , 12 , 15 , 19]
    list.remove(15)
    print(list)      # [10, 20, 18, 15, 12, 15, 19]

    list.remove(25)  # Error
except:
    print('25  is   not  in  the  list')
[19/08, 12:25 am] .: # Program to delete all occurrences of 'x' from the list

a = eval(input("Enter List  :  "))
x = eval(input("Enter  element  to  be  deleted : "))

# remove all occurrences of x
result = [i for i in a if i != x]

print("List  without  {}'s : ".format(x), result)
