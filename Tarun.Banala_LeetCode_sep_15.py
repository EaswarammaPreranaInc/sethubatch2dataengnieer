#TARUN BANALA 
'''
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
'''

#Answer:
class Solution:
    def longestPalindrome(self, s):
        if len(s) <= 1:
            return s
        
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        longest = ""
        for i in range(len(s)):
            # Check for odd-length palindromes (center at i)
            palindrome_odd = expand_around_center(i, i)
            if len(palindrome_odd) > len(longest):
                longest = palindrome_odd
            
            # Check for even-length palindromes (center between i and i+1)
            palindrome_even = expand_around_center(i, i + 1)
            if len(palindrome_even) > len(longest):
                longest = palindrome_even
        
        return longest
        
