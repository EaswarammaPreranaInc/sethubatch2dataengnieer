'''
    problem : Count the frequency of characters in a string
    Difficulty : Easy
 '''
def freq_char(s):
    f = {}
    for i in s:
        if i in f:
            f[i] += 1
        else:
            f[i] = 1
    return f

s = input('Enter string : ')
result = freq_char(s)
for i,j in result.items():
    print(f'{i} : {j}')
