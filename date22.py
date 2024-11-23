#This is a python terminal only implementation of the project
#This program was created to give an overview of how the project generally works
#datettime package must downloaded using the python pip command incase you don'thave it
from datetime import datetime

# Initialize the sessions dictionary
tasks = {}

def add_task():
    # Ask for the session details
 
    user = input("Please enter your artist username: ")
    task = input("Enter your session activity: ")
    date_str = input("When is your session?(YYYY-MM-DD): ")
    date = datetime.strptime(date_str, "%Y-%m-%d").date()
    
    # Check if the date is already taken
    if date in scheduled_dates:
        print("Sorry, this date is already taken.")
    else:
        # Add the task to the dictionary
        if user in tasks:
            tasks[user].append((task, date))
        else:
            tasks[user] = [(task, date)]
        
        # Add the date to the set of scheduled dates
        scheduled_dates.add(date)
        print("Session has been added successfully.")

def view_tasks():
    # Print the tasks by user
    for user in tasks:
        print(user)
        for task in tasks[user]:
            print("  -", task[0], "set on", task[1].strftime("%Y-%m-%d"))

# Initialize the set of scheduled dates
scheduled_dates = set()

while True:
    # Ask for the action to perform
    action = input("Enter 'add' to add an activity, 'view' to view sessions, or 'exit' to exit: ")
    
    # Perform the action
    if action == "add":
        add_task()
    elif action == "view":
        view_tasks()
    elif action == "exit":
        break
    else:
        print("Invalid action. Please try again.")

# This program asks the user to enter their username, task, and due date.
# It then checks if the date is already taken before adding the task to the tasks dictionary 
# it then schedules the dates set. 
# The view_tasks function simply prints the tasks by user.
