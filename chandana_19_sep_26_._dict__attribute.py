#  What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from  prog1  import  Student
s = Student()
print(s . __dict__) # empty dict
s . get()
print(s . __dict__) # dictionary representation of object s
s . compute()
print(s . __dict__) # dictionary representation of object s
'''
o/p:
{}
Enter roll number : 19
Enter student name :sita
Enter gender:f
Enter marks of 1st subject: 63
Enter marks of 2nd subject: 85
Enter marks of 3rd subject: 71
{'roll_num': 19, 'name': 'sita', 'gender': 'f', 'm1': 63.0, 'm2': 85.0, 'm3': 71.0}
{'roll_num': 19, 'name': 'sita', 'gender': 'f', 'm1': 63.0, 'm2': 85.0, 'm3': 71.0, 'total': 219.0, 'average': 73.0, 'grade': 'Distinction'}   
'''

'''
Repeat  student  program  for  'n'  students

1) import  student  class  defined in  prog9a  but  do  not  rewrite

2) Use  list  of  objects
'''
from prog1 import Student
students=[]
n = int(input("Enter number of students : "))
for i in range(n):
    print(f"\nStudent {i+1}")
    s = Student()
    s.get()
    s.compute()
    students.append(s)

print("\nRoll\tName\tGender\tTotal\tAverage\tGrade")
for s in students:
    s.disp()
'''
o/p:
Enter number of students : 3

Student 1
Enter roll number : 1
Enter student name :ramu
Enter gender:m
enter marks of subject 1 : 56
enter marks of subject 2 : 76
enter marks of subject 3 : 57

Student 2
Enter roll number : 2
Enter student name :jay
Enter gender:m
enter marks of subject 1 : 56
enter marks of subject 2 : 7
enter marks of subject 3 : 89

Student 3
Enter roll number : 3
Enter student name :rishi
Enter gender:m
enter marks of subject 1 : 67
enter marks of subject 2 : 89
enter marks of subject 3 : 76

Roll    Name    Gender  Total   Average Grade
Roll  Number  :   1
Student  Name :   ramu
Gender        :   m
Total  Marks  :   189
Average       :   63.0
Grade         :   First Class
Roll  Number  :   2
Student  Name :   jay
Gender        :   m
Total  Marks  :   152
Average       :   50.666666666666664
Grade         :   fail
Roll  Number  :   3
Student  Name :   rishi
Gender        :   m
Total  Marks  :   232
Average       :   77.33333333333333
Grade         :   Distinction
'''