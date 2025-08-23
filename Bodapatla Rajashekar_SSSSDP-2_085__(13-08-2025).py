st=input("enter the string:")
st1=''
for i in st:
    if i in "aeiouAEIOU":
        st1=st1+i
print(st1)        
