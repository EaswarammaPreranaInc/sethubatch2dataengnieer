'''
    Problem: First non-repeating character in a string    
    Link : https://www.geeksforgeeks.org/problems/non-repeating-character-1587115620/1?page=1&category=Strings&sortBy=submissions
    Category: Strings       
    Difficulty: Easy
'''


class Solution:
    def nonRepeatingChar(self,s):
        #code here
        d = {}
        
        for i in s:
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 1
        
        for i in s:
            if d[i] == 1:
                return i
        
        return '$'
    
    