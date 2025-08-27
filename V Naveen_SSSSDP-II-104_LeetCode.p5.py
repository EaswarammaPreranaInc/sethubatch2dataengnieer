'''
Example 1:

Input: nums = [3,2,1]

Output: 1

Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
'''


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        k = list(set(nums))
        k.sort()
        if len(k) == 2:
            return k[1]
        elif len(k) == 1:
            return k[0]
        else:
            return k[-3]    