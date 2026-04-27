from datetime import date
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

def list_faculty(connection):       # Make a list of the names and ID's if all faculty
    cursor = connection.cursor()
    cursor.execute("SELECT name,facultyID FROM faculty ORDER BY name ASC")
    faculty_list = cursor.fetchall()

    if not faculty_list:
        print("No Faculty members found.")
        cursor.close()
        return[]
    

    for i, row in enumerate(faculty_list, start = 1):
        print(f"{i}. {row[0]} (ID: {row[1]})")
    
    cursor.close()
    return faculty_list

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
        print("6. Record a deposit")
        print("7. Record an expense")
        print("8. Report total expenses and remaining budget")
        print("9. Return\n")

        choice = get_menu_choice(1, 9)

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
            record_deposit(connection, club_name, club_year)
        elif choice == 7:
            record_expense(connection, club_name, club_year)
        elif choice == 8:
            report_budget(connection, club_name, club_year)
        elif choice == 9:
            break

def manage_meetings(connection, club_name, club_year):
    while True:
        print(f"\n=== Manage Meetings for {club_name} ({club_year}) ===")
        print("1. Add a meeting")
        print("2. Delete a meeting")
        print("3. Return\n")

        choice = get_menu_choice(1, 3)

        # -------------------------
        # ADD MEETING
        # -------------------------
        if choice == 1:
            cursor = connection.cursor()

            meeting_date = input("Enter meeting date (YYYY-MM-DD): ")
            start_time = input("Enter start time (HH:MM:SS): ")
            classroom = input("Enter classroom: ")
            description = input("Enter description: ")
            duration = int(input("Enter duration (minutes): "))

            try:
                cursor.execute("""
                    INSERT INTO meeting
                    (clubName, clubYear, meetingDate, startTime, classroom, description, duration)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (
                    club_name,
                    club_year,
                    meeting_date,
                    start_time,
                    classroom,
                    description,
                    duration
                ))

                connection.commit()
                print("Meeting added successfully!")

            except Exception as e:
                print(f"Error adding meeting: {e}")

            cursor.close()
            input("\nPress Enter to continue...")

        # -------------------------
        # DELETE MEETING
        # -------------------------
        elif choice == 2:
            cursor = connection.cursor()

            meeting_date = input("Enter meeting date (YYYY-MM-DD): ")
            start_time = input("Enter start time (HH:MM:SS): ")

            try:
                cursor.execute("""
                    DELETE FROM meeting
                    WHERE clubName = %s
                    AND clubYear = %s
                    AND meetingDate = %s
                    AND startTime = %s
                """, (
                    club_name,
                    club_year,
                    meeting_date,
                    start_time
                ))

                connection.commit()

                if cursor.rowcount > 0:
                    print("Meeting deleted successfully!")
                else:
                    print("No matching meeting found.")

            except Exception as e:
                print(f"Error deleting meeting: {e}")

            cursor.close()
            input("\nPress Enter to continue...")

        # -------------------------
        # RETURN
        # -------------------------
        elif choice == 3:
            break

def view_students(connection, club_name, club_year):
    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT s.studentID, s.name
            FROM membership m
            JOIN student s ON m.studentID = s.studentID
            WHERE m.clubName = %s AND m.clubYear = %s
            ORDER BY s.name
        """, (club_name, club_year))

        results = cursor.fetchall()

        print(f"\n=== Students in {club_name} ({club_year}) ===")

        if not results:
            print("No students are currently enrolled in this club.")
        else:
            for student_id, name in results:
                print(f"{student_id} - {name}")

    except Exception as e:
        print(f"Error retrieving students: {e}")

    cursor.close()
    input("\nPress Enter to continue...")

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
    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT meetingDate, startTime, classroom, description, duration
            FROM meeting
            WHERE clubName = %s AND clubYear = %s
            ORDER BY meetingDate, startTime
        """, (club_name, club_year))

        results = cursor.fetchall()

        print(f"\n=== Meetings for {club_name} ({club_year}) ===")

        if not results:
            print("No meetings scheduled for this club.")
        else:
            for meeting_date, start_time, classroom, description, duration in results:
                print(f"\nDate: {meeting_date}")
                print(f"Time: {start_time}")
                print(f"Room: {classroom}")
                print(f"Duration: {duration} minutes")
                print(f"Description: {description}")

    except Exception as e:
        print(f"Error retrieving meetings: {e}")

    cursor.close()
    input("\nPress Enter to continue...")

def record_budget(connection, club_name, club_year):
    cursor = connection.cursor()

    try:
        balance = float(input("Enter budget balance: "))

        cursor.execute("""
            INSERT INTO budget (clubName, clubYear, balance)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE balance = VALUES(balance)
        """, (club_name, club_year, balance))

        connection.commit()
        print(f"Budget set to ${balance:,.2f} for {club_name} ({club_year})")

    except Exception as e:
        print(f"Error recording budget: {e}")

    cursor.close()
    input("\nPress Enter to continue...")

def record_deposit(connection, club_name, club_year):
    cursor = connection.cursor()

    try:
        # -------------------------
        # USER INPUT
        # -------------------------
        transaction_id = input("Enter 9-digit Transaction ID: ")

        # validate format
        if not (transaction_id.isdigit() and len(transaction_id) == 9):
            print("Transaction ID must be exactly 9 digits.")
            cursor.close()
            return

        transaction_date = input("Enter transaction date (YYYY-MM-DD): ")
        description = input("Enter description: ")
        amount = float(input("Enter deposit amount: "))

        # -------------------------
        # CHECK DUPLICATE ID
        # -------------------------
        cursor.execute("""
            SELECT 1 FROM transactions
            WHERE transactionID = %s
            AND clubName = %s
            AND clubYear = %s
        """, (transaction_id, club_name, club_year))

        if cursor.fetchone():
            print("Error: Transaction ID already exists for this club.")
            cursor.close()
            return

        # -------------------------
        # INSERT
        # -------------------------
        cursor.execute("""
            INSERT INTO transactions
            (clubName, clubYear, transactionID, transactionDate, description, amount, transactionType)
            VALUES (%s, %s, %s, %s, %s, %s, 'deposit')
        """, (
            club_name,
            club_year,
            transaction_id,
            transaction_date,
            description,
            amount
        ))

        connection.commit()
        print("Deposit recorded successfully!")

    except Exception as e:
        print(f"Error recording deposit: {e}")

    cursor.close()
    input("\nPress Enter to continue...")
def record_expense(connection, club_name, club_year):
    cursor = connection.cursor()

    try:
        # -------------------------
        # USER INPUT
        # -------------------------
        transaction_id = input("Enter 9-digit Transaction ID: ")

        # validate ID format
        if not (transaction_id.isdigit() and len(transaction_id) == 9):
            print("Transaction ID must be exactly 9 digits.")
            cursor.close()
            return

        transaction_date = input("Enter transaction date (YYYY-MM-DD): ")
        description = input("Enter description: ")
        amount = float(input("Enter expense amount: "))

        if amount <= 0:
            print("Expense amount must be greater than 0.")
            cursor.close()
            return

        # -------------------------
        # CHECK DUPLICATE ID
        # -------------------------
        cursor.execute("""
            SELECT 1 FROM transactions
            WHERE transactionID = %s
            AND clubName = %s
            AND clubYear = %s
        """, (transaction_id, club_name, club_year))

        if cursor.fetchone():
            print("Error: Transaction ID already exists for this club.")
            cursor.close()
            return

        # -------------------------
        # INSERT EXPENSE
        # -------------------------
        cursor.execute("""
            INSERT INTO transactions
            (clubName, clubYear, transactionID, transactionDate, description, amount, transactionType)
            VALUES (%s, %s, %s, %s, %s, %s, 'expense')
        """, (
            club_name,
            club_year,
            transaction_id,
            transaction_date,
            description,
            amount
        ))

        connection.commit()
        print("Expense recorded successfully!")

    except Exception as e:
        print(f"Error recording expense: {e}")

    cursor.close()
    input("\nPress Enter to continue...")

def report_budget(connection, club_name, club_year):
    cursor = connection.cursor()

    try:
        # -------------------------
        # GET BUDGET
        # -------------------------
        cursor.execute("""
            SELECT balance
            FROM budget
            WHERE clubName = %s AND clubYear = %s
        """, (club_name, club_year))

        budget_row = cursor.fetchone()
        budget = budget_row[0] if budget_row else 0

        # -------------------------
        # TOTAL DEPOSITS
        # -------------------------
        cursor.execute("""
            SELECT COALESCE(SUM(amount), 0)
            FROM transactions
            WHERE clubName = %s
            AND clubYear = %s
            AND transactionType = 'deposit'
        """, (club_name, club_year))

        deposits = cursor.fetchone()[0]

        # -------------------------
        # TOTAL EXPENSES
        # -------------------------
        cursor.execute("""
            SELECT COALESCE(SUM(amount), 0)
            FROM transactions
            WHERE clubName = %s
            AND clubYear = %s
            AND transactionType = 'expense'
        """, (club_name, club_year))

        expenses = cursor.fetchone()[0]

        # -------------------------
        # OUTPUT
        # -------------------------
        print(f"\n=== Budget Report for {club_name} ({club_year}) ===")
        print(f"Total Deposits  : ${deposits:,.2f}")
        print(f"Total Expenses  : ${expenses:,.2f}")
        print(f"-----------------------------")
        print(f"Remaining Budget : ${budget:,.2f}")

    except Exception as e:
        print(f"Error generating budget report: {e}")

    cursor.close()
    input("\nPress Enter to continue...")

def manage_faculty(connection):             # 2. Manage faculty members who advise clubs
    while True:
        print(f"\n=== Manage Faculty ===")
        print("Select a Faculty Member to View Advised Clubs")

        faculty = list_faculty(connection)

        print(f"{len(faculty) + 1}. Return\n ")

        choice = get_menu_choice(1, len(faculty) +1 )
        if choice == len(faculty) + 1:
            break;
        
        selected_faculty = faculty[choice - 1]
        faculty_name = selected_faculty[0]
        faculty_ID = selected_faculty[1]

        view_advised_clubs(connection,faculty_ID,faculty_name)


        

def view_advised_clubs(connection, faculty_ID, faculty_name): #Display all of the clubs that a facutly member advises
        cursor = connection.cursor()
        cursor.execute("""
            SELECT clubName,clubYear 
            FROM advisor
            WHERE advisor.facultyID = %s """, (faculty_ID,) )
        
        result = cursor.fetchall()
        
        print(f"\n=== Clubs Advised by {faculty_name} ===")
        if result:
            for row in result:
                print("Club Name: ,{row[0]} ({row[1]})")
        else:
            print("Advises no clubs.")

        cursor.close()
        input("\n Press Enter to continue...")
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