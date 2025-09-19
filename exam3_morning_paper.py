#Unit matrix
def unit():
  for i in matrix:
    if matrix[0][0]==1 and matrix[1][1]==1 and matrix[2][2]==1:
       return True
    elif matrix[0][1]!=0 and matrix[0][2]!=0:
       return False  
  
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
l=unit()
if l== True:
  print("unit matrix")
else:
  print("not a unit matrix")



# function returning first string that repeated max number of times 
def frequent_word(s):
    words=s.replace(".","").split()
    fword=words[0]
    count=0
    for w in words:
        if w==fword:
           count += 1
    return fword,count
s=input("enter a sentence:")
word,c=frequent_word(s)
print(word)
print(c)


#recursion function to count occ of a value in a list
def occ(l,value,i=0):
   if i==len(l):
      return False
   if l[i]==value:
      return True
   return occ(l,val,i+1)


l=eval(input("enter number of elements: "))
val=int(input("enter value to search: "))
if occ(l,val):
   print("true")
else:
   print("false")
enter number of elements: [1,2,3]
enter value to search: 2
true

enter number of elements: [1,2,3,6,7]
enter value to search: 8
false


# printing number pattern
n=int(input("enter number of rows:"))
for i in range(1,n+1):
   print(" "*(n-i),end="")
   for j in range(i,0,-1):
      print(j,end="")
  # for j in range(2,i+1):
     # print(j,end="")
   print()

enter number of rows:5
    1
   212
  32123
 4321234
543212345

#couting frequency of each unique character
def count(s):
  char=sorted(set(s))
  res=[]

  for ch in char:
    if ch!=" ":
       res.append(f"{ch}...{s.count(ch)}")
  print(",".join(res))

s=input("enter string:")
count(s.upper())


enter string:rama rao
A...3,M...1,O...1,R...2




