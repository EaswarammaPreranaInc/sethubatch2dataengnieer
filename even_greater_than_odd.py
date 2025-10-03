'''
    Problem : Given an array of integers arr, rearrange the elements of arr such that
    - arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= ...
    - The rearrangement should be done in-place, meaning you should modify the input array directly without using extra space for another array.
    - If there are multiple valid rearrangements, you can return any of them.  

    Link : https://www.geeksforgeeks.org/problems/rearrange-array-such-that-even-positioned-are-greater-than-odd4804/1
    Difficulty : Easy
    Category : Arrays
 '''

class Solution:
    def rearrangeArray(self, arr):
        # code here
        
        n = len(arr)
        
        for i in range(1,n):
            if i%2==1:
                if arr[i]<arr[i-1]:
                    arr[i],arr[i-1] = arr[i-1],arr[i]
            else:               
                if arr[i]>arr[i-1]:
                    arr[i],arr[i-1] = arr[i-1],arr[i]
        
        return arr
                