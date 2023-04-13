from db_conn import DB_CONN

class Verification:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
    LIBRARY_TABLE_MANAGEMENT = """
    CREATE TABEL IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL
    );
    """

    def register_user(self):
        DB_CONN.execute("INSERT INTO users (username, password) VALUES (?, ?)", (self.username, self.password))
        DB_CONN.commit()

    def login_user(self):
        cursor = DB_CONN.execute("SELECT * FROM users WHERE username = ?", (self.username,))
        user = cursor.fetchone()
        if user and user[2] == self.password:
            return True
        else:
            return False
