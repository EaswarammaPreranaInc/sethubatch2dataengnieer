'''
    Problem Statement: Given an array Arr of N integers.
    Find the contiguous sub-array (containing at least one number) which has the maximum sum and return its sum.
    Link: https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/kadanes-algorithm-1587115620
    Difficulty: Medium
    Category: Arrays
'''


class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        current_sum = arr[0]
        max_sum = arr[0]
        n = len(arr)
        
        for i in range(1,n):
            current_sum = max(current_sum+arr[i],arr[i])
            
            max_sum = max(max_sum,current_sum)
            
        return max_sum