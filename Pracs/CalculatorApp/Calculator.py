#created by Grant Samson
#This is a program that greets the user
#and asks them for 2 random number
#then proceeds to do basic arithemetic operations on the two numbers

print=("Hello Nerd")

#Asksing the user for two numbers

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

#Calculations of the two numbers

Subtaction_Result=input(num1-num2)
Addition_Result=input(num1+num2)
Division_Result=input(num1/num2)
Modulus_Result=input(num1%num2)
Multiplication_Result=input(num1*num2)

#Printing the results of the calculations
print("Subtraction Result: ", Subtaction_Result)
print("Addition Result: ", Addition_Result)
print("Division Result: ", Division_Result)
print("Modulus Result: ", Modulus_Result)
print("Multiplication Result: ", Multiplication_Result)

