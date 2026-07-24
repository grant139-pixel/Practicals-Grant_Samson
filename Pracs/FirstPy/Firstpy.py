#Created by Grant Samson
#This is a program that asks the user
#for their first name, surname and current_year than prints 
#a message that says Hello first name , you were 
#bprn in year_of_birth


#Message to user



message="Hello Nerd, Welcome to Python"
print(message)

#Getting input from user
Name=input("Enter your first name: ")
Surname=input("Enter your surname: ")
age=int(input("Enter your age: "))
current_year=int(input("Enter the current year: "))

#Processing-Caclulating the year_of_birth
year_of_birth=current_year-age

#Output- Displaying a message
print("Hello ", Name, " " , Surname , "you were born in " , str(year_of_birth))


