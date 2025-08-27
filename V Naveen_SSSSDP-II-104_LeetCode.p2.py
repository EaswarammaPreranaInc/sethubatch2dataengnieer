'''
Example 1:

Input: s = "Hello World"

Output: 5

Explanation: The last word is "World" with length 5.
'''


class Solution(object):
    def lengthOfLastWord(self, s):
        k = s.split()
        return len(k[-1])