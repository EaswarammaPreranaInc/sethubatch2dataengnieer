home work 06/08/2025
try:
    sum = ctr = 0
    while True:
        if (x := eval(input('Enter input (ctrl + z to stop) : '))) is not EOFError:
            sum += x
            ctr += 1
except EOFError:
    try:
        print(F'Average : {sum / ctr}')
    except ZeroDivisionError:
        print('Enter at least one input')
except (NameError, TypeError):
    print('Input can not be string')
