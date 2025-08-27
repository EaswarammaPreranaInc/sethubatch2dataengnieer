'''
A set is an unordered collection of elements without duplicate entries.
When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order.

Sample Input:
STDIN                                       Function
-----                                       --------
10                                          arr[] size N = 10
161 182 161 154 176 170 167 171 170 174     arr = [161, 181, ..., 174]

Sample Output:
169.375

Expalnation:
Here, set is the set containing the distinct heights. 
Using the sum() and len() functions, we can compute the average.
'''


def average(array):
    a = set(arr)
    return sum(a)/len(a)
if __name__ == '__main__':
    n = int(input("Enter a number : "))
    arr = list(map(int, input("Enter elements : ").split()))
    result = average(arr)
    print(result)