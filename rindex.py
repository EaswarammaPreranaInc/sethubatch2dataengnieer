a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'

try:
    index = a.rindex('is')
    while True:
        print(index)
        index = a.rindex('is', 0, index)
except ValueError:
    print('End')
