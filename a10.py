'''

Library book and member management program

'''
members = []
books = []
borrowed = {}
ADD_MEMBER = 1
DELETE_MEMBER = 2
ADD_BOOK = 3
DELETE_BOOK = 4
FIND_BORROWER = 5
ISSUE_BOOK = 6
RETURN_BOOK = 7
LIST_MEMBERS = 8
LIST_BOOKS = 9
PRINT_HELP = 10
EXIT = 0

# print menu
print("The commands are:")
print("  ", ADD_MEMBER, "to add a member")
print("  ", DELETE_MEMBER, "to delete a member")
print("  ", ADD_BOOK, "to add a book")
print("  ", DELETE_BOOK, "to delete a book")
print("  ", FIND_BORROWER, "to find out borrower of a book")
print("  ", ISSUE_BOOK, "to issue a book")
print("  ", RETURN_BOOK, "to return a book")
print("  ", LIST_MEMBERS, "to list members")
print("  ", LIST_BOOKS, "to list books")
print("  ", PRINT_HELP, "to print this menu")
print("  ", EXIT, "to quit")

def delete_list_entry(list_name, type_of_entry): # List_name is members, books   type_of_entry --> string book or memeber
   entry = input("Enter " + type_of_entry + " name: ")
   if entry not in list_name:
      print("No " + type_of_entry + " " + entry)
   else:
      list_name.remove(entry)
      print(entry + " deleted from " + type_of_entry + " list " )

def add_list_entry(list_name, type_of_entry):
      entry = input("Enter " + type_of_entry + " name: ")
      if entry not in list_name:
            list_name.append(entry)
            print(entry + " " + "added to: " + type_of_entry)
      else:
           print("Already exists " + type_of_entry + " " + entry) 

def isBorrowed(list_name, type_of_entry):
      entry = input("Enter " + type_of_entry + " name: ")
      if entry not in books:
            print("No book named" + type_of_entry + " " + entry)
      elif entry not in borrowed:
             print(entry, "is not borrowed")
      else:
             print(borrowed[entry])

def is_issued(book_name, member_name):
      book_name = input("Enter name of book: ")
      if book_name not in books:
            print("No book named: " + book_name)
      elif book_name not in borrowed: 
            member_name = input("Enter member name: ")
            if member_name not in members:
               print("No member named", member_name)
            else:
               borrowed[book_name] = member_name
               print(book_name + " issued to :" + member_name)
      else:
            print(book_name, "is already borrowed")

def is_returned(list_name, type_of_entry):
      entry = input("Enter " + type_of_entry + " name: ")
      if entry not in books:
            print("No " + type_of_entry + " named " + entry)
      elif entry not in borrowed:
             print(type_of_entry + " " + entry + " is not borrowed")
      else:
         del borrowed[entry]
         print(entry + " has been returned.")
       
def displayMembers():
        for member in members:
            print(member)
def displayBooks():
        for book in books:
            print(book)

def process():

      command = int(input("Enter a command "))

      while command != EXIT:
         if command == ADD_MEMBER:
               add_list_entry(members, "member")

         elif command == DELETE_MEMBER:     
            delete_list_entry(members, "member") 
         
         elif command == ADD_BOOK:
               add_list_entry(books, "book")
         
         elif command == DELETE_BOOK:    
            delete_list_entry(books, "book") 
         
         elif command == FIND_BORROWER:
               isBorrowed(books, "book")
            
         elif command == ISSUE_BOOK:
               is_issued(books, members)
      
         elif command == RETURN_BOOK:
               is_returned(books, "book")
         
         elif command == LIST_MEMBERS:
               displayMembers()
         
         elif command == LIST_BOOKS:
               displayBooks()

         elif command == PRINT_HELP:
            # print menu
            print("The commands are:")
            print("  ", ADD_MEMBER, "to add a member")
            print("  ", DELETE_MEMBER, "to delete a member")
            print("  ", ADD_BOOK, "to add a book")
            print("  ", DELETE_BOOK, "to delete a book")
            print("  ", FIND_BORROWER, "to find out borrower of a book")
            print("  ", ISSUE_BOOK, "to issue a book")
            print("  ", RETURN_BOOK, "to return a book")
            print("  ", LIST_MEMBERS, "to list members")
            print("  ", LIST_BOOKS, "to list books")
            print("  ", PRINT_HELP, "to print this menu")
            print("  ", EXIT, "to quit")
         command = int(input("Enter a command " + str(PRINT_HELP) + " for help "))

process()
