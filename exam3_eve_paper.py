#couting frequency of each vowel character
def count(s):
  char=sorted(set(s))
  res=[]
  vow="aeiouAEIOU"

  for ch in char:
    if ch!=" " and ch in vow:
       res.append(f"{ch}...{s.count(ch)}")
  print(",".join(res))
s=input("enter string:")
count(s.upper())

enter string:rama rao
A...3,O...1



# printing number pattern
n=int(input("enter number of rows:"))
num=1
for i in range(1,n+1):
   for j in range(i):
        print(num,end=" ")
        num+=2
   print()

enter number of rows:4
1
3 5
7 9 11
13 15 17 19


# sorting each row in matrix
rows=int(input("enter  rows:"))
cols=int(input("enter  cols:"))
matrix=[]
for i in range(rows):
    row=[]
    for j in range(cols):
      val=int(input(f"enter values for row at {i+1} and column at{j+1} :"))
      row.append(val)
    matrix.append(row)
for row in matrix:
  print(row)
for row in matrix:
  row.sort()
print("after sorting")
for row in matrix:
  print(row)

enter  rows:2
enter  cols:2
enter values for row at 1 and column at1 :12
enter values for row at 1 and column at2 :2
enter values for row at 2 and column at1 :32
enter values for row at 2 and column at2 :3
[12, 2]
[32, 3]
after sorting
[2, 12]
[3, 32]


# recursive function for sum of numbers
def sum(a):
   if a==1:
     return 1
   return a+sum(a-1)
   
a=int(input("enter  number: "))
print(sum(a))

enter  number: 100
5050


# function for counting of strings which have last and 1st char same
def num(a):
  count=0
  for i in a:
     if len(a)>0 and i[0]==i[-1]:
        count+=1
  return count
    
a=eval(input("enter list of strings: "))
c=num(a)
print(c)

enter list of strings: ['1221','aab','aba','acb']
2










