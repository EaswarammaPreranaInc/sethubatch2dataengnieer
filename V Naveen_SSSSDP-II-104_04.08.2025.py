#1. Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if  i % 3  == 0:
			continue
	else:
			print('Sec')
	print('Hello')
# End of loop
print('Outside loop')
'''1
Sec
Hello
2
Sec
Hello
3
4
Sec
Hello
5
Sec
Hello
6
7
Sec
Hello
Outside loop '''



#2. Identify Error  (Home  work)
if ():
	print('Hyd')
	continue # Error due to only for and while loops can use continue 
	print('Sec')


#3. Find outputs (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		break
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')

'''1
Sec
Hello
2
Sec
Hello
3
Outside loop
'''



#4. Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	break #Error due to only for and while loops can use break
	print('Sec')



#5. Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		pass
		print('Hyd')
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')
'''
1
Sec
Hello
2
Sec
Hello
3
Hyd
Hello
4
Sec
Hello
5
Sec
Hello
6
Hyd
Hello
7
Sec
Hello
Outside loop
'''



#6. Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		exit()
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')

'''
1
Sec
Hello
2
Sec
Hello
3
'''




#8. Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i)
	if   i % 3 == 0:
		continue
	else:
		print('Sec')
	print('Hello')
else:
	print('else  suite')
# End  of  the  loop
print('Outside  loop')

'''
1
Sec
Hello
2
Sec
Hello
3
4
Sec
Hello
5
Sec
Hello
6
7
Sec
Hello
else  suite
Outside  loop

'''


#9. Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i)
	if  i % 3 == 0:
		break
	else:
		print('Sec')
	print('Hello')
else:
	print('else  suite')
#End   of  the  loop
print('Outside  loop')

'''
1
Sec
Hello
2
Sec
Hello
3
Outside  loop
'''



#10. Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i)
	if  i == 8:
		break
	else:
		print('Sec')
	print('Hello')
else:
	print('else  suite')
# End  of  the  loop
print('Outside loop') 
'''
1
Sec
Hello
2
Sec
Hello
3
Sec
Hello
4
Sec
Hello
5
Sec
Hello
6
Sec
Hello
7
Sec
Hello
else  suite
Outside loop
'''



#11. program to search for an element
a = eval(input("Enter any list : "))
b = eval(input("Enter the element to be searched : "))
for i in range(len(a)):
    if a[i] == b:
        print("Found at index : " , i)
        break
else:
    print("Not Found")




#12. program to search element in list with index
a = eval(input("Enter any list : "))
b = eval(input("Enter the element to be searched : "))
count = 0
for i in range(len(a)):
    if a[i] == b:
        print( f'{b}'" is found at index : " , i)
        count += 1
if b in a:
    print(f'{b}'" is found " f'{count}' " times")
else:
    print("Not found")

'''
Enter any list : [10, 20, 13, 12, 13]
Enter the element to be searched : 13
13 is found at index :  2
13 is found at index :  4
13 is found 2 times
'''



#13.  Walrus   operator (:=)  demo  program
print(a := 25) # 25
#print(a = 25) # Error
print(a) # 25
print(a := 6 + 7) # 13
print(a) # 13
print((a := 6) + 7) # 13
print(a) # 6
#print((a = 6) + 7) # Error due to invalid arg




#14. Find  outputs  (Home  work)
a = 0
if  a == 0:
	print('Hyd') # Hyd
else:
	print('Sec')
if  b := 0:
	print('Hyd') 
else:
	print('Sec : ' , b) # sec : 0
if  c = 0: # Error due to c is not defined
	print('Hyd')
else:
	print('Sec')




#15. average of inputs
sum = 0
c = 0
try:
    while True:
        a = eval(input("Enter input (ctrl + Z to stop) : " ))
        sum += a
        c += 1
except:
    print("Average : " ,sum/c)
    
'''
Enter input (ctrl + Z to stop) : 23
Enter input (ctrl + Z to stop) : 45
Enter input (ctrl + Z to stop) : 23
Enter input (ctrl + Z to stop) : 5
Enter input (ctrl + Z to stop) : 35
Enter input (ctrl + Z to stop) : 
Average :  26.2
'''



#16.  del  operator  demo program  (Home  work)
a = 25
print(a) # 25
del   a
print(a) # Error due to a is already deleted




#17. Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c) # 25<space>25<space>25
del   a
print(b , c) # 25<space>25<space>
print(a) # Error due to a is deleted
del   b
print(c) # 25
print(b) # Error due to b is deleted
del   c
print(c) # Error due to c is deleted


#18.  Can  multiple  objects  be  deleted  with  same  del  operator ? Yes
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c) # 25<space>10.8<space>Hyd
del   a , b , c
print(a) # Error due to a is deleted
print(b) # Error due to b is deleted
print(c) # Error due to c is deleted



#19. Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a) # [10 , 20 , 15 , 18]
del  a[2]
print(a) # [10 , 20 , 18]
del  a
print(a) # Error due to list 'a' is deleted
print(a[0]) # Error



#20. Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a) # (10 , 20 , 15 , 18)
print(a[0]) # 10
del  a[2]
del  a
print(a) # Error due to tuple 'a' is deleted
print(a[0]) # Error