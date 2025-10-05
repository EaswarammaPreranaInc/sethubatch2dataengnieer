'''
    Problem: Multiply two strings 
    Link: https://www.geeksforgeeks.org/problems/multiply-two-strings/1?page=1&category=Strings&difficulty=Medium&sortBy=submissions
    Category: Strings       
    Difficulty: Medium
'''


class Solution:
    def multiplyStrings(self, s1, s2):
        # code here
        n1 = int(s1)
        n2 = int(s2)
        sign = 1
        if n1<0:
            n1 = -(n1)
            sign *= -1
        if n2<0:
            n2 = -(n2)
            sign *= -1
        
        if sign > 0:
            return n1*n2
        else:
            return -(n1*n2)