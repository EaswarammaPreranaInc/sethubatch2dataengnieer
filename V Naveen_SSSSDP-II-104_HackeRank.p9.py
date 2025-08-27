'''
Sample Input:
5
12 9 61 5 14 

Sample Output:
True

Explanation:
Condition 1: All the integers in the list are positive.
Condition 2: 5 is a palindromic integer.

Hence, the output is True.
'''


n,nums=int(input()),input().split()
print(all(int(x)>0 for x in nums) and any(x==x[::-1] for x in nums))
