from db_conn import DB_CONN
from enter import Verification

class BookCollection:
    def __init__(self) -> None:

        
        return None
    
    def open(self) -> None:

       
       choice = -1
       while choice !=0:
            choice = self.askChoice()

            if choice == 1:
                self.availableBook()
            elif choice == 2:
                self.addBook()
            elif choice == 3:
                self.showBooks()
            elif choice == 4:                
                print("*Note - You have to register if you are using this book swap for the first time.")
                option = int(input("Would you like to login or register?\nIf you want to login then press 1.\nIf you want to register press 2.\nYour choice: "))
                if option == 1:
                    username = input("username: ")
                    password =  input("password: ")
                    obj = Verification(username, password)
                    obj.login_user()
                    self.takeBook()
                elif option == 2:
                    username = input("username: ")
                    password = input("password: ")
                    obj = Verification(username, password)
                    obj.register_user()
                else:
                    print("Please choose the correct option to take the book.")
            elif choice == 0:
                break
            else:
                print("Unknown option.")
            print("")

    def askChoice(self) -> int:
            
            print("Options:")
            print("1) Availabe book")
            print("2) Add book")
            print("3) Show books")
            print("4) Take book")
            print("0) Exit")
            feed = input("Choice: ")
            choice = int(feed)      
            return choice
    def availableBook(self) -> None:
        print("Available books: ")
        books = self.getBooks()
        available_books = [book for book in books if book[3] > 0]
        for book in available_books:
            print(f"Book ID: {book[0]} - Faculty: {book[1]}, Name: {book[2]}, Number: {book[3]}")
        return None



    def addBook(self) -> None:
        cursor = DB_CONN.cursor()
        #sql statemet to insert data
        sql_statement ="INSERT INTO product(faculty, name, number) VALUES(?, ?, ?);"
        record_data = self.createBooks()
        cursor.execute(sql_statement, record_data)
        DB_CONN.commit()
        cursor.close()
        return None
    def showBooks(self) -> None:
        print("Books: ")
        books = self.getBooks()
        for book in books: 

            print(f"Books: {book[0]} - Faculty: {book[1]}, Name: {book[2]}, Number: {book[3]}")
        return None
    def takeBook(self) -> None:
        book_id = int(input("Enter book ID: "))
        books = self.getBooks()
        for book in books:
            if book[0] == book_id:
                if book[3] > 0:
                    cursor = DB_CONN.cursor()
                    sql_statement = "UPDATE product SET number = ? WHERE id = ?"
                    new_number = book[3] - 1
                    cursor.execute(sql_statement, (new_number, book_id))
                    DB_CONN.commit()
                    cursor.close()
                    print(f"You got the book: {book[2]}")
                else:
                    print("Sorry, the book is taken already.\nTake after some time.")
                return None
        print("Book Not found.")    
    def createBooks(self) -> tuple:
        print("Insert book details")
        faculty = input("Faculty: ")
        name = input("Name: ")
        number = int(input("Number: "))

        book_data = (faculty, name, number)
        return book_data
    def getBooks(self) -> list:
        
        cursor = DB_CONN.cursor()
        sql_query = "SELECT * FROM product;"
        cursor.execute(sql_query)
        datas = cursor.fetchall() #fetch all datas
        DB_CONN.commit()
        cursor.close()
        return datas
