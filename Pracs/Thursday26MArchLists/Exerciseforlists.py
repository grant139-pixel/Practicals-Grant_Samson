#Created by Grant Samson
#I am going to create a python program that asks a user  to enter the number of students in their class
#I will use a looop to ask the user to enter
#Student name and surname for each student
#it will thn print the ist of students using a list

#Greets and thanwill ask them for the amount of students
print("Hello dear students please enter the amount of students in your class")
Amount=int(input(" Hello!,Enter number of students: "))

#empty list of students
studentlist=[]

#range of code

for x in range(0,Amount):
    name=input("Enter student name: ")
    Surname=input("Enter student Surname: ")
    full_name=name+" "+Surname
    studentlist.append(full_name)

#this will display the stuff specified in the range

for x in studentlist:
    print(x)

for x in range(0,5):
    full_name= input("Enter full name of student: ")
    studentlist.append(full_name)












