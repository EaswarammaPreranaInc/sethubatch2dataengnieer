'''
Problem Statement: Given a string S, the task is to check if the characters of the given string can be rearranged to form a palindrome.
Link: https://www.geeksforgeeks.org/problems/anagram-palindrome4720/1?page=1&category=Strings&status=unsolved&sortBy=difficulty
Difficulty: Basic
Category: Strings
'''

#User function Template for python3
class Solution:

    def isPossible(self, s):
        # code here
        count = 0
        freq_dict = {}
        for i in s:
            if i in freq_dict:
                freq_dict[i] += 1
            else:
                freq_dict[i] = 1
        
        for i in freq_dict.values():
            if i%2!=0:
                count+=1
        
        if count>1:
            return 0
        else:
            return 1