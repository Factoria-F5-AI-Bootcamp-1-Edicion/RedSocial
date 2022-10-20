import psycopg2
from psycopg2 import Error
# variable de entorno para contraseñas
from dotenv import load_dotenv
import os
load_dotenv()
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_DDBB = os.environ.get('DB_DDBB')

print(DB_DDBB)

db = psycopg2.connect(user=DB_USER,
                  password=DB_PASS,
                  host=DB_HOST,
                  port=DB_PORT,
                  database=DB_DDBB)

    # Create a cursor to perform database operations 5432
cursor = db.cursor()

    # Print PostgreSQL details
print("PostgreSQL server information")
    #print(db.get_dsn_parameters(), "\n")

#cursor.execute("CREATE TABLE Persons (PersonID int, LastName varchar(25));")
# db.commit()

    # Executing a SQL query
#cursor.execute("SELECT * from coders ;")
#rows = cursor.fetchall()
    # for row in rows:
    #    print(f" ->", row[1] )
    # Fetch result

#print("You are connected \n", rows)

#cursor.close()
#db.close()
print("PostgreSQL db is closed")
