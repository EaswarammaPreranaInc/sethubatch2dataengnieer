try:
    n = int(input('Please enter a integer:  '))
    for row in range(1, n+1):
        print( (n-row) * ' ' + (2*row-1)*'*' + (n-row)*' ')
except ValueError:
    print('Please enter only integer value')
