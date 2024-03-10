import mysql.connector

cnx = mysql.connector.connect (
        host = "localhost",
        
        user = "root",
        password = "nevergiveup_04",
        database = "envision_db"
    )
def fetch_doctor():
    cursor = cnx.cursor()

    query = ("""SELECT Name from doctors
                WHERE Status = 'Available'
                LIMIT 1;""")
    cursor.execute(query)

    result = cursor.fetchone()

    

    if result is not None:
        return result
    else:
        return None
    
def fetch_nurse():
    cursor = cnx.cursor()

    query = ("""SELECT Nurse_name from nurses
                WHERE Status = 'Available'
                LIMIT 1;""")
    cursor.execute(query)

    result = cursor.fetchone()

    # cnx.close()

    if result is not None:
        return result
    else:
        return None

import mysql.connector

# Define your database connection parameters here
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="nevergiveup_04",
    database="envision_db"
)

def update_doctor_status(doctor_name):
    try:
        cursor = cnx.cursor()

        # SQL query to update the doctor's status to 'Assigned'
        query_update = ("""
        UPDATE doctors
        SET Status = 'Assigned'
        WHERE Name = %s;
        """)

        # Execute the update query with the doctor's name as a parameter
        cursor.execute(query_update, (doctor_name,))

        # Commit the changes to the database
        cnx.commit()

        # cursor.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def update_nurse_status(nurse_name):
    try:
        cursor = cnx.cursor()

        # SQL query to update the nurse's status to 'Assigned'
        query_update =( """
        UPDATE nurses
        SET Status = 'Assigned'
        WHERE Nurse_name = %s;
        """)

        # Execute the update query with the nurse's name as a parameter
        cursor.execute(query_update, (nurse_name,))

        # Commit the changes to the database
        cnx.commit()

        # cursor.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# def complete_nurse(nurse_id):
#     try:
#         cursor = cnx.cursor()

#         query = (""" 
#                     UPDATE nurses
#                     SET Status ='Available
#                     WHERE Emp_id = %s""")
        
#         cursor.execute(query,(nurse_id,))

#         cnx.commit()
#     except mysql.connector.Error as err:
#         print(f"Error: {err}")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")

def complete_doctor(doc_id):
    try:
        cursor = cnx.cursor()

        query = (""" 
                    UPDATE doctors
                    SET Status ='Available
                    WHERE Emp_id = %s""")
        
        cursor.execute(query,(doc_id,))

        cnx.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        

        


