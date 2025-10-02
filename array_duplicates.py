
'''
    Problem: Array Duplicates 
    Link: https://www.geeksforgeeks.org/problems/find-duplicates-in-an-array/1?page=1&category=Arrays,Strings&sortBy=submissions
    Category: Arrays
    Difficulty: Easy
'''



class Solution:
    def findDuplicates(self, arr):
        # code here
        freq = {}
        n = len(arr)
        for i in range(n):
            if arr[i] in freq.keys():
                freq[arr[i]] += 1
            else:
                freq[arr[i]] = 1
        result = []
        for i,j in freq.items():
            if j>1:
                result.append(i)
                
        return result
            
        
        
        