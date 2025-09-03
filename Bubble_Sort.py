# Bubble Sorting

'''
The program takes the size of the array and the elements as input.
It uses Bubble Sort algorithm to compare and swap adjacent elements.
The process is repeated until the array is sorted in ascending order.
Finally, the program prints the sorted array.
'''

def bubble_sort(arr,n):
  for i in range(n-1):
    for j in range(n-i-1):
      if arr[j]>arr[j+1]:
        arr[j],arr[j+1]=arr[j+1],arr[j]
  return arr

n=int(input('Enter the Size of the array:'))
arr=list(map(int,input().split()))[:n]
print(bubble_sort(arr,n))

'''
Output:

Enter the Size of the array:5
10 2 0 5 1
[0, 1, 2, 5, 10]
'''