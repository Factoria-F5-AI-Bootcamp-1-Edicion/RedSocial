import os

import psycopg2
from psycopg2 import Error

from dotenv import load_dotenv

load_dotenv()

DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_DDBB = os.environ.get('DB_DDBB')


db = psycopg2.connect(user=DB_USER,
                  password=DB_PASS,
                  host=DB_HOST,
                  port=DB_PORT,
                  database=DB_DDBB,
                  connect_timeout=10)

    # Create a cursor to perform database operations
cursor = db.cursor()

    # Print PostgreSQL details
print(f"PostgreSQL server information")
    #print(db.get_dsn_parameters(), "\n")

    #cursor.execute("CREATE TABLE Persons (PersonID int, LastName varchar(25));")
    #db.commit()
    
    # Executing a SQL query
    ##cursor.execute("SELECT * from usuarios ;")
    ##rows = cursor.fetchall()
    ##for row in rows:
    ##    print(f" ->", row[1] )
    # Fetch result
   
print(f"You are connected to {DB_DDBB} \n")
