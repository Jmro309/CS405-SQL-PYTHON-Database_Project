import mysql.connector
from mysql.connector import Error

def connect():
    try:
        connection = mysql.connector.connect(                       # Connect to the Database
            host='mysql.cs.uky.edu',                                # Hardcoded for this project
            user='username',      # your UKY database username
            password='password',  # your UKY database password
            database='ajgo261'   # your assigned database name
        )
        if connection.is_connected():
            print("Connected to database successfully!")
            return connection
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None
    
def get_menu_choice(min, max):                                      # Forces input to only be between the given options
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if min <= choice <= max:
                return choice
            else:
                print(f"Please enter a number between {min} and {max} according to the options.")
        except ValueError:
            print(f"Please enter a number between {min} and {max} according to the options.")

def list_clubs(connection):         # Make a list of the names and years of all clubs
    cursor = connection.cursor()
    cursor.execute("SELECT name, year FROM club ORDER BY year DESC, name")
    clubs = cursor.fetchall()

    for i, club in enumerate(clubs, start=1):
        print(f"{i}. {club[0]} ({club[1]})")
    
    print(f"{i + 1}. Return.\n")

    cursor.close()
    return len(clubs)  # return the count back to whoever called this function

# =================================================== Make functions for each of the 3 main objectives of the project =================================================== #

def manage_clubs(connection):               # 1. Manage clubs and their associated information
    while True:
        print("\n=== Manage Clubs ===\n")

        club_count = list_clubs(connection)

        choice = get_menu_choice(1, club_count + 1)
        if choice == club_count + 1:
            break   # just goes back to main menu

def manage_faculty(connection):             # 2. Manage faculty members who advise clubs
    while True:
        break

def manage_students(connection):            # 3. Manage students and their club memberships
    while True:
        break

# ======================================================================================================================================================================== #

def main():
    connection = connect()
    if connection is None:
        return

    while True:
        print("\n=== Club Management System ===")
        print("1. Manage Clubs")
        print("2. Manage Faculty")
        print("3. Manage Students")
        print("4. Exit")

        choice = get_menu_choice(1, 4)

        if choice == 1:
            manage_clubs(connection)


        elif choice == 2:
            manage_faculty(connection)

        elif choice == 3:
            manage_students(connection)

        elif choice == 4:
            print("Goodbye!")
            connection.close()
            break

main()