'''
Question:
Write a program to generate all permutations of a given list of numbers.
The program should take numbers separated by commas as input and print each permutation as a tuple.
'''

def permute(nums):
    if len(nums) == 0:
        return [[]]  
    result = []
    for i in range(len(nums)):
        rest = nums[:i] + nums[i+1:]  
        for p in permute(rest):
            result.append([nums[i]] + p)
    return result

nums = list(map(int, input("Enter numbers separated by comma (e.g. 1,2,3): ").split(',')))
all_perms = permute(nums)
for p in all_perms:
    print(tuple(p)) 

'''
Output 1:
Input: 1,2,3
(1, 2, 3)
(1, 3, 2)
(2, 1, 3)
(2, 3, 1)
(3, 1, 2)
(3, 2, 1)

Output 2:
Input: 2,3
(2, 3)
(3, 2)
'''
