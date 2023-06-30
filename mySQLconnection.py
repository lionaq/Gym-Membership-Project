import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="viewer",
    password="12345",
    database="gymplan"
)

cursor = connection.cursor()

# INSERT 
def insertCustomerTable(values):
    #print(values)
    sql = "INSERT INTO customer(CustomerID, Name, Gender, Weight, Height, PlanName, StartDate, EndDate, ContactNo, BirthDate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    #print(values)
    cursor.execute(sql, values)
    connection.commit()

def insertTrainerTable(values):
    #print(values)
    sql = "INSERT INTO trainer(TrainerID, Name, PlanName) VALUES (%s, %s, %s)"
    #print(values)
    cursor.execute(sql, values)
    connection.commit()

def insertPlanTable(values):
    #print(values)
    sql = "INSERT INTO gymmembershipplan(PlanName, Pricing) VALUES (%s, %s)"
    #print(values)
    cursor.execute(sql, values)
    connection.commit()

def insertAmenitiesTable(values):
    #print(values)
    sql = "INSERT INTO amenity(amenity) VALUES (%s)"
    print("DEEZ:",values)
    cursor.execute(sql, values)
    connection.commit()

def insertAvailableAmenitiesTable(values):
    #print(values)
    sql = "INSERT INTO availableamenities(PlanName, Amenity) VALUES (%s, %s)"
    #print(values)
    cursor.execute(sql, values)
    connection.commit()

#UPDATE

def updateCustomerTable(values):
    #print(values)
    sql = "UPDATE customer SET CustomerID = %s, Name = %s, Gender = %s, Weight = %s, Height = %s, PlanName = %s, StartDate = %s, EndDate = %s, ContactNo = %s, BirthDate = %s WHERE CustomerID = %s"
    #print(values)
    cursor.execute(sql, values)
    connection.commit()

def updateTrainerTable(values):
    #print(values)
    sql = "UPDATE trainer SET TrainerID = %s, Name = %s, PlanName = %s WHERE TrainerID = %s"
    #print(values)
    cursor.execute(sql, values)
    connection.commit()

def updatePlanTable(values):
    #print(values)
    sql = "UPDATE gymmembershipplan SET PlanName = %s, Pricing = %s WHERE PlanName = %s"
    #print(values)
    cursor.execute(sql, values)
    connection.commit()

def updateAmenitiesTable(values):
    #print(values)
    sql = "UPDATE amenity SET Amenity = %s WHERE Amenity = %s"
    #print(values)
    cursor.execute(sql, values)
    connection.commit()

# DELETE
def deleteCustomerTableRow(values):
    print(values)
    if values:
        sql = "DELETE FROM customer WHERE customerID = %s"

    print(values)
    cursor.execute(sql, (values,))
    connection.commit()
    
def deleteTrainersTableRow(values):
    print(values)
    if values:
        sql = "DELETE FROM trainer WHERE TrainerID =  %s"

    print(values)
    cursor.execute(sql, (values,))
    connection.commit()    

def deleteAmenityTableRow(values):
    print(values)
    if values:
        sql = "DELETE FROM amenity WHERE Amenity = %s"

    print(values)
    cursor.execute(sql, (values,))
    connection.commit() 

def deletePlansTableRow(values):
    print(values)
    if values:
        sql = "DELETE FROM gymmembershipplan WHERE PlanName = %s"

    print(values)
    cursor.execute(sql, (values,))
    connection.commit()

def deleteAvailableAmenities(values):
    if values:
        sql = "DELETE FROM availableamenities WHERE PlanName = %s AND Amenity = %s"
        print(values)
        cursor.execute(sql, values)
        connection.commit()



def queryCustomerTable():
    sql = "SELECT * FROM customer"
    cursor.execute(sql)
    rows = cursor.fetchall()
    #print(rows)
    return rows

def queryPlansTable():
    sql = "SELECT * FROM gymmembershipplan"
    cursor.execute(sql)
    rows = cursor.fetchall()
    #print(rows)
    return rows

def queryTrainersTable():
    sql = "SELECT * FROM trainer"
    cursor.execute(sql)
    rows = cursor.fetchall()
    #print(rows)
    return rows

def queryAmenitiesTable():
    sql = "SELECT * FROM amenity"
    cursor.execute(sql)
    rows = cursor.fetchall()
    #print(rows)
    return rows

def queryAvailableAmenitiesTable(value):
    sql = "SELECT Amenity FROM availableamenities WHERE PlanName = %s "
    cursor.execute(sql,value)
    rows = cursor.fetchall()
    #print(rows)
    return rows

####################################################################################################################################################################################
def deleteTableRow(values, choice):
    print(values)
    if choice == 0:
        sql = "DELETE FROM student_table WHERE studentID = %s"
    elif choice == 1:
        sql = "DELETE FROM course_table WHERE courseCode = %s"
    else:
        print("no choice selected")
        return
    
    print(values)
    if len(values) != 0 :
        for item in values:
            cursor.execute(sql, (values,))
            connection.commit()

def queryTable(choice):
    print(choice)
    if choice == 0:
        sql = "SELECT * FROM student_table"
    elif choice == 1:
        sql = "SELECT * FROM course_table"
    else:
        print("no choice selected")
        return

    cursor.execute(sql)
    rows = cursor.fetchall()
    #print(rows)
    return rows

def editTable(columnName, list, choice):
    #print(columnName)
    #print(list)
    if choice == 0:
        sql = f"UPDATE student_table SET {columnName} = %s WHERE studentID = %s"
    elif choice == 1:
        sql = f"UPDATE course_table SET {columnName} = %s WHERE courseCode = %s"

    cursor.execute(sql,list)
    connection.commit()

def closeConnection():
    cursor.close()
    connection.close()
