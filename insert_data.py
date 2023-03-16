#!C:/Users/jeff/AppData/Local/Programs/Python/Python311/python
#The line above shows the cgi where to find the python interpreter,the location,
#might be different in another person's case
print("Content-Type: text/html")
print()
import cgi
import mysql.connector

print("<h1>Feedback Hub!!</h1>")
print("</hr>")

# Get the form data
form = cgi.FieldStorage()
user_id = form.getvalue('user_id')
username = form.getvalue('username')
email = form.getvalue('email')
session = form.getvalue('session')
date = form.getvalue('date')

# Connect to the MySQL database
con = mysql.connector.connect(user='root', password='',
                              host='localhost', database='trial_data')
cursor = con.cursor()

# Insert the data into the database
query = "INSERT INTO sessions(user_id, username, email, session, date) VALUES (%s, %s, %s, %s, %s)"
values = (user_id, username, email, session, date)
#Alert the user if the date is already taken
try:
    cursor.execute(query, values)
    con.commit()
    print("<h3>Your session has been recorded successfully</h3>")
except mysql.connector.IntegrityError:
    print("<h3>SORRY, THIS DATE IS ALREADY TAKEN BY ANOTHER ARTIST!!!</h3>")
    con.rollback()

# Close the database connection
cursor.close()
con.close()

print("<a href='http://localhost/studio/index.php'>click here to go back</a>")

