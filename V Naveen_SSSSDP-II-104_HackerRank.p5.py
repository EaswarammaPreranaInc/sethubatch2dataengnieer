'''
Sample Input:
this is a string 

Sample Output:
this-is-a-string
'''


def split_and_join(line):
    return '-'.join(line)
if __name__ == '__main__':
    line = input("Enter a string : ").split()
    result = split_and_join(line)
    print(result)
