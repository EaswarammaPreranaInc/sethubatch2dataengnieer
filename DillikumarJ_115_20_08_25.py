# l=int(input("enter elements to perform :"))

# l=[2 , 4 , 6 , 8 , 10]
# res=[i**3  for i in l]
# print(res)

# s='hyd'
# res=s.capitalize()
# print(res)

# s='hyd'
# res=s[0].upper() 
# print(res)

# s=['hyd' , 'pune' , 'chennai' , 'vijayawada']
# res=[]
# for i in s :
#    res.append(i[0].upper())
# print(res)

# s=['hyd' , 'pune' , 'chennai' , 'vijayawada']
# res=[i[0].upper() for i in s]
# print(res)

# s=input("enter any string  : ")
# res=[]
# for i in range(len(s)) :
#     c=len(s[i])
#     res.append(c)
# print(list(res,len))
    
#s=input("enter any string  : ")
# word=s.split()
# res=[]
# for  i in word:
#     res.append([i,len(i)])
# print(list(res))

# w=s.split()
# res=[[i , len(i)] for i in s.split()]
# print(res)

# l1=eval(input("enter 1st list "))
# l2=eval(input("enter 2nd list "))
# res=l1+l2
# print(res)

# res = [item for item in eval(input("Enter 1st list: "))] + [item for item in eval(input("Enter 2nd list: "))]
# print(res)

# l1=eval(input("enter 1st list "))
# l2=eval(input("enter 2nd list "))
# res=[]
# for i in l1:
#     if i not in l2:
#         res.append(i)
# print(res)

# res=[]
# for i in range(1,20):
#     if i%2==0:
       
#        res.append(i)
# print("even numbers  are in range of : ",res)

# even_num=[i for i in range(0,20,2) ]
# print(even_num)

# res=[]
# for i in range(1,20):
#     if i%2==0:
       
#        res.append(i)
# c=[x**2 for x in res]
# print("even numbers  are in range of : ",c)

# res = [i**2 for i in range(1, 20) if i % 2 == 0]
# print("Squares of even numbers are:", res)

# l1=eval(input("enter 1st list "))
# l2=eval(input("enter 2nd list "))
# res=[]

# for i in l1:
#     for j in l2:
#         res.append(i+j)
# print(res)

# l1=eval(input("enter 1st list "))
# l2=eval(input("enter 2nd list "))
# res=[i+j for  i in l2 for j in l2]
# print(res)

# l1=input("enter string :")
# l2=input("enter string :")
# res=[]
# for i in l1:
#     for j in l2:
#         res.append(i.capitalize()+j.capitalize())
# print(res)

# l1=eval(input("enter 1st list "))
# res=[]

# for i in l1:
#     for j in i:
#         res.append(j)
# print('resulted list is :',res)

# l1=eval(input("enter 1st list "))
# res=[j for i in l1 for j in i]

# print('resulted list is :',res)

#l1= ['Swathi' , 'Anand' , 'Srinivas' , 'Zebra' , 'King' , 'Amar' ]
# l1=eval(input("enter 1st list "))
# for i in 

# l1=input("enter string :")
# l2=input("enter string :")
# c=[]
# i,j=0,0
# while i<len(a)  and j<len(b):
#     if a[i] < b[j]:
#         c.append(a[i])
#         i+=1
#     else:
#         c.append(b[i])
#         j+=1
# print(c)


# Program to find n-th largest element in a list


# a = eval(input("Enter list:"))
# n = int(input("Enter  largest element :"))
# a.sort(reverse=True)
# print(n, "th  largest  element  :", a[n-1])


a =  eval(input("Enter list:"))
for i in range(len(a)):
    for j in range(0, len(a)-i-1):
        if a[j] > a[j+1]:
          
            a[j], a[j+1] = a[j+1], a[j]

print("Sorted list is :", a)