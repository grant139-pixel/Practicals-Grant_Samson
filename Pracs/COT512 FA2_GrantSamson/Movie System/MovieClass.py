#Movie rental system created by Grant Samson First year software developer
#student number: 20261224
#OCC SD1
#Facilitator: Mr Newman Dube
#This is the classes file

class Customer:
    #the constructor that runs whenever a new Customer object is created
    #it sets up all the starting information for that customer
    def __init__(self, CustomerName,CustomerEmail,MoviesRented=None,Finesowed=0.0):
        self.__CustomerName= CustomerName #stores the customers name privately
        self.__CustomerEmail= CustomerEmail #stores the customers email privately
        self.__MoviesRented= MoviesRented if MoviesRented is not None else [] #stores the rented movies list, if nothing is passed in it defaults to an empty list
        self.__FinesOwed= Finesowed #stores the fines the customer owes, defaults to 0.0 if nothing is passed in




    #adds a movie to the customers rented list when they rent a movie
    def rentMovie(self, movie):
        self.__MoviesRented.append(movie)
        
    #removes a movie from the customers rented list when they return it
    def returnMovie(self, movie):
        self.__MoviesRented.remove(movie)
        
    #process the fine payments for the customers
    def payFine(self, amount):
        #return self.__returnMovie
        if amount >= self.__FinesOwed: #if the payment covers the full fine or more, the balance is cleared
            self.__FinesOwed = 0
        else:
            self.__FinesOwed -= amount #if the payment is less than the fine, only reduce the balance by the amount paid
 
        return True #returns True to confirm the payment was processed
    
    #adds a fine to the customers outstanding balance
    def addFine(self, amount):
        self.__FinesOwed = self.__FinesOwed + amount #adds the new fine amount on top of whatever the customer already owes

    #returns the customers name   
    def getCustomerName(self):
        return self.__CustomerName #gives access to the private name variable from outside the class
    
    #returns the customers email
    def getCustomerEmail(self):
        return self.__CustomerEmail #gives access to the private email variable from outside the class
    
    #returns the list of movies the customer currently has rented
    def getMoviesRented(self,):
        return self.__MoviesRented #gives access to the private rented movies list from outside the class
    
    #returns the total fines the customer currently owes
    def getFinesowed(self):
        return self.__FinesOwed #gives access to the private fines balance from outside the class

    
        
