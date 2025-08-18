try:
    sum = ctr = 0
    while True:
        if (x := eval(input('Enter input (ctrl + z to stop) : '))) is not None:
            sum += x
            ctr += 1
except EOFError:
    try:
        print(f'Average : {sum / ctr}')
    except ZeroDivisionError:
        print('Enter at least one input')
except (NameError, TypeError):
    print('Input cannot be string')
