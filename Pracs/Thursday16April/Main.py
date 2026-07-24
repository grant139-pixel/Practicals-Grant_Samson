#Created by Grant Samon 
#This code will calculate the average and give wether the individual has passed or not

#Calculate average function
def calculate_average(mark1,mark2,mark3):
    #TODO: Calcuate and return average
    return (mark1 + mark2 + mark3) / 3

#Grade Function
def get_grade(average):
    # A = 75 and above, B = 60 to 74, C = 50 to 59, F below 50 
    if average >= 75:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "F"

#Pass or Fail Function
def check_pass_fail(average): 
    if average >= 50:
        return "Pass"
    else:
        return "Fail"
    
#Display Results Function
def display_result(name, average, grade, status): 
    print("name: "+name)
    print("average: "+ str(average))
    print("grade: "+grade)
    print("status: "+status)



#Asks user for marks
def main(): 
    num_students = int(input("How many students? ")) 
    for i in range(num_students): 
        print("\nStudent", i + 1) 
        name = input("Enter name: ") 
        mark1 = float(input("Enter mark 1: ")) 
        mark2 = float(input("Enter mark 2: ")) 
        mark3 = float(input("Enter mark 3: ")) 
        
        average = calculate_average(mark1, mark2, mark3)
        grade = get_grade(average) 
        status = check_pass_fail(average)
        display_result(name, average, grade, status)

main()

