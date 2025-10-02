'''
    problem :Given an array of size N containing elements from 1 to N.
    You need to find the frequency of all elements from 1 to N in the array.
    Link: https://practice.geeksforgeeks.org/problems/frequency-of-array-elements-1587115620/1?page=1&category=Arrays&sortBy=submissions
    Difficulty: Easy
    Category: Arrays
'''

class Solution:
    def frequencyCount(self, arr):
        #  code here
        n = len(arr)
        result = []
        freq_dict={}
        for i in arr:
            if i in freq_dict:
                freq_dict[i] += 1
            else:
                freq_dict[i] = 1
        
        for i in range(1,n+1):
            if i in freq_dict:
                result.append(freq_dict[i])
            else:
                result.append(0)
        
        return result 
                

