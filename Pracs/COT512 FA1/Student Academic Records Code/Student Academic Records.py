#Created by Grant Samson First Year OCC: Software Developer
#The system that i have been assigned to create,
#should store information for mutliple students and also be able to calculate the students marks,
#furthermore the system should be able to all the teacher to input more then 1 stsudent marks for all 4 terms of the school year.
#It should also print and allow the input of the grade in which the stueent is enrolled in


All_student=[] #this will hold all the student records for all the students on the system
All_grades=[] #this will hold all the student grades for all the students on the system
All_marks=[] #this will hold all the student marks for all the students on the system

#Below is the menu that the user of the system will see when the code starts running while the choice chosen remains true 
#for the chosen option (1,2,3 and will end whenever 0 is chosen bringing the loop to a close)
def main():
    while True: #keeps the main function working until the user chooses ti exit the system
        #The following below is the menu that is displayed for the user to enter and choose specific opertions before continuing to use the system
        #With only 4 options being granted for the user to be able to use
        print("Welcome to School calculator")
        print("1. Add student")
        print("2. Display student marks")
        print("3. Calculate student averages")
        print()
        print("0. Close")

        try:
            choice=input("What would you like to do?: ").strip()
        except ValueError: #Ends the code when anything but an integer is entered to the options provided
            print("Invalid Choice")
            continue

        #an if statement that runs through the loop for what should be entered when the choice is equal to a specific choice chosen
        #The first choice adds students to the system
        if choice == "1":
            #Application prompts the user on how many students should be added.
	        #The application prompts the user to add a student name
	        #The application prompts the user to enter a student grade
	        #The application prompts the user to enter 4 marks (I mark per term)
	        #The application does this for the number of students to be added.
	        #Information entered should be stored in a list or dictionary

            num_students=0 #keeps asking the user to enter a number until a number greater than 0 is entered
            while num_students <= 0:
                try:
                    num_students = int(input("Enter number of students: "))#asks for the number of students that the user would like to be entered into the system
                    if num_students <= 0:
                        print("Please enter a number greate then 0")
                except ValueError:
                    print("Please enter a whole number!")
            for i in range(num_students):
                #this gets the students names and grades and stores them in the lists that have been appended below
                name_ofstudent =input("Enter Student Name: ")
                while True:
                    try:
                        grade_ofstudent =int(input("Enter Student Grade (8-12): "))# asks the user to enter a students grae between the grades 8 and 12 and it is converted into an interger meaning strings wont be accepted 
                        if 8 <= grade_ofstudent <=12:# checks if grade is within given range
                            break #exits the loop is the number/grade entered isnt a grade between 8 and 12 
                        else:
                            print("Please enter a grade between 8 and 12")
                    except ValueError:
                        print("Please enter a number!")
                All_student.append(name_ofstudent) #all the students that are added into the system are stored into this list which reads all the names entered into the system
                All_grades.append(grade_ofstudent) #all the grades that are added into the system are stored into this list which reads all the grades entered into the system

                student_marks=[]#temporary list to hold all the students marks which are then permeaty stored in the all_marks list once the user ha enetered all the information
                for term in range(1,5): #a loop to loop 4 times for therms 1 till 4
                    while True:
                        try:
                            mark=int(input(f"Enter mark for Term {term}: ")) #Asks the user to please enter a term mark for each term
                            if 0 <= mark <=100: #a restriction that prevents users from entering numbers smaller than 0 or greater then 100, if so it returns an error until an accurate number in the specified range is given by the user 
                                student_marks.append(mark) #adds the entered marks temporarily into student_marks which then lists all the marks in All_marks
                                break
                            else:
                                print("Invalid Input please enter a mark between 0 and 100!")
                        except ValueError:
                            print("Please enter a number!")# if anything but a string is entered instead of an integer the following error is returned
                All_marks.append(student_marks) #adds all the marks into 1 entry under the all_marks students after they have been stored temporarily in the students_marks

            
        elif choice == "2":
            print("Display student marks")

            for i in range (len(All_student)): #loops through all the students entered in the sytem, the len value helps with determing how many students were entered by reading the amount of names added in the list of students
                #after all of this it prints all the necessariy information about that student which is their grade, name and their marks for all 4 terms
                print("\nStudent Name: ")
                print("============")
                print(All_student[i])

                print("\nStudent Grade: ")
                print("============")
                print(All_grades[i])

                print("\nStudent Marks: ")
                print("============")
                for term in range(4): #loops 4 times to show all 4 marks in the 4 terms
                    print(f"Term {term +1}: {All_marks[i][term]}%") #prints the term1-4 and the mark for each term and student respectfully
                


        elif choice == "3":
            if len(All_grades) == 0: #checks if there are any students on records and marks before it starts calculating the avergaes
                print("No students on Record!")
            else:
                print("Calculating Averages")
                print("\nAverage Marks: ")
                print("============")
                
                for i in range(len(All_student)): #determines the amount of students entered in the system then loops through them and begins to calculate all their averages 
                    total=0
                    for t in range(4): #loops through all 4 terms for each student
                        total += All_marks[i][t] #adds each term mark to the total of the pervious terms and has a final total of all the marks combinded for that student for those 4 terms
                    average= total / 4 #devides the total of the 4 terms of the students marks by 4 giving us the average across all the terms
                    print(f"Student name: {All_student[i]:<15} Average: {average:.2f}") #prints the students name and their average to the second decimal place
                

        elif choice == "0":
            print("Exiting Students Academic Records System!")
            break #exits the while loop when the choice chosen is 0 meaning the user does not wish t continue adding any information into the system
        else: 
            print("Invalid choice: Choose again from the list provided in the menu either 1, 2, 3 or 0") #what is shown to the user when they enter an option not provided in the menu
main() #calls for the main function def main(): to start and run the program

