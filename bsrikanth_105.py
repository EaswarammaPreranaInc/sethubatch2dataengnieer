
#wap to fetch the distinct vowels from the string?

st=input("enter the string:")
st1=''
for i in st:
    if i in "AEIOUaeiou" and i not st1:
        st1=st1+i
print(st1)
