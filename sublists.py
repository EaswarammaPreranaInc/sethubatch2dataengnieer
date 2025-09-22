'''
Question:
Write a recursive program to generate all sublists (subsets) of a given list of numbers.
The program should take numbers separated by commas as input and print all sublists,
sorted first by length and then lexicographically.
'''

def all_sublists(nums):
    if not nums:
        return [[]]
    
    first = nums[0]
    rest = all_sublists(nums[1:])
    
    new_sublists = []
    for sub in rest:
        new_sublists.append(sub)           
        new_sublists.append([first] + sub) 
    
    return new_sublists

nums = list(map(int, input("Enter numbers separated by comma (e.g. 1,2,3): ").split(',')))
result = all_sublists(nums)

result.sort(key=lambda x: (len(x), x))
print("\nAll sublists are:")
for sub in result:
    print(sub)

'''
Output 1:
Input: 1,2
All sublists are:
[]
[1]
[2]
[1, 2]

Output 2:
Input: 1,2,3
All sublists are:
[]
[1]
[2]
[3]
[1, 2]
[1, 3]
[2, 3]
[1, 2, 3]
'''
