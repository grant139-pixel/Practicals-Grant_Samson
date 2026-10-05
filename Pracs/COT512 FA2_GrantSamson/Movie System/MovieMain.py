#Movie rental system created by Grant Samson First year software developer
#student number: 20261224
#OCC SD1
#Facilitator: Mr Newman Dube

from MovieClass import Customer

  
def loadMovies(): 
    movies={} #a dictionary where the titles will be stored
    try:
        movie=open("Movies.txt", "r")
        for i in movie: # loops through each line to remove blank spaces
            i=i.strip() #removes any extra spaces
            if i != "":#skips blank lines to avoid errors when splittinh
                parts=i.split(",") #this splits the movie lines into a list 
                title=parts[0] #this displays the first part of the title
                copies=int(parts[1]) #this displays the number of copies of the movie
                movies[title]= copies #stores the information read in the dictionary
        movie.close()
        print("Movies Loaded successfully!") # shows the user that movies were loaded wiht no issues
    except Exception:
        print("Movies.txt no found.") #if no movies were found this is returned to the user
    return movies #returns the dictionary after all the informaton has been read and added

def loadCustomers():
    Customers=[] #list that stores all the customers that have been loaded from added customers
    try:
        #opens the customer txt file and rerieves saved customer data by opeining it in read mode
        file=open("Customers.txt", "r")
        content=file.read()#reads the entire whole file
        file.close() #closes the file after reading the file

        blocks=content.strip().split("\n\n") #splits the blocks into single blocks which are divided by blank spaces

        for block in blocks:# loops through each customer block one at a time
            if block.strip() == "":# skips any blocks that are empty or just whitespace
                continue
            lines= block.strip().split("\n")
            name=lines[0] # the first line of the block is the customers name
            email=lines[1]# the second line is the customers email address
            movieCount=int(lines[2]) # the third line is how many movies the customer currently has rented
            rented=[] # creates a temporary empty list to store the rented movies
            for j in range(movieCount): # loops once for each movie the customer has rented
                rented.append(lines[3+ j])# reads each rented movie title from the lines after the count and adds it to the list
            fines= float(lines[3 + movieCount])
            Customers.append(Customer(name, email, rented, fines))# creates a new Customer object with all the loaded data that can be read and added to the list
    except Exception:
        print("Customers.txt not found, Starting with no customers!")
    return Customers

def SaveCustomers(customers):
    file=open("Customers.txt", "w")

    for i in range(len(customers)): #loops through the amount of customers found
        custom=customers[i]# gets the current customer object for easier access

        file.write(custom.getCustomerName()+ "\n") #writes the customers name as the first line of their block
        file.write(","+custom.getCustomerEmail()+ "\n") #writes the customers email on the same line separated by a comma

        movies = custom.getMoviesRented()
        if movies is None:
            movies=[]
        file.write(str(len(movies))+",")
        for movie in movies:
            file.write(movie +",")

        file.write("," + str(custom.getFinesowed())+ "\n")
    file.close()
    print("Customers Saved")


def SaveMovies(movies):
    file=open("Movies.txt","w") #opens the file for writing

    for title in movies:
        copies=movies[title] #gets the number of copies available for this movie
        file.write(title+","+str(copies)+"\n") # writes the title and copy count separated by a comma, then moves to a new line

    file.close()#closes the file once all movies have been written
    print("Movies Saved")

def rentMovie(movies, customers):
    print("\nRent Movies:")
    print("============")
    # If there are no customes the user must first enter customers before renting out movies
    if len(customers) == 0:  #checks if there are any customers
        print("No Customers, Please add a customer!") #if no customers are found this message is displayed
        Add_Customer(customers) #this then allows the user to add customers from the functionadd_customers inorder to allow them to continue using the system
        return



    print("Movies Available:")  #shows the movies avaliable in the system
    movies_available=[] #stores all the avilable movies from movies.txt and shows them to the customer
    for title in movies: #loops through every movie in the dictionary
        if movies[title] > 0: # only shows movies that have at least than 1 copy left
            movies_available.append(title) #adds that available movie to the list of movies from the movie.txt

    if len(movies_available) == 0:
        print("No movies available")
        return

    for i in range(len(movies_available)): #display numbered list of customers for you to pick
        print(str(i +1)+","+movies_available[i]+ "(Copies: "+str(movies[movies_available[i]])+")")

    Moviechoice=int(input("Please choose a movie: ")) #asks the user to chose a movie
    if Moviechoice < 1 or Moviechoice > len(movies_available): #checks that the customers choice of the movie is within the given range which is 25 movies
        print("Invalid option, choose again")
        return
    Moviechosen = movies_available[Moviechoice -1] #gets the actual movie title using the number chosen, minus 1

    print("Customers Avialable: ")
    print("===========")
    for i in range(len(customers)):
        print(str(i +1)+","+customers[i].getCustomerName())

    Customerchoice= int(input("Please select a customer below: "))
    if Customerchoice < 1 or  Customerchoice > len(customers):
        print("Invalid option, choose again")
        return #if input is invalid it exits the system
    Customerchosen= customers[Customerchoice -1] #retrieves the actual Customer object using the entered number

    movies[Moviechosen] = movies[Moviechosen] - 1 #reduces the number of the chosen movies copies by 1
    Customerchosen.rentMovie(Moviechosen) #adds the movie rented to the customers rented list
    print(Moviechosen + " rented to " + Customerchosen.getCustomerName()) #confirms the movie rental of the customer, by displaying their name nd the movie rented


def Add_Customer(customers):
    print("\nADD CUSTOMER:")
    print("=============")
    CustomerName=input("Enter Customer name: ") #asks user for new customer name
    CustomerEmail=input("Enter Customer email:") #asks user for new customer email

    new_customer=Customer(CustomerName,CustomerEmail, []) #creates a new Customer object with the entered details and an empty rented list since they havent rented anything yet
    customers.append(new_customer) #adds the new customer to the main customers list so they appear in the system

    print("Customer "+ CustomerName +" added successfully!")


    
def returnMovie(movies,customers):
    print("Return a Movie")
    print("===============")
    if len(customers) == 0: #checks if there are any customers on the system
        print("No customers found.")
        return

    Hasrentals=[] #empty list to hold only customers who currently have movies rented out
    for i in customers: #loops through every customer to check if they have rentals
        if len(i.getMoviesRented()) > 0: #checks if the customers rented list has at least one movie
            Hasrentals.append(i) #adds the customer to the list if they have active rentals

    if len(Hasrentals) == 0:
        print("No movies have been rented")
        return

    for i in range(len(Hasrentals)):
        rentedList = ", ".join(Hasrentals[i].getMoviesRented()) #joins all rented movie titles into one readable string
        print(str(i + 1) + ". " + Hasrentals[i].getCustomerName() + " Rented: " + rentedList) #displays the customer number, name, and what they have rented

    customer_choice=int(input("\n Select a customer: ")) #asks the user to pick a customer
    if customer_choice <1 or customer_choice > len(Hasrentals): #checks that the selected number is within range
        print("Invalid Option, try again.")
        return
    customer_chosen=Hasrentals[customer_choice -1]

    rentedmovies=customer_chosen.getMoviesRented() #gets the list of movies the chosen customer currently has rented
    print("\n Movies rented by " + customer_chosen.getCustomerName()+":") #heading showing whose movies are being listed
    for i in range(len(rentedmovies)): #loops through the customers rented movies
        print(str(i+1)+"."+ rentedmovies[i])

    movie_choice=int(input("Please select the movie you'd like to return: ")) #asks the user to selet the movie they would like returned from their rented movies
    if movie_choice < 1 or movie_choice > len(rentedmovies): #checks the input is a valid movie number
        print("Invalid Option, choose again")
        return
    movie_chosen=rentedmovies[movie_choice -1] #gets the actual movie title from the rented list
        
    movies[movie_chosen]=movies[movie_chosen]+ 1 #increases the available copy count for that movie by 1 now that its been returned
    customer_chosen.returnMovie(movie_chosen)
    print(movie_chosen + " returned successfully into rental system") #confirms the return was successful becak into the system

    late= input("Is the movie being returned late?(yes/no): ").lower() #asks wheter or not the movie was late or not and if yes the following calcultions below are carried out 
    if late == "yes":
        days=int(input("How many days?: ")) #asks the user to input the amount of days overdue since the movie should have been returned
        fine=days*5 #for everyday late you get charger r5
        customer_chosen.addFine(fine) #adds the calculated fine amount to the customers outstanding fines
        print(customer_chosen.getCustomerName()+ " has been fined R "+ str(fine)) #displays to the user how much the fine is
    else:
        print("Movie not late so not fined")

def Outstanding_rentals(customers):
    print("Outstanding Rentals")
    print("===============")

    if len(customers) == 0: #checks if there are any customers in the system and if not it will ask you to askk customers
        print("No customers found")
        return
    rentals= False

    for i in customers:
        if len(i.getMoviesRented()) > 0:
            rentals= True
            print("\n"+ i.getCustomerName()+ "(" + i.getCustomerEmail()+"):") #prints the customers name and email as a heading
            for movie in i.getMoviesRented():#loops through each movie the customer has rented
                print("-" + movie)
    if not rentals: #checked after the loop, if the flag is still False then nobody has rentals
        print("No movies are currently rented out")
def outstanding_fine(customers):
    print("Outstanding Fines")
    print("============")
    if len(customers) == 0: #checks that there are customers in the system before checking fines
        print("No Customers found.")
        return

    Fines= False #flag to track whether any customers have outstanding fines

    for i in customers:
        if i.getFinesowed() > 0:
            Fines = True #sets the flag to True since at least one customer has a fine
            print(i.getCustomerName() + " owes R "+ str(i.getFinesowed())) #displays the customers name and how much they owe

    if not Fines: #checked after the loop, if the flag is still False then no one owes anything
        print("No outstanding fines.")

def payFines(customers):
    print("Pay Fines")
    print("============")
    customer_fined=[]#creates a new empty list to store only customers who actually owe fines
    for i in customers:
        if i.getFinesowed() > 0:  #checks if the customer owes more than R0
            customer_fined.append(i) #adds them to the list if they have an outstanding fine

    if len(customer_fined) == 0: #if no customers owe anything there is nothing to pay
        print("No Outstanding fines")
        return #exits the system because there are no fines to be paid

    for i in range(len(customers)): #loops through all customers to find those who owe fines
            print(str(i+1)+"."+customers[i].getCustomerName()+" Owes R "+str(customers[i].getFinesowed())) #shows the customer number, name, and their fine amount

    choice=int(input("Select Customer: ")) #asks the user to select a customer from the list of customers provided
    if choice <1 or choice > len(customers):
        print("Invalid option.")
        return
    chose=customers[choice -1] # retrieves the selected Customer object
    amount=float(input("Enter payment amount:"))# asks how much the customer is paying and accepts decimals for cents and then calcukates how much they owe after they have payed the amount
    chose.payFine(amount)
    print("Payment successful. "+ chose.getCustomerName()+ " now owes R " + str(chose.getFinesowed())) #confirms the payment and shows the updated remaining balance

        
def exitSystem(movies, customers):
    SaveMovies(movies) #saves all current movie data to Movies.txt before closing so nothing is lost
    SaveCustomers(customers) #saves all current customer data to Customer.txt before closing
    print("Exiting System. Goodbye!") #this prints after everything has been saved

def menu():
        print("1. Rent Movie")
        print("2. Add Customer" )
        print("3. Return Movie")   
        print("4. View Outstanding Rentals")    
        print("5. View Outstanding Fines")    
        print("6. Pay Fines")   
        print("0. Exit System")
        

def main():
    print("Welcome to the Movie DVD Rental System!")
    movies=loadMovies() #loads all movie data from Movies.txt into a dictionary at startup
    Customers=loadCustomers() #loads all customer data from Customer.txt into a list at startup
    while True:
        menu() #makes sure the menu loops until a valid choice is chosen by the user
        choice=int(input("Enter a choice: ")) #asks the user to choose what they would like to do from the menu provided

        if choice == 1:
            rentMovie(movies, Customers) #returns the function rentmovie when the choice is selected 
        elif choice == 2:
            Add_Customer(Customers) #returns the function add customers when the choice is selected
        elif choice == 3:
            returnMovie(movies, Customers) #returns the function that allows users to return movies when this choice is selected
        elif choice == 4:
            Outstanding_rentals(Customers) #returns all outstanding rentals of movies by customers in the system when this is selected
        elif choice == 5:
            outstanding_fine(Customers)  #returns all the customers names and all theiur outstnding fines when this choice is selected
        elif choice == 6:
            payFines(Customers) #allows the user to pay fines when this is slected and returns the function that allows them to do so
        elif choice == 0:
            exitSystem(movies, Customers) #this is the exit system that once the user is done with all of the above it prompts the program to save all the information into the txts upon the user choosing to close the system.
            break
        else:
            print("Invalid choice. Please select available choices!")
main()
