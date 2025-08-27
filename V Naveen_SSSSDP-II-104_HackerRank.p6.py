'''
We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).

Sample Input:
STDIN           Function
-----           --------
abracadabra     s = 'abracadabra'
5 k             position = 5, character = 'k'

Sample Output:
abrackdabra
'''




def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]
if __name__ == '__main__':
    s = input("Enter a string : ")
    i, c = input("Enter position and character to be replaced : ").split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)