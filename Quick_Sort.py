'''
# QUICK SORT

The program takes an array of numbers as input from the user.
It applies the quick sort algorithm, where the first element of the array (or sub-array) is chosen as the pivot.
The part() function rearranges elements so that all smaller (or equal) values go left of the pivot and all larger ones go right.
The algorithm recursively sorts the left and right parts, and finally the sorted array is printed.
'''

def part(arr, low, high):
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        while arr[i] <= pivot and i <= high - 1:
            i += 1
        while arr[j] > pivot and j >= low + 1:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]
    return j

def quick_sort(arr, low, high):
    if low < high:
        p_index = part(arr, low, high)
        quick_sort(arr, low, p_index - 1)
        quick_sort(arr, p_index + 1, high)

n = int(input('Enter the Size of the array: '))
arr = list(map(int, input().split()))[:n]
low = 0
high = n - 1
quick_sort(arr, low, high)
print("Sorted array:", arr)

'''
Output:

Enter the size of the array: 5
10 2 0 5 1
Sorted array: [0, 1, 2, 5, 10]

'''