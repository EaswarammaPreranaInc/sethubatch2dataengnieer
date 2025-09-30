'''
Write  a  program to  generate  10  passwords  each  of  6 character  length  where
1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters are digits

U7U2X8
V9I6X8
G4M8S2
M4U3C3
I7K2B8
F0E9Q1
Y8H8L7
K1U5S0
W7G0J3
Y9B9J6

'''
from random import *
for i in range(10):
    p = [None] * 6
    for i in range(0, 5, 2):
        r = randint(65, 90)
        p[i] = chr(r)
    for i in range(1, 6):
        r = randint(0, 9)
        p[i] = str(r)
    print(''.join(p))

'''
Q85633
I57900
G37670
T26680
N67500
F25650
O93146
H20777
X74945
'''