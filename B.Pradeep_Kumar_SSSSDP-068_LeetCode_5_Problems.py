'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
'''
a=eval(input("Enter l1 :"))
b=eval(input("Enter l2 :"))
c=""
d=""
for i in a[::-1]:
    c+=str(i)
for j in b[::-1]:
    d+=str(j)
e=str(int(c)+int(d))
f=[]
g=[]
for k in e[::-1]:
    f+=(k)
for s in f:
    g.append(int(s))
print(g)



'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
'''
a=eval(input("Enter 1st input : "))
b=eval(input("Enter 2nd input : "))
c=sorted(a+b)
for i in c:
    if len(c)%2==0:
        print(f"sorted is : {c} and Median is : ",(c[((len(c))//2)-1]+c[len(c)//2])/2)
        break
    else:
        print(f"sorted is : {c} and Median is : ",c[(len(c)-1)//2])
        break



'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
'''
def string(x):
    c=[]
    i=0
    try:
        if len(x)==2:
            for p in a[int(x[i:i+1:1])]:
                for q in a[int(x[i+1:i+2:1])]:
                    c.append(p+q)
        elif len(x)==0:
            pass
        else:
            for i in a[int(x[i:i+1:1])]:
                c.append(i)
    except ValueError:
        print("Enter integer between 0-99 ")
    return c
x=input("Enter a number between 0-99: ")
a={0:"",1:"",2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
print(string(x))


'''
SPACE  #    x[0:4:1] + x[0::-1]
PACES  #   x[1:4:1]  + x[1::-1]
ACESP  #   x[2:4:1]  + x[]
CESPA  #   x[3:4:1]
ESPAC  #   x[4:4:1]
'''

x=input("Enter a input : ")
i=0
while i<=len(x):
    print(x[i:len(x):]+x[0:i])
    i=i+1
    
    


'''
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.
Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
'''
def rev():
    a=eval(input("enter a list : "))
    b=int(input("Enter a number : "))
    c=sorted(a,reverse=True)
    d=[]
    for i in c:
        if i<=b:
            d.append(i)
    for j in a[b::]:
        d.append(j)
    return d
k=rev()
print(k)
