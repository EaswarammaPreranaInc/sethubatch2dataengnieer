'''
Question:
Write a recursive program to calculate the sum of a list of numbers.
The program should take numbers separated by commas as input and return their sum.
'''

def recursive_sum(nums):
    if not nums:
        return 0
    return nums[0] + recursive_sum(nums[1:])

nums = list(map(int, input("Enter numbers separated by comma (e.g. 1,2,3): ").split(',')))
x = recursive_sum(nums)
print("Sum of numbers:", x)

'''
Output 1:
Input: 1,2,3,4
Sum of numbers: 10

Output 2:
Input: 5,10,15
Sum of numbers: 30
'''
