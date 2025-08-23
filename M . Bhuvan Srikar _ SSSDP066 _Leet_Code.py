#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#The overall run time complexity should be O(log (m+n)).
#Example 1:
#Input: nums1 = [1,3], nums2 = [2]
#Output: 2.00000
#Explanation: merged array = [1,2,3] and median is 2.
#Example 2:
#Input: nums1 = [1,2], nums2 = [3,4]
#Output: 2.50000
#Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

a = eval(input('enter a list1 of numbers : '))
b = eval(input('enter a list2 of numbers : '))
c = a + b
d = sorted(c)
if len(d) % 2 != 0:
	e = d[len(d)//2]
	print(f'merged list is {d} and median is {e}')
else:
	f = (d[len(d)//2] +  d[len(d)//2 - 1]) / 2
	print(f'merged list is {d} and median is {f}')


#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#The overall run time complexity should be O(log (m+n)).
#Example 1:
#Input: nums1 = [1,3], nums2 = [2]
#Output: 2.00000
#Explanation: merged array = [1,2,3] and median is 2.
#Example 2:
#Input: nums1 = [1,2], nums2 = [3,4]
#Output: 2.50000
#Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

a = eval(input('enter a list1 of numbers : '))
b = eval(input('enter a list2 of numbers : '))
c = a + b
d = sorted(c)
if len(d) % 2 != 0:
	e = d[len(d)//2]
	print(f'merged list is {d} and median is {e}')
else:
	f = (d[len(d)//2] +  d[len(d)//2 - 1]) / 2
	print(f'merged list is {d} and median is {f}')


'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
Example 1:
Input: x = 123
Output: 321
Example 2:
Input: x = -123
Output: -321
Example 3:
Input: x = 120
Output: 21
'''
a = int(input('Enter a number: '))
b = 0
sign = 0
if a < 0:
	sign = -1
else:
	sign = 1
a = abs(a)
def f1(a):
	sum = 0
	while a != 0:
		b = a % 10
		sum = sum * 10 + b
		a = a // 10 
	return sign * sum
c = f1(a)
print(f'reverse number is {c}')


#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#Notice that the solution set must not contain duplicate triplets.
#Example 1:
#Input: nums = [-1,0,1,2,-1,-4]
#Output: [[-1,-1,2],[-1,0,1]]
#Explanation: 
#nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
#nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
#nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
#The distinct triplets are [-1,0,1] and [-1,-1,2].
#Notice that the order of the output and the order of the triplets does not matter.
#Example 2:
#Input: nums = [0,1,1]
#Output: []
#Explanation: The only possible triplet does not sum up to 0.
#Example 3:
#Input: nums = [0,0,0]
#Output: [[0,0,0]]
#Explanation: The only possible triplet sums up to 0.
a = eval(input('Enter a List : '))
def f1(a): 
	b = []
	for i in range(len(a)): 
		for j in range(i + 1 , len(a)):
			for k in range(j + 1 , len(a)): 
				if a[i] + a[j] + a[k] == 0:
					t = sorted([a[i] , a[j] , a[k]])
					if t not in b:
						b . append(triplet)
	return b
c = f1(a)
print(f'The Distinct Triplets are : {c}')


#You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
#Merge all the linked-lists into one sorted linked-list and return it.
#Example 1:
#Input: lists = [[1,4,5],[1,3,4],[2,6]]
#Output: [1,1,2,3,4,4,5,6]
#Explanation: The linked-lists are:
#[
#  1->4->5,
#  1->3->4,
#  2->6
#]
#merging them into one sorted linked list:
#1->1->2->3->4->4->5->6
#Example 2:
#Input: lists = []
#Output: []
#Example 3:
#Input: lists = [[]]
#Output: []

a = eval(input('Enter a group of nested lists: '))
b = []
for i in range(len(a)):
	for j in range(len(a[i])):
		b . append(a[i][j])
print(f'Sorted and merged list is : {sorted(b)}')


#Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
#Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
#Example 1:
#Input: num1 = "2", num2 = "3"
#Output: "6"
#Example 2:
#Input: num1 = "123", num2 = "456"
#Output: "56088"
a = input('Enter 1st string number: ')
b = input('Enter 2nd string number: ')
c = float(a)
d = float(b)
e = c * d
f = str(e)
print(f'Multiplied String : {f}')
print(type(f))




'''
Given an array of integers nums sorted in non-decreasing order, find the starting 
and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
'''
a = eval(input('Enter a List : '))
target = int(input('Enter a number to be searched : '))
def f1(a , target):
	b = []
	c = []
	for i in range(len(a)):
		if a[i] == target:
			b . append(i)
	if len(b) == 0:
		return [-1 , -1]
	else:
		return [b[0] , b[-1]]
result = f1(a , target)
print(f'Output : {result}')



'''
There is an integer array nums sorted in non-decreasing order 
(not necessarily with distinct values).
Before being passed to your function, nums is rotated at an unknown 
pivot index k (0 <= k < nums.length) such that the resulting array is 
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become
[4,5,6,6,7,0,1,2,4,4].
Given the array nums after the rotation and an integer target, 
return true if target is in nums, or false if it is not in nums.
You must decrease the overall operation steps as much as possible.
Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
'''
a = eval(input('Enter a list : '))
target = int(input('Enter a number to be searched : '))
def f1(a):
	ctr = 0
	for i in range(len(a)):
		if a[i] == target:
			ctr += 1
	if ctr > 0:
		return True , ctr
	else :
		return False , ctr
result , count = f1(a)
print(f'Output : {result} and repeated {count} times')


'''
integer to roman
even different symbols represent Roman numerals with the following values:
Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000
Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:
If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.
Given an integer, convert it to a Roman numeral.
Example 1:
Input: num = 374
Output: "MMMDCCXLIX"
Explanation:
3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC as 500 (D) + 100 (C) + 100 (C)
  40 = XL as 10 (X) less of 50 (L)
   9 = IX as 1 (I) less of 10 (X)
Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places
Example 2:
Input: num = 58
Output: "LVIII"
Explanation:
50 = L
8 = VIII
Example 3:
Input: num = 1994
Output: "MCMXCIV
Explanation:
1000 = M
 900 = CM
  90 = XC
   4 = IV
'''
Roman = [('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
    ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)]

num = int(input('Enter a number : '))
def f1(Roman , num):
	a = []
	for x , y in Roman:
		count = num // y
		a . append(x * count)
		num = num % y
	return a
list = f1(Roman , num)
print(f'Roman Number of {num} is {''.join(list)}')



'''
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]
Explanation:
Example 2:
Input: head = []
Output: []
Example 3:
Input: head = [1]
Output: [1]
Example 4:
Input: head = [1,2,3]
Output: [2,1,3]
'''
a = eval(input('Enter a list : '))
def f1(a):
	b = []
	for i in range(0 , len(a) - 1 , 2):
		b . append(a[i + 1])
		b . append(a[i])
	if len(a) % 2 != 0:
		b . append(a[-1])
	return b
result = f1(a)
print(f'Swaped list : {result}')	

'''
The count-and-say sequence is a sequence of digit strings 
defined by the recursive formula:
countAndSay(1) = "1"
countAndSay(n) is the run-length encoding of countAndSay(n - 1).
Run-length encoding (RLE) is a string compression method that 
works by replacing consecutive identical characters (repeated 2 or more times)
with the concatenation of the character and the number marking the count 
of the characters (length of the run). For example, to compress the string "3322251"
we replace "33" with "23", replace "222" with "32", replace "5" with "15" and 
replace "1" with "11". Thus the compressed string becomes "23321511".
Given a positive integer n, return the nth element of the count-and-say sequence.
Example 1:
Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = RLE of "1" = "11"
countAndSay(3) = RLE of "11" = "21"
countAndSay(4) = RLE of "21" = "1211"
Example 2:
Input: n = 1
Output: "1"
Explanation:
This is the base case.
'''
a = input('Enter a number : ') # 33222511
b = list(a) # [3 , 3 , 2 , 2 , 2 , 5 , 1 , 1]
def countsay(a):
	count = 1
	c = []
	for i in range(1 , len(b)):
		if b[i] == b[i - 1]:
			count += 1
		else:
			c . append(str(count))
			c . append(b[i - 1])
			count = 1
	c . append(str(count))
	c . append(b[-1])
	return c
result = countsay(a)
e = '' .join(result)
print(f'Output : {e}')

'''
Given an array nums with n objects colored red, white, or blue, 
sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, 
and blue, respectively.
You must solve this problem without using the library's sort function.
Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]
'''
a = eval(input('Enter a list between (0 , 1 and 2) : '))
for i in range(len(a)):
	if a[i] > 2:
		print('Please enter a value between 0 to 2')
		exit()
	else:
		def nums(a):
			b = []
			for x in [0 , 1 , 2]:
				for y in a:
					if x == y:
						b . append(y)
			return b
d = nums(a)
print(f'Output : {d}')

#def mull(list , a , b):
#	for i in range(a):
#		minn = list.index(min(list))
#		list[minn] = list[minn] * b
#	return list
#list = eval(input('Enter a list : '))
#a = int(input('How many times want to mutliply : '))
#b = int(input('Number to multiply : '))
#c = mull(list , a , b)
#print(f'modified list : {c}')

class c1:
	def get(self):
		self . list = eval(input('Enter a list : '))
		self . a = int(input('How many times want to mutliply : '))
		self . b = int(input('Number to multiply : '))
	def mull(self):
		for i in range(self . a):
			self . minn = self.list.index(min(self.list))
			self.list[self.minn] = self.list[self.minn] * self . b
		return self.list
o = c1()
o.get()
d = o.mull()
print(f'modified list : {d}')


d = [ '' , '@' , 'abc','def','ghi' ,'jkl','mno',
     'pqrs','tuv','xyz']
a = input('Enter a number : ') # 23
e = list(a)
b = []
#for x in d[int(e[0])]:
#	for y in d[int(e[1])]:
#		b . append(x + y)
#print(b)
z = list(d[int(a[0])])
for x in a[1:]:
	num = d[int(x)]
	result = []
	for h in z:
		for y in num:
			result . append(h + y)
	z  = result
print(z)


import math
a = eval(input('Enter a List : '))
b = eval(input('Enter a list : '))
c = a + b
d = sorted(c)
def median(d) : 
	if len(d) % 2 == 0:
		return (d[((len(d) - 1) // 2)] + d[(((len(d)-1) // 2 )+ 1)]) / 2
	else:
		return d[math.floor(len(d) / 2)]
result = median(d)
print(f'The median of {d} is {result}')

a = eval(input('Enter a List : '))
b = int(input('Enter a number to be searched : '))
a . sort() # [-2 , -1 , 0 , 0 , 1 , 2]
c = []
total = 0
for i in range(len(a)):
	for j in range(i+1 , len(a)):
		for k in range(i+2 , len(a)):
			for l in range(i+3 , len(a)):
				if a[i] + a[j] + a[k] + a[l] == b:
					result = [a[i] , a[j] , a[k] , a[l]]
					if result not in c: 
						c . append(result)
print(f'Output : {c}')


import itertools
def disp(a):
	i = 0
	while i < 2:
		print(next(a))
		i += 1
a = eval(input('Enter a list : '))
p = itertools.permutations(a , 3)
disp(p)


# 34
a = eval(input('Enter a list : '))
b = int(input('Target : '))
try:
	c = []
	i = a . index(b)
	while  b in  a:
		c . append(i)
		i = a . index(b , i + 1)
		a . remove(b)
except ValueError as msg:
	print(msg)
print(f'Output : {c}')

'''
Given an integer array nums, find the subarray with the largest sum,
and return its sum.
Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
kadnae's algorithm
'''
a = eval(input('Enter a list : '))
def maxsum(a):
	sum1 = sum2 = a[0] 
	for x in a[1::]:
		sum1 = max(x , sum1 + x) 
		sum2 = max(sum1 , sum2)
	return sum2
result = maxsum(a)
print(f'The largest sum is {result}')
