'''
The program counts positive, negative, and zero numbers from command-line arguments.
It imports argv from the sys module to access command-line inputs.
Using a for loop over argv[1:] (skipping the script name), each argument is converted to int and classified as:
    Positive → increment pos
    Negative → increment neg
    Zero → increment zero
Finally, the program prints the counts of positive, negative, and zero numbers.
'''

from sys import argv
pos=0
neg=0
zero=0
for x in argv[1:]:
    if int(x) > 0:
        pos+=1
    elif int(x) < 0:
        neg+=1
    else:
        zero+=1
print("Number of +ve values : ",pos)
print("Number of -ve values : ",neg)
print("Number of Zeros : ",zero)

'''
Output:

python script.py 5 -3 0 7 -1 0

Number of +ve values :  2
Number of -ve values :  2
Number of Zeros :  2

'''