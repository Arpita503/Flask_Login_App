# %pip install mysql-connector-python
# %pip install python-dotenv
import mysql.connector as conn
from dotenv import load_dotenv
import os 

# Load environment variables from the .env file
load_dotenv()

# Fetch the credentials from the environment variables 
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

# Connect to the MySQL server
mydb = conn.connect(
    host=db_host, 
    user=db_user,
    passwd=db_password
)
cursor = mydb.cursor()

# Create and use database
cursor.execute(f'CREATE DATABASE IF NOT EXISTS {db_name}')
cursor.execute(f'USE {db_name}')

# Create table if not exists
cursor.execute('CREATE TABLE IF NOT EXISTS users (name VARCHAR(20), email VARCHAR(20), password VARCHAR(20))')

# Functions

def add_user(name, email, password):
    query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s);"
    cursor.execute(query, (name, email, password))
    mydb.commit()

def find_user(email, password=None):
    if password:
        query = "SELECT * FROM users WHERE email = %s AND password = %s"
        cursor.execute(query, (email, password))
        entry = cursor.fetchall()
        return entry
    
    query = "SELECT * FROM users WHERE email = %s"
    cursor.execute(query, (email,))
    entry = cursor.fetchall()
    return entry
