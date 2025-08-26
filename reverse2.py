str1=input("Enter the list of String: ")
a=list(str1)
n=len(a)
for i in range(n):
    for j in range(
        n-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
print("Sorted List of Strings: ",''.join(a))


