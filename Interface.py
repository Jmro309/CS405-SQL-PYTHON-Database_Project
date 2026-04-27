import mysql.connector
from mysql.connector import Error

def connect():
    try:
        connection = mysql.connector.connect(                       # Connect to the Database
            host='mysql.cs.uky.edu',                                # Hardcoded for this project
            user='ajgo261',      # your UKY database username
            password='u2681741',  # your UKY database password
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

    cursor.close()
    return clubs  # return the full list of clubs

# ====================================== Make functions for each of the 3 main objectives of the project ====================================== #

def manage_clubs(connection):               # 1. Manage clubs and their associated information
    while True:
        print("\n=== Manage Clubs ===")
        print("Select a club to manage:\n")

        clubs = list_clubs(connection)

        print(f"{len(clubs) + 1}. Report the total budget of all clubs in a given year")
        print(f"{len(clubs) + 2}. Return\n")

        choice = get_menu_choice(1, len(clubs) + 2)
        if choice == len(clubs) + 2:
            break

        # look up which club they picked (subtract 1 because lists start at 0)
        selected_club = clubs[choice - 1]
        club_name = selected_club[0]
        club_year = selected_club[1]

        manage_single_club(connection, club_name, club_year)

def manage_single_club(connection, club_name, club_year):           # Manages the selected club in manage_clubs
    while True:
        print(f"\n=== {club_name} ({club_year}) ===")
        print("1. Add or delete meetings and events")
        print("2. View all students in this club")
        print("3. View faculty advisor")
        print("4. View all meetings and events")
        print("5. Record annual budget")
        print("6. Record an expense")
        print("7. Report total expenses and remaining budget")
        print("8. Return\n")

        choice = get_menu_choice(1, 8)

        if choice == 1:
            manage_meetings(connection, club_name, club_year)
        elif choice == 2:
            view_students(connection, club_name, club_year)
        elif choice == 3:
            view_advisor(connection, club_name, club_year)
        elif choice == 4:
            view_meetings(connection, club_name, club_year)
        elif choice == 5:
            record_budget(connection, club_name, club_year)
        elif choice == 6:
            record_expense(connection, club_name, club_year)
        elif choice == 7:
            report_budget(connection, club_name, club_year)
        elif choice == 8:
            break

def manage_meetings(connection, club_name, club_year):
    return 0

def view_students(connection, club_name, club_year):
    return 0

def view_advisor(connection, club_name, club_year):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT faculty.facultyID, faculty.name 
        FROM faculty 
        JOIN advisor ON faculty.facultyID = advisor.facultyID
        WHERE advisor.clubName = %s AND advisor.clubYear = %s
    """, (club_name, club_year))
    
    result = cursor.fetchall()
    
    print(f"\n=== Advisor for {club_name} ({club_year}) ===")
    if result:
        for row in result:
            print(f"ID: {row[0]}, Name: {row[1]}")
    else:
        print("No advisor assigned.")
    
    cursor.close()
    input("\nPress Enter to continue...")  # pause so user can read it before menu reappears

def view_meetings(connection, club_name, club_year):
    return 0

def record_budget(connection, club_name, club_year):
    return 0

def record_expense(connection, club_name, club_year):
    return 0

def report_budget(connection, club_name, club_year):
    return 0

def report_budget_all(connection, club_name, club_year):
    return 0

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