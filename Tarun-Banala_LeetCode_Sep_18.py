#TARUN BANALA        18-09-2025
#Question:
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
 

Constraints:

-231 <= x <= 231 - 1
'''

#Answer:

class Solution:
    def reverse(self, x):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        
        reversed_x = 0
        while x != 0:
            digit = x % 10
            x //= 10
            
            # Check for overflow before adding the digit
            if sign == 1:
                if reversed_x > INT_MAX // 10 or (reversed_x == INT_MAX // 10 and digit > INT_MAX % 10):
                    return 0
            else:
                if reversed_x > abs(INT_MIN) // 10 or (reversed_x == abs(INT_MIN) // 10 and digit > abs(INT_MIN) % 10):
                    return 0
            
            reversed_x = reversed_x * 10 + digit
        
        return sign * reversed_x
        
