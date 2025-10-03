"""
Problem: Anagram 
Link: https://www.geeksforgeeks.org/problems/anagram-1587115620/1
Category: Strings
Difficulty: Easy
"""

class Solution:
    def areAnagrams(self, s1, s2):
        if len(s1) != len(s2):
            return False
        
        lt1 = sorted(s1)
        lt2 = sorted(s2)
        
        for i in range(len(s1)):
            if lt1[i] != lt2[i]:
                return False
        return True
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.areAnagrams("listen", "silent"))     # True
    print(sol.areAnagrams("triangle", "integral")) # True
    print(sol.areAnagrams("apple", "pale"))        # False
