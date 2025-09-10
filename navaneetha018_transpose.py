'''4.Write a program to determine Transpose of a matrix.
input: 10 20 30 40
       50 60 70 80
       90 100 110 120
o/p:  10 50 90
      20 60 100
      30 70 110
      40 80 120
hint: use nested list'''
try:
      a=[]
      print('Enter matrix until ctrl+z')
      while True:
            line=input()
            row=[]
            for x in line.split():
                  row.append(int(x))
            a.append(row)
except:
      b=[]
      for i in range(len(a[0])):
            c=[]
            for row in a:
                  c.append(row[i])
            b.append(c)
      for row in b:
            print(*row)
            

'''OUTPUT:
10 50 90
20 60 100
30 70 110
40 80 120
'''