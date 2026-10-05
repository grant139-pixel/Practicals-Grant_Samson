import re #importing regular expresions to validate emails of the members in the library system


class Book():
    def __init__(self, Title, Author, ISBN, IsAvailable=True):
          self.__title=Title
          self.__author=Author
          self.__isbn=ISBN
          self.__IsAvailable= IsAvailable #The true statement means that the book is still on the shelf, while if its false that means the books been checked out of the system

    def getTitle(self):
        return self.__title

    def getAuthor(self):
        return self.__author

    def getISBN(self):
        return self.__isbn

    def getIsAvailable(self):
        return self.__IsAvailable


    def updateAvailability(self, IsAvailable):
        #this updates wether or not the book is available or not using the True for available and False for it being checked out logic
        self.__IsAvailable= IsAvailable

    def __str__(self):
        status= "Available" if self.__IsAvailable else "Checked Out"
        return f"{self.__title} by {self.__author} (ISBN: {self.__isbn}) - {status}"

          
class Member():
     #the Member class stores all information relateing to registered library member
     def __init__(self, Name, Email, borrowed_books=None):
         self.__name=Name #stores the members name 
         self.__collection_books= borrowed_books if borrowed_books is not None else []  #an empty list that stores all the borrowed books for new members with no borrowed books

         pattern=r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$" #Validates the email address using regular expressions before accepting it into the system
         if not re.match(pattern, Email):
            raise ValueError (f"Invalid email address {Email} please use a valid format")
            print("Invalid email, please try again.")
            Email=input("Please enter an email: ")

         self.__email=Email #stores the members email and only saved all the emails after validation.

     def getName(self):
         return self.__name

     def getEmail(self):
         return self.__email

     def getBorrowedBooks(self):
         return self.__collection_books #returns the list of the ISBNs the member currently has borrowed

     def borrowBook(self, isbn):
         #Adds the ISBN of the checked out book to the members collection list
         self.__collection_books.append(isbn)

     def returnBook(self, isbn):
         #removes the isbn of returned book from the member's collection list
        
        if isbn in self.__collection_books:
            self.__collection_books.remove(isbn)

     def __str__(self):
         return f"{self.__name} ({self.__email}) Borrowed Books: {len(self.__collection_books)}"
         
         




         



        


          
    

