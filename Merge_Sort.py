'''
Merge Sort

The program takes an array of numbers as input from the user.
It uses the divide and conquer approach by repeatedly splitting the array into two halves until single elements remain.
The merge_join() function merges two sorted halves into a single sorted list.
Finally, the program prints the array in sorted (ascending) order.
'''

def merge_join(left, right):
    a, b = len(left), len(right)
    i, j = 0, 0
    l = []
    while i < a and j < b:
        if left[i] <= right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1
    while i < a:
        l.append(left[i])
        i += 1
    while j < b:
        l.append(right[j])
        j += 1
    return l

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    merge_left = arr[:mid]
    merge_right = arr[mid:]
    left = merge_sort(merge_left)
    right = merge_sort(merge_right)
    return merge_join(left, right)

n = int(input("Enter the size of the array: "))
arr = list(map(int, input().split()))[:n]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)

'''
Output:

Enter the size of the array: 5
10 2 0 5 1
Sorted array: [0, 1, 2, 5, 10]

'''