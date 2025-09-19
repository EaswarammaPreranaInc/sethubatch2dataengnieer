cubes = [x**3 for x in [2,4,6,8,10]]
print(cubes)   # [8, 64, 216, 512, 1000]




a = ['hyd' , 'pune' , 'chennai' , 'vijayawada']
b = []
for s in a:
    b.append(s[0].upper())
print(b)   # ['H', 'P', 'C', 'V']




a = ['hyd' , 'pune' , 'chennai' , 'vijayawada']
b = [s[0].upper() for s in a]
print(b)   # ['H', 'P', 'C', 'V']




s = "Students are getting bored"
words = s.split()
res = []
for w in words:
    res.append([w.upper(), len(w)])
print(res)   # [['STUDENTS', 8], ['ARE', 3], ['GETTING', 7], ['BORED', 5]]




# append word and its length with comprehension
s = "hyd is green city"
words = s.split()
res = [[w.upper(), len(w)] for w in words]
print(res)   # [['HYD', 3], ['IS', 2], ['GREEN', 5], ['CITY', 4]]




a = [10,20,30,40,50,60,70]
b = [100,200,300,400]
res = []
for i in range(len(b)):
    res.append(a[i] + b[i])
print(res)   # [110, 220, 330, 440]




a = [10,20,30,40,50,60,70]
b = [100,200,300,400]
res = [a[i] + b[i] for i in range(len(b))]
print(res)   # [110, 220, 330, 440]




rows, cols = 3, 4
res = []
for _ in range(rows):
    res.append([0]*cols)
print(res)   # [[0,0,0,0],[0,0,0,0],[0,0,0,0]]




rows, cols = 3, 4
res = [[0]*cols for _ in range(rows)]
print(res)   # [[0,0,0,0],[0,0,0,0],[0,0,0,0]]




a = [10,20,15,18,25,32]
b = [30,40,10,25,15]
res = []
for x in a:
    if x not in b:
        res.append(x)
print(res)   # [20, 18, 32]




a = [10,20,15,18,25,32]
b = [30,40,10,25,15]
res = [x for x in a if x not in b]
print(res)   # [20, 18, 32]




res = [x for x in range(1,21) if x%2==0]
print(res)   # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]




res = [x for x in range(2,21,2)]
print(res)   # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]




res = [x**2 for x in range(1,21) if (x**2)%2==0]
print(res)   # [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]




res = [(x**2) for x in range(2,21,2)]
print(res)   # [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]




a = [10,20,15]
b = [30,40,35,32]
res = []
for x in a:
    for y in b:
        res.append(x+y)
print(res)   # [40, 50, 45, 42, 50, 60, 55, 52, 45, 55, 50, 47]




a = [10,20,15]
b = [30,40,35,32]
res = [x+y for x in a for y in b]
print(res)   # [40, 50, 45, 42, 50, 60, 55, 52, 45, 55, 50, 47]




s1 = "HYD"
s2 = "PUNE"
res = [x+y for x in s1 for y in s2]
print(res)   # ['HP','HU','HN','HE','YP','YU','YN','YE','DP','DU','DN','DE']




a = [[10,20],[30,40,50],[60,70,80,90]]
res = []
for lst in a:
    for val in lst:
        res.append(val)
print(res)   # [10,20,30,40,50,60,70,80,90]




a = [[10,20],[30,40,50],[60,70,80,90]]
res = [val for lst in a for val in lst]
print(res)   # [10,20,30,40,50,60,70,80,90]




a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x  for  x  in  a  for  y  in  x]
print(b)   # [10, 20, 30, 40, 50, 60, 70, 80, 90]




a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]
print(a)   # [[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]




names = ['Swathi' , 'Anand' , 'Srinivas' , 'Zebra' , 'King' , 'Amar']
res = []
for ch in {n[0] for n in names}:
    d = [n for n in names if n[0]==ch]
    res.append(d)
print(res)   # [['Swathi','Srinivas'], ['Anand','Amar'], ['Zebra'], ['King']]




a = [10,20,30,40,50]
b = [5,12,20,37]
i=j=0
c = []
while i<len(a) and j<len(b):
    if a[i]<=b[j]:
        c.append(a[i]); i+=1
    else:
        c.append(b[j]); j+=1
c.extend(a[i:])
c.extend(b[j:])
print(c)   # [5,10,12,20,20,30,37,40,50]




a = [10,20,30,25,40,35,12,5]
n = 3
res = sorted(a, reverse=True)[n-1]
print(res)   # 30




a = [10,20,30,25,40,35,12,5]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print(a)   # [5,10,12,20,25,30,35,40]
