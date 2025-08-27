'''You are given a string .
contains alphanumeric characters only.

Your task is to sort the string  in the following manner:
1.All sorted lowercase letters are ahead of uppercase letters.
2.All sorted uppercase letters are ahead of digits.
3.All sorted odd digits are ahead of sorted even digits.

Input Format:
A single line of input contains the string .

Output Format:
Output the sorted string .

Sample Input:
Sorting1234

Sample Output:
ginortS1324
'''


a = input("Enter a alphanumeric string : ")
b = ""
c = ""
d = ""
for i in a:
    if i.islower():
        b += i
    elif i.isupper():
        c += i
    else:
        d += i
h = "".join(sorted(b))
g = "".join(sorted(c))
e = ""
f = ""
for i in d:
    if int(i)%2==0:
        e += str(i)
    else:
        f += str(i)
k = "".join(sorted(e))
l = "".join(sorted(f))
m = h+g+l+k
#n = ",".join(m)
print(str(m))    
