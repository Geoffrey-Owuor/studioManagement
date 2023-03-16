#This python file must be run first (and only once)in order to create a table in mysql
#After which you can now insert data
#python module mysql-connector is required
#xampp mysql has been used in this case
import mysql.connector

# Connect to the MySQL database
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password='',
    database="trial_data"
)

# Create a cursor object to execute SQL queries
cursor = cnx.cursor()

# Create the sessions table with a UNIQUE constraint on the date column
create_table_query = """
CREATE TABLE sessions(
  user_id VARCHAR(255) PRIMARY KEY NOT NULL,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  session VARCHAR(255) NOT NULL,
  date DATE NOT NULL,
  UNIQUE (date)
)
"""
try:
    cursor.execute(create_table_query)
    cnx.commit()
    print("Table created succsessfully.")
except mysql.connector.IntegrityError:
    print("There was an error creating the table.")
    cnx.rollback()
    
#THE CODE BELOW IS EXPERIMENTAL

# # Add a task to the tasks table
# add_task_query = "INSERT INTO tasks (user, task, date) VALUES (%s, %s, %s)"
# task_data = ("Alice", "Complete project", "2023-03-10")
# try:
#     cursor.execute(add_task_query, task_data)
#     cnx.commit()
#     print("Task added successfully.")
# except mysql.connector.IntegrityError:
#     print("Sorry, this date is already taken.")
#     cnx.rollback()

# Close the cursor and database connection
cursor.close()
cnx.close()
