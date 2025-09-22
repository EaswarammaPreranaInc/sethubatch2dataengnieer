'''
Question:
Write a recursive program to count how many times a given value occurs in a list of numbers.
The program should take numbers separated by commas as input and a target value to search for.
'''

def recursive(nums, val):
    if not nums:
        return 0
    return (1 if nums[0] == val else 0) + recursive(nums[1:], val)

nums = list(map(int, input("Enter numbers separated by comma (e.g. 1,2,3): ").split(',')))
val = int(input("Enter the target Value : "))
x = recursive(nums, val)
print(f"{val} occurs {x} times")

'''
Output 1:
Input: 1,2,2,3,2
Enter the target Value: 2
2 occurs 3 times

Output 2:
Input: 5,6,5,7,5
Enter the target Value: 5
5 occurs 3 times
'''
