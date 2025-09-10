'''
Insertion sorting

The program reads the size and elements of an array from the user.
It sorts the array using the insertion sort algorithm, which builds the sorted array one element at a time.
For each element, it shifts larger elements to the right until the correct place for the current element (key) is found.
Finally, it prints the array in ascending order.
'''

def insert_sort(arr,n):
  for i in range(n):
    key=arr[i]
    j=i-1
    while j>=0 and arr[j]>key:
      arr[j+1]=arr[j]
      j-=1
    arr[j+1]=key
  return arr

n=int(input('Enter the Size of the array:'))
arr=list(map(int,input().split()))[:n]
print(insert_sort(arr,n))


'''
Output:

Enter the Size of the array:5
10 2 0 5 1
[0, 1, 2, 5, 10]

'''