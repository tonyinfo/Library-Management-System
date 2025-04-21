import datetime


# global books

# Create a list of books, 
# where each book is represented by books.
books = [ ["Victory", "Rev. Tony", 1001], ["Migration", "Rev. Ekperechi", 1002], ["The Word", "Rev. Ndubuisi", 1003]]

# Create a list of subscribers, 
# where each subscriber is represented by subscribers.
subscribers = [ ["John Doe", "Church Hall London", 101], ["Mark Maxwell", "Carnbrook Rd, London", 102], ["Backs Monks", "Jane Square, Greenwich", 103], ["Mike Wong", "Mongo Park", 1004 ]]

# ---------------------------------------------------
# Define the main function for managing the books
def manageBooks():

    print(""" 

  ------------------------------------------------------
 |======================================================| 
 |======== Welcome To Library Management System	========|
 |======================================================|
  ------------------------------------------------------
#User Options
Enter 1 : Display books
Enter 2 : Display subscribers
Enter 3 : Add books
Enter 4 : Add subscribers
Enter 5 : Search books
Enter 6 : Add borrower
Enter 7 : Remove books
Enter 8 : Returned books

		""")

    
    try:
        userInput = int(input("Please choose an option: "))
    except ValueError:
        exit("\nPlease enter a number to choose.")

    #Display books
    if (userInput == 1):
        print("List Books\n")
        # ---------------------------------------------------
        # -------- Print the details of all books --------
        for book in books:
            print(f"=> {book}")
    
    #Display subscribers
    if (userInput == 2):
        print("List Subscribers\n")
        # ---------------------------------------------------
        # -------- Print the details of all subscruvers --------
        for subscriber in subscribers:
            print(f"=> {subscriber}")
            
    
    #Add new books
    elif (userInput == 3):
        # ---------------------------------------------------
        # ---------- Get the details of the books --------
        # Receive the Name of the new book.
        newBookName = input("Enter New Book: ")
        
        #Receive the name of the new author
        newAuthorName = input("Enter New Author: ")
        
        # Receive the ID number of the new book
        newISBN = int(input("Enter New ISBN: "))
     
        newBook = [newBookName, newAuthorName, newISBN]
                # ---------------------------------------------------
        # --------- Add the book to the records ----------
        # Check if new book already exists
        if (newBook in books):
            print(f"\nThis Book {newBook} Already In The Database.")  # Error Message
        else:
            # Add the new book to the book database (i.e., books)
            books.append(newBook)
            print(f"\n=> New book {newBook} Successfully Added \n")
            for book in books:
                print(f"=> {book}")
                
    #Register new subscribers           
    elif (userInput == 4):
        # ---------------------------------------------------
        # ---------- Get the details of the subscriber --------
        # Receive the Name of the new subscriber.
        newSubscriber = input("Enter New Subscriber: ")
        
        # Receive the ID number of the new subscriber
        newID = int(input("Enter New ID: "))
        
        #Receive the name of the new address
        address = input("Enter New Address: ")
        
        #Define new registered users
        subscriber = [newSubscriber, address, newID]
                # ---------------------------------------------------
        # --------- Add the user to the records ----------
        # Check if new user already exists
        if (subscriber in subscribers):
            print(f"\nThis Subscriber {subscriber} Already In The Database.")  # Error Message
        else:
            # Add the new suscriber to the database (i.e., subscribers)
            subscribers.append(subscriber)
            print(f"\n=> New subscriber {subscriber} Successfully Added \n")
            for subscriber in subscribers:
                print(f"=> {subscriber}")
                
                
    #Search books
    elif (userInput == 5):
        # ---------------------------------------------------
        # ---------- Get the details of the books --------
        # Receive the Name of the book to Search.
        srcBookName = str(input("Enter Book Name To Search: "))
        
        #Receive the Name of the author to search
        srcAuthorName = str(input("Enter Author Name To Search: "))
        
        # Receive the ID number of the the book to Search.
        srcISBN = int(input("Enter ISBN of book to Search: "))
        
        #Create a list to represent the the book to remove
        srcBook = [srcBookName, srcAuthorName, srcISBN]

        # ---------------------------------------------------
        # ------------- Search for the book --------------
        if (srcBook in books):
            print(f"\n=> Book found {srcBook}.")
        else:
            print(f"\n=> No Record Found Of such Book {srcBook}.")  # Error Message
    
    #Borrow books
    elif (userInput == 6):
        #Receive the name of the borrower
        borrower = input("Enter Name of Borrower: ")
        
        #Receive the name of the book to borrow
        bookName = input("Enter Name of Book Borrowed: ")
        
        #Receive the number of the book to borrow
        bookISBN = int(input("Enter ISBN of Book: "))
        
        #Receive the date of lending the book
        #today=lentDate 
        #today=datetime.date.today()
        
        #Receive the return date of the book
        dueDate = input("Enter Return Date: ")
        
        #Create a name of the book to borrow
        borrowBook = [borrower, bookName, bookISBN, dueDate]
        
        #Lent the book
        if (borrowBook in books):
            books.remove(borrowBook)
            print(f"\n=> Book {borrowBook} Not found \n.") #Error message     
            
        else:
            print(f"\n=>Book lent to {borrowBook} \n.")
            
            #Show the current date and time
            print(f"\nToday's Date is, {datetime.datetime.now()} ")
            
    #Details of books to remove    
    elif (userInput == 7):
        # ---------------------------------------------------
        # ---------- Get the details of the books --------
        # Receive the Name of the book to remove.
        rmBookName = input("Enter Book Name To Remove: ")
        
        #Receive the author of book to remove
        rmAuthorName = input("Enter Authur Name of Book To Remove: ")

        
        # Receive the ID number of the the book to remove.
        rmISBN = int(input("Enter ISBN of Book To Remove: "))
        
        #Create a list to represent the the books to remove
        rmBook = [rmBookName, rmAuthorName, rmISBN]

        # ---------------------------------------------------
        # ------ Remove the book from the database -------
        if (rmBook in books):
            books.remove(rmBook)
            print(f"\n=> Book {rmBook} Successfully Removed \n.")

        else:
            print(f"\n=> No Record Found of This Book {rmBook}.")  # Error Message

     #Add returned books
    elif (userInput == 8):
        # ---------------------------------------------------
        # Receive the Name of the returned book.
        returnedBookName = input("Enter name of book: ")
        
        #Receive the name of the author of returned book
        returnedBookAuthor = input("Enter name of Author: ")
        
        # Receive the ID number of returned book
        returnedBookISBN = int(input("Enter ISBN: "))
     
        returnedBook = [returnedBookName, returnedBookAuthor, returnedBookISBN]
                # ---------------------------------------------------
        # --------- Add the returned book to the records ----------
        # Check if the returned book already exists
        if (returnedBook in books):
            print(f"\nThis Book {returnedBook} Already In The Database.")  # Error Message
        else:
            # Add the returned book to the book database (i.e., books)
            books.append(returnedBook)
            print(f"\n=> New book {returnedBook} Successfully Added \n")
            for book in books:
                print(f"=> {book}")
           
    
    
    elif (userInput < 1 or userInput > 8):
        print("Please Enter Valid Option")


# Define a function to check if the user wants to continue and direct accordingly.
def runAgain():
    #Ask user if they wish to continue to 
    runAgn = input("\nWant to continue y/n?: ")
    # check if response is 'y' (it will change the response to lowercase first). 
    if (runAgn.lower() == 'y'):
        # Run the application again
        manageBooks()
        # Run the function to find out if the user wants to continue
        runAgain()
    else:
        quit()

# ============================================
# =============== Begin ======================


#Show the current date and time
print(f"\nToday's Date is, {datetime.datetime.now()} ")

# Run the main function for managing books
manageBooks()

# Run the function to find out if the use wants to continue
runAgain()
