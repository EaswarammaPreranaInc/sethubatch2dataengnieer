'''
    Problem Statement: Given an array of prices where prices[i] is the price of a given stock on the ith day, 
    find the maximum profit you can achieve by making at most one transaction (i.e., buy one and sell one share of the stock).
    Note that you cannot sell a stock before you buy one.
    Link: https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/buy-stock-2
    Difficulty: Easy
    Category: Arrays
'''

class Solution:
    def maximumProfit(self, prices):
        # code here
        if len(prices)==0 or len(prices)<2:
            return 0
        
        max_profit = 0
        min_price = prices[0]
        n = len(prices)
        
        for i in range(1,n):
            profit = prices[i]-min_price
            max_profit = max(max_profit,profit)
            
            min_price = min(min_price,prices[i])
            
        return max_profit
        