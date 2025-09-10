'''
Selection sorting

The program takes an array of numbers as input from the user and sorts them.
It uses the selection sort algorithm, where in each pass the maximum element is selected and swapped into its correct position.
The comparison inside the loop (if arr[j] > arr[mid]) ensures sorting in descending order.
Finally, the sorted array is printed as the output.
'''

def select_sort(arr,n):
  for i in range(n):
    mid=i
    for j in range(i+1,n):
      if arr[j]>arr[mid]:
        mid=j
      arr[j],arr[mid]=arr[mid],arr[j]
  return arr
n=int(input('Enter the Size of the array:'))
arr=list(map(int,input().split()))[:n]
print(select_sort(arr,n))


'''
Output:

Enter the Size of the array:5
10 2 0 5 1
[0, 1, 2, 5, 10]

'''