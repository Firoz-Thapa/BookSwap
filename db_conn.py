# import database driver
import sqlite3
from pathlib import Path


# define path to be universal
DB_FILEPATH = Path().joinpath("./dev.db")
#print(DB_FILEPATH)
#print(DB_FILEPATH.absolute())

#define database connection 
DB_CONN = sqlite3.connect(DB_FILEPATH)

