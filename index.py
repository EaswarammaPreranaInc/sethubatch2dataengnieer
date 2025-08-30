a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'

try:
    index = a.index('is')
    while True:
        print(index)
        index = a.index('is', index + 1)
except ValueError:
    print('End')
