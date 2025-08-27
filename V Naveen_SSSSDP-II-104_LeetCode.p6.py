'''
Example:

Input: x = 121

Output: true

Explanation: 121 reads as 121 from left to right and from right to left.
'''


class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        s = str(x)
        return s == s[::-1]  
