'''
for  i   in   range(1,8):
	print(i)
	if i % 3  == 0:
			continue
	else:
			print('Sec')
	print('Hello')
# End of loop
print('Outside loop')

for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		break
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')

for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		pass
		print('Hyd')
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')

for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		exit()
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')

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
print('Outside  loop')

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
print('Outside  loop')

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
print('Outside loop')

lst = eval(input("Enter any list: "))
key = eval(input("Enter the element to be searched: "))

found = False

for i in range(len(lst)):
    if lst[i] == key:
        print("Found at index:", i)
        found = True
        break

if not found:
    print("Not Found")

lst = eval(input("Enter any list: "))
key = int(input("Enter element to search for: "))

count = 0

for i in range(len(lst)):
    if lst[i] == key:
        print(f"{key} is found at index {i}")
        count += 1

if count > 0:
    print(f"{key} is found {count} times")
else:
    print(f"{key} is not found")
'''
total = 0
count = 0

print("Enter input (Ctrl + Z or Ctrl + D to stop):")

while True:
    try:
        value = eval(input("Enter input (ctrl + z to stop) : "))
        total += value
        count += 1
    except EOFError:
        break

if count > 0:
    average = total / count
    print("Average:", average)
else:
    print("No inputs entered.")
