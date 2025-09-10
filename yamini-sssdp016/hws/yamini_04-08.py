# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i) # i is printed from 1 to 7
	if  i % 3  == 0:
			continue # when i%3==0 like for 3 6 the execution is skipped
	else:
			print('Sec') # except for 3 and 6 all times sec is printed
	print('Hello')  # for every iteration hello is printed
# End of loop
print('Outside loop') # only once this statement is printed

# Identify Error  (Home  work)
if ():
	print('Hyd')
	#continue # continue is only used in loops like for while
	print('Sec')
	
# Find outputs (Home  work)
for  i   in   range(1 , 8):
	print(i) # i is printed from 1 to 7
	if   i % 3 == 0: # the loop is breaked and the execution is stopped when i is 3
		break
	else:
		print('Sec') # else will run only for 1 2
	print('Hello') #hello is printed 2 times
# End  of  the  loop
print('Outside loop')  # it is printed only 1 time

# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	#break # break is used only in loops so error
	print('Sec')
	
# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)  # i is printed from 1 to 7
	if   i % 3 == 0:
		pass  # pass statement doesnt make any change in the execution
		print('Hyd') # hyd is printed when i is 3 and 6
	else:
		print('Sec') # sec is printed except for 3 and 6
	print('Hello') # hello is printed every time
# End  of  the  loop
print('Outside loop') # only one time after end of loop


# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)  # i is printed from 1 to 7
	if   i % 3 == 0:    
		exit() # when i is 3 the loop gets exitted
	else:
		print('Sec') # sec is printed only for 1 and 2
	print('Hello') # hello is printed 2 times
# End  of  the  loop
print('Outside loop') # this statement is skipped

print()
# Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i)  # i is printed from 1 to 7
	if   i % 3 == 0:
		continue
	else:
		print('Sec')
	print('Hello')
else:
	print('else  suite')
# End  of  the  loop
print('Outside  loop')
	
