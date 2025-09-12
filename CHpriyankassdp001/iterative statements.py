# iterative statements
""" executing block of statements continues until condition false """
#1. for loop
print("for loop")
print()
#a. using range


i=0
for i in range(100):
    print(i)





#2. using sequence

strip="priya"
for letter in strip:
    print(letter)


hi="welcome"
for i in hi[1:6]:
    print(i)

hey="this is my world"
for j in hey[0:17]:
    print(j,end=" ")
    print()




#while condition statememnts
print("while loop")
x=int(input("enter:"))
i=0
while i<=x:
    print(i)
    i+=1



#nested loops
print("nested loop")
for i in range(0,5):
    for j in range(0,i+1):
        print("*",end=" ")
    print()



for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print(" ")


print("inverted right angle triangle")

for i in range(6,0,-1):
    for j in range(0,i-1,1):
        print("*",end=" ")
    print(" ")