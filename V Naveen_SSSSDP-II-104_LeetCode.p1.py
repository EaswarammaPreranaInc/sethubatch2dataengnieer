'''
Example :

Input: haystack = "sadbutsad", needle = "sad"

Output: 0

Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
'''


class Solution(object):
    def strStr(self, haystack, needle):
        return(haystack.find(needle))
        