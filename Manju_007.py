list1=eval(input("enter 1st list"))
list2=eval(input("enter 2nd list"))
result=[]
for i in range(len(list1)):
    result.append(list1[i] + list2[i])
print("list 1 :",list1)
print("list 2 :",list2)

print("sum list:",result)
