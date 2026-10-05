#library system that members of the library can use to check books in and out of the library, while also keeps track of the books that are added to the system or removed or borrowed from the system
#created by Grant samson
#first year OCC Software developer
#Student number: 20261424
#Lecteruer/facilitator: Mr NB Dube

#imports the classes from the classes python file and also imports regex for validation rules when it comes to emails and ISBNs numbers fir books
from Classes import Book
from Classes import Member
import re

#loads books from the books.txt file into a list of books which can be selected by the customer
def load_books():
    books=[] # list where all the books from the txt file will be stored
    try:
        with open("Books.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(",")
                    #only processes the line if it contains all 4 required fields
                    if len(parts) >= 4: 
                        books.append(Book(
                            parts[0].strip(),
                            parts[1].strip(),
                            parts[2].strip(),
                            parts[3].strip().lower() == "true"
                        ))
        print(f"{len(books)} Books loaded!")
    except FileNotFoundError:
        print("Books.txt not found. Starting with no books")
    return books

#loads members from the members.txt file into a list of members that will be displayed when members are added to the system
def load_members():
    members=[] #a list where all loaded Member objects will be stored
    try:
        file=open("Members.txt", "r")
        content=file.read()
        file.close()

        blocks=content.strip().split("\n\n") #splits into individual member blocks divided by blanks lines

        for block in blocks:
            if block.strip() == "":
                continue
            lines= block.strip().split("\n")
            name=lines[0]
            email=lines[1]
            book_count=int(lines[2])

            #reads the ISBNs of borrowed books
            borrowed_books= [] 
            for j in range(book_count):
                borrowed_books.append(lines[3+j]) #reads each ISBN starting from line index 3, since lines 0-2 are name, email, and book count

            members.append(Member(name, email, borrowed_books))

    except Exception:
        #handles missing file or any errors that may arise
        print("Members.txt not found. Starting with no members!")
    return members

#saves all the books into the books.txt file
def save_books(books):
    try:
        with open("Books.txt", "w") as file: #opens the file for writing after all the information has been added to the system and the user has opted to exit the system

            for book in books: #loops through all the books in the list

                # Write all book info on one line separated by commas
                file.write(f"{book.getTitle()},{book.getAuthor()},{book.getISBN()},{book.getIsAvailable()}\n")
            print("Books have been saved")

    except Exception as e:
        print(f"Error saving books: {e}")

    #file.close() #closes the file once all books have been written

#saves all the members to the members.txt file
def save_members(members):
    try:
        file=open("Members.txt", "w") #open the files for writing of the members names

        for member in members: # loops through the list of memebers
            file.write(member.getName()+"\n") #writes the members name
            file.write(member.getEmail()+"\n") #writes the members email
            borrowed=member.getBorrowedBooks()
            if borrowed is None:
                borrowed=[] #an empty list is returned if no boks were borrowed

            file.write(str(len(borrowed))+ "\n") #writes the count of borrowed books
            for isbn in borrowed:
                file.write(isbn + "\n") #writes each borrowed ISBN on its own line
            file.write("\n") #blank line seperates each memeber

        file.close()
        print("Members saved successfully!")
    except Exception as e:
        #cathes any unexpected errors during the writing of information into the file
        print(f"Error: {e}")
#allows you to add books into the library
def addbook(books):
    print("\nAdd Book:")
    print("============")
    title= input("Enter Book Title: ").strip() #asks for the books title when it is going to be added, also the .strip() removes any accidental leading/trailing spaces the user may type
    author=input("Enter Book Author: ").strip() #asks ffor the books author after the title , also the .strip() removes any accidental leading/trailing spaces the user may type
    isbn=input("Enter Book ISBN (10 or 13 digits): ").strip() #asks for thr isbn number of the book once all the other 2 things title and author have been filled in , also the .strip() removes any accidental leading/trailing spaces the user may type

    #validates the isbn numbers using regular expression similar to how we validate the email address using regex
    #removes dashes and spaces 
    isbn_clean=isbn.replace("-", "").replace(" ","")
    if not re.match(r"^\d{10}$|^\d{13}$", isbn_clean):
        print("Invalid ISBN")
        return
    
    # checks for duplicate ISBNs before adding to avoid the same book being added twice
    for book in books:
        if book.getISBN() == isbn_clean:
            print(f"A book with ISBN {isbn_clean} already exists!")
            return

    #creates a new book within the book class when the detailed are entered by the user
    newbook=Book(title, author, isbn_clean)

    #adds the new book to the main books lists so it can show up in the system
    books.append(newbook)

    print(f"Book {title} by {author} added successfully!")

    
#removes a book from the library      
def removebook(books):
    print("\n Remove Book:")
    print("============")
    #checks if there are any books present in the library
    if len(books) == 0:
        print("No Books found")
        return
    #displays all the books so the user can choose which one they would like to remove
    showbooks(books)

    try:
        #allows the user to choose which book they want to remove
        choice=int(input("Select the book you'd like to remove: "))
        #makes sure that the book number selected is within the given range and total amount of books present in the system
        if choice < 1 or choice > len(books):
            print("Invalid book option, try again")
            return

        selected=books[choice - 1]
        #prevent removing books that have been checked out of the system
        if not selected.getIsAvailable():
            print(f"Can't remove {selected.getTitle()} - it has been checked out")
            return 

        removed=books.pop(choice - 1) #removes the books permantely from the list
        print(f"{removed.getTitle()} has been removed from the library.")
    except ValueError:
        print("Invalid input. Please enter a number above")

#Displays all the books in the library with numbering
def showbooks(books):
   #displays a numbered list of all the books including their author, isbn and availability
   print("\nAll Books in Library:")
   print("=================")
   if len(books) == 0:
       print("No books found in library")
       return

   #brings back all the books and displays them as numbered in the books.txt file
   for i in range(len(books)):
       print(str(i + 1) + ". " + str(books[i]))

#allows the user to search for a book or books using either the title of the book or the author who wrote the book
def searchbooks(books):
    #allows the user to search for books by title or author, search is case insensitive and returns all corresponding matches
    print("\nSearch Books in Library:")
    print("==============")

    #checks if there are any books to be looked up to begin with, because you cant search without book in the system
    if len(books) == 0:
        print("No books in library")
        return
    
    #when the user wants to search the library for a book the system asks what they would like to search the books by, wether it be the title or the author name
    print("What would you like to search by")
    print("1. Title")
    print("2. Author")

    try:
        search=int(input("Choose the search type: "))
        if search not in [1, 2]:
            print("Invalid search option")
            return
        #converts the search option to lowercase for case insensitive search just incase the books name or the authors name doesnt start with a capital letter
        search_item=input("Enter search term: ").lower().strip()

        #stores all the books that match the search term inputted by the user
        resultsof_search=[]

        for book in books:
            #if the search option is 1 it will search by title and ask the user to enter the title while including case-insensitivity for all titles
            if search == 1 and search_item in book.getTitle().lower():
                resultsof_search.append(book)
            #does the same thing as option 1 but this time by author name while also maintaning case senitivity
            elif search == 2 and search_item in book.getAuthor().lower():
                resultsof_search.append(book)

        #this checks if there are any authors are books that match the search that the user inutted and returns wether or not the book or author was found or not
        if len(resultsof_search) == 0:
            print(f"No books found matching the following {search_item}")
        else:
            #if there are books found that match the search it is fetched from the list that stores the names that match that name
            print(f"{len(resultsof_search)} book(s) found: ") 
            for i in range(len(resultsof_search)):
                print(str(i+1) + "." + str(resultsof_search[i]))

    except ValueError:
        print("Invalid input. Enter a either 1 or 2")   

#Registers a new member into the library
def addmember(members):
    print("\nAdd a Member:")
    print("==============")
    name=input("Enter Member Name: ").strip()
    email=input("Enter Member Email: ").strip()

    try:
        #the member class already handles email validation with regex
        newmember=Member(name, email)
        #adds the new members information to the main members list
        members.append(newmember)
        print(f"Member {name} registered successfully!")

    except ValueError as e:
        #displays the error message raised by the member class for an individual email
        print(f"Error: {e}")

#removes a member from the library
def remove_member(members):
    print("\nRemove Member:")
    print("==============")

    if len(members) == 0:
        print("No members registered in the system.")
        return

    show_members(members) #displays all the members so the user can choose which member to remove

    try:
        choice=int(input("Select a member to remove: "))
        if choice < 1 or choice > len(members):
            print("Invalid option, choose again.")
            return

        selected_members=members[choice - 1]
        #prevents removing a member who still has books
        if len(selected_members.getBorrowedBooks()) > 0:
            print(f"Can't remove {selected_members.getName()} - they have books checked out!")
            return

        #permanently removes the member from the list
        removed=members.pop(choice -1)
        print(f"Member {removed.getName()} has been removed")

    except ValueError:
        print("Invalid input. Please enter a number")

#displays all the members in the system with numbering    
def show_members(members):
    print("\nAll Registered Members:")
    print("=======================")
    if len(members) == 0:
        print("No members found in the system")
        return

    #prints each member with their number using the Member class's __str__ method
    for i in range(len(members)):
        print(str(i + 1)+"."+str(members[i]))

#checks out a book to a member of the library
def checkoutbooks(books, members):
    """Allows a registered member to borrow an available book.
    Steps:
     1. Checks that members exist (prompts to add one if not).
     2. Filters and displays only available books.
     3. Lets the user pick a book and a member.
     4. Marks the book as unavailable and records the ISBN on the member.
     5. Uses assertions to verify the checkout was completed correctly."""

    print("\nCheckout Book:")
    print("=============")

    #if there are no members, the user is asked to add one before a checkout of any book from the library can happen
    if len(members) == 0:
        print("No members registered. please add a member first!")
        addmember(members) #opts for a member to be added by returning the addmember function 
        return

    #collects only books that are currently available on the shelf
    available_books=[]
    for book in books:
        if book.getIsAvailable():
            available_books.append(book)

    if len(available_books) == 0:
        print("No books are currently available for checkout.")
        return

    #displays only the available books for the selection
    print("Avalable Books:")
    for i in range(len(available_books)):
        print(str(i + 1) + ". " + str(available_books[i]))

    try:
        #book selection happens here
        book_choice = int(input("Select a book to checkout: "))
        if book_choice < 1 or book_choice > len(available_books): #makes sure the number of th book chosen is within the range of books available
            print("Invalid option, choose again.") #if a number of a book greater then the number of listed books is entered this message is returned tp the user
            return

        chosen_book= available_books[book_choice - 1] #gets the actual book that needs to be checked out

        #member selection happens here where u choose which members books would you lke to be returned
        print("\nRegistered Members:")
        for i in range(len(members)):
            print(str(i + 1) + ". " + members[i].getName())

        member_choice = int(input("Select a member: ")) #asks for a number of listed members to be chosen from those members that are available in the system
        if member_choice < 1 or member_choice > len(members): #makes sure the number entered is within the range of the total number of meembers available in the system
            print("Invalid option, choose again.")
            return
        
        chosen_member = members[member_choice -1] #gets the actual member from whom the book will be checked out from

        #assertion confirms the book is still available before completing the checkout
        assert chosen_book.getIsAvailable(), f"{chosen_book} is not available!"

        chosen_book.updateAvailability(False) #marks the book as checked out

        chosen_member.borrowBook(chosen_book.getISBN()) #records the ISBN on the member's account

        #assertions verify the checkout was recorded correctly in both the book and member

        assert not chosen_book.getIsAvailable(), "Error: book availability was not updated!"
        assert chosen_book.getISBN() in chosen_member.getBorrowedBooks(), "Error: book not added to member!"

        print(f"'{chosen_book.getTitle()}' checked out to {chosen_member.getName()} successfully!")

    except AssertionError as e:
        #catches and records any failed assertions and displayed the error message
        print(f"Error: {e}")
    except ValueError:
        print("Invalid input. Please enter a number.")
       
#returns a borrowed book from a member of the library back into the library
def returnbook(books, members):
    """Allows a member to return a book they have borrowed.
    Steps:
     1. Filters members who currently have books checked out.
     2. Lets the user select a member and then which book to return.
     3. Finds the matching Book object using the stored ISBN.
     4. Marks the book as available and removes the ISBN from the member.
     5. Uses assertions to verify the return was completed correctly."""

    print("\nReturn Book:")
    print("=============")
    #if there are no members it will opt th user to create or add a member to the system inorder for it to proceed further
    if len(members) == 0:
        print("No memebers found in system!")
        return

    #collects only those members whom have books checked out
    members_withbooks=[]
    for member in members:
        if len(member.getBorrowedBooks()) > 0:
            members_withbooks.append(member)

        
    if len(members_withbooks) == 0:
        print("No books are currently checked out.")
        return

    #displays members who have books checked out
    print("Members with checked out books:")
    for i in range(len(members_withbooks)):
        count = len(members_withbooks[i].getBorrowedBooks())
        print(str(i + 1) + ". " + members_withbooks[i].getName() + " (" + str(count) + " book(s) checked out)")

    try:
        #allows the user to select a member from the memebers available
        member_choice = int(input("Select a member: "))
        if member_choice < 1 or member_choice > len(members_withbooks): #makes sure the number from the customers selected is within the range if the customers avaliable for selection
            print("Invalid option, choose again")
            return

        chosen_member=members_withbooks[member_choice - 1]

        #finds the actual book that matches the ISBN of the members borrowed book

        #the member stores the usbs only, so we need to find a matching book object
        borrowed_isbn=chosen_member.getBorrowedBooks()
        borrowed_books=[] #stores all the borrowed books that are marked as checkedout in the library system

        for book in books:
            if book.getISBN() in borrowed_isbn:
                borrowed_books.append(book) #after getting the isbn number of the borrowed books, this gets appended into the main books list

        #displayts the specific books this member currently has checked out/ borrowed
        print(f"\nBooks borrowed by {chosen_member.getName()}:")
        for i in range(len(borrowed_books)):
            print(str(i + 1) + ". " + str(borrowed_books[i]))

        #book selection happens where the user can choose which book they would like to return
        bookchoice = int(input("Select the book to return: "))
        if bookchoice < 1 or bookchoice > len(borrowed_books):
            print("Invalid option, choose again.")
            return
        chosen_book = borrowed_books[bookchoice - 1] #retrieves and returns the selected book

        # assertion confirms the book is recorded as checked out before processing the return
        assert not chosen_book.getIsAvailable(), f"'{chosen_book.getTitle()}' is already available!"

        chosen_book.updateAvailability(True)             # marks the book as available again
        chosen_member.returnBook(chosen_book.getISBN())  # removes the ISBN from the member's borrowed list

        # assertions verify the return was recorded correctly in both the book and member
        assert chosen_book.getIsAvailable(), "Error: book not marked available after return!"
        assert chosen_book.getISBN() not in chosen_member.getBorrowedBooks(), "Error: ISBN not removed from member!"

        print(f"'{chosen_book.getTitle()}' returned successfully!")

    except AssertionError as e:
        #displays any assertions errors and displays the message
        print(f"Return Error: {e}")
    except ValueError:
        print("Invalid input. Please enter a number.")

#displays the main menu options for the user
def menu():
    print("1. Add a Book")
    print("2. Add a Member")
    print("3. Remove a Book")
    print("4. Remove a Member")
    print("5. Show Members")
    print("6. Show Books")
    print("7. Search Books")
    print("8. Checkout Books")
    print("9. Return Book")
    print("0. Exit Library")

#The main function that starts the library system.
#Loads existing data from files, then runs a loop that
#repeatedly shows the menu and processes the user's choice
#until they choose to exit.

def main():
    print("WELCOME TO THE LIBRARY")
    #loads all saved books and members from the txt files when the system starts
    books=load_books()
    members=load_members()
    while True: # keeps the system running until the user chooses option 0 to exit
        menu() #displays the menu before every choice
        try:
            choice=int(input("Enter a choice from menu: "))
            if choice == 1:
                addbook(books)
                        
            elif choice == 2:
                addmember(members)
                        
            elif choice == 3:
                removebook(books)
                        
            elif choice == 4:
                remove_member(members)
                        
            elif choice == 5:
                show_members(members)
                        
            elif choice == 6:
                showbooks(books)

            elif choice == 7:
                searchbooks(books)

            elif choice == 8:
                checkoutbooks(books, members)

            elif choice == 9:
                returnbook(books, members)
                        
            elif choice == 0:
                #saves all data back to the files before exiting the system to make sure that data was not lost for user and memebers in the system
                save_books(books)
                save_members(members)
                print("Exiting system")
                break
            else:
                #if a number that isnt in the menu is entered this message will be displayed
                print("Invalid choice. Please select available choices!")
        except ValueError:
            #handles the case where the user types anything that isnt a number
            print("Invalid choice. Please enter a number from the menu above")

if __name__ == "__main__":
    main()
        

