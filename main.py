from db_conn import DB_CONN
from book_collection import BookCollection

#statement in program
LIBRARY_TABLE_STATEMENT = """
CREATE TABLE IF NOT EXISTS product(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    faculty VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    number INTEGER(13) NOT NULL
);
"""
LIBRARY_TABLE_STATEMENT = """
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);
"""
class Main:
    def __init__(self) -> None:
        #initiialize the program
        print("Welcome to online book swap.\nHere you can add the books that is with you.\nAnd also take the books that you need.")

        self.initDatabase()
        menu_product = BookCollection()
        #operate
        menu_product.open()
        #clean up 
        DB_CONN.close()
        print("Thank you for choosing.Visit again")
        return None
    

    def initDatabase(self) -> None:
        #cursor for operating database
        cursor = DB_CONN.cursor()
        #executing sql statement using cursor
        cursor.execute(LIBRARY_TABLE_STATEMENT)
        cursor.execute(LIBRARY_TABLE_STATEMENT)
        #commiting the database transaction
        DB_CONN.commit()
        #close the cursor
        cursor.close()
        return None
    
    

    

if __name__ == "__main__":
    app = Main()    

