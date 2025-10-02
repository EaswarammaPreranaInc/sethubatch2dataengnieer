'''
    Problem : Given an array arr of size N, find the index of any one of its peak elements.
    An array element is considered a peak if it is NOT smaller than its neighbors.
    For corner elements, we need to consider only one neighbor.
    Note: The output index should be 0-based.
    Link : https://practice.geeksforgeeks.org/problems/peak-element/1
    Difficulty : Medium
    Category : Arrays
'''

class Solution:   
    def peakElement(self, arr):
        # Code here
        n = len(arr)
        low = 0
        high = n-1
        
        while(low<high):
            mid = (low+high)//2
            if arr[mid]<arr[mid+1]:
                low = mid+1
            else:
                high = mid
            
        return low