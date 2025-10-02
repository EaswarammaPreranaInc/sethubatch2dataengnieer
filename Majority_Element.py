'''
    Problem : Given an array of size N. Find all elements in array that appear more than n/3 times.
    Link: https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/majority-vote
    Difficulty: Medium
    category: Arrays
'''

class Solution:
    def findMajority(self, arr):
        # code here
        n = len(arr)
        f = n//3
        freq_dict = {}
        result = []
        
        for i in arr:
            if i in freq_dict:
                freq_dict[i] += 1
            else:
                freq_dict[i] = 1
        
        for key,value in freq_dict.items():
            if value>f:
                result.append(key)
        
        return sorted(result)
                
                