# 1. Producer-Consumer Problem with Queue

import threading
import time
from queue import Queue
from random import randint

def producer(q):
    while True:
        num = randint(1, 100)
        q.put(num)
        print("Producer inserts:", num)
        time.sleep(1)

def consumer(q):
    while True:
        val = q.get()
        print("Consumer removes:", val)
        time.sleep(1)

q = Queue()
t1 = threading.Thread(target=producer, args=(q,))
t2 = threading.Thread(target=consumer, args=(q,))
t1.start()
t2.start()






# 2. Creating a File Using `writelines()` Method

def create(f):
    print('Enter text terminated by ctrl + z')
    lines = []
    try:
        while True:
            line = input()
            lines.append(line + '\n')
    except EOFError:
        pass
    f.writelines(lines)
    print(f'File {f.name} is created')
# End of function

fname = input('Enter filename: ')
f = open(fname, 'w')
create(f)
f.close()





# 3. Print Data of a File (Whole Content)

def disp(f):
    data = f.read()
    print(f'Data of the file {f.name}:')
    print(data)
# End

fname = input('Enter filename: ')
f = open(fname, 'r')
disp(f)
f.close()





# 4. Print File Pagewise (20 Lines per Page) and Pause/Clear Each Page

import os

def disp(f):
    count = 0
    while True:
        line = f.readline()
        if not line:
            break
        print(line, end='')
        count += 1
        if count % 20 == 0:
            os.system('pause')  # Pauses every 20 lines (Windows)
            os.system('cls')    # Clears screen for next 20 lines
# End

fname = input('Enter filename: ')
f = open(fname, 'r')
disp(f)
f.close()
