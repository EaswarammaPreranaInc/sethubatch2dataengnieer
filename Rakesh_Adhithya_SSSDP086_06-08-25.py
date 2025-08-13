#Unlimited inputs until Ctrl+Z is pressed

try:
    sum = 0
    count = 0
    while(True):
        sum += eval(input('Enter input (ctrl + z to stop):  '))
        count += 1
except EOFError:
    print(f'Average: {sum/count}')