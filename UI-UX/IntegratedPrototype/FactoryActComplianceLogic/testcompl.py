# -*- coding: utf-8 -*-
"""testcompl.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ElbQ_a0Bm9RniuYn7ZEn0TQd9RRpA7i8
"""

import sqlite3
conn = sqlite3.connect('localdb.db')
curs = conn.cursor()
print ("Opened database successfully");

curs.execute('''CREATE TABLE IF NOT EXISTS COMPANY
         (EmpID INT PRIMARY KEY     NOT NULL,
         First_Name             char(255) NOT NULL,
         Last_Name            char(255)   NOT NULL,
         datetoday            datetime,
        datetoday_1           datetime,
        status_1	                 char(255),
        status_2	                 char(255),
        status_3	                 char(255),
        status_4	                 char(255),
        status_5	                 char(255),
        status_6	                 char(255),
        status_7	                 char(255),
        status_8	                char(255)

        );''')

print ("Table created successfully");

#(curs.execute("INSERT  INTO COMPANY (EmpID,First_Name,Last_Name , datetoday, datetoday_1, status_1, status_2,status_3,status_4,status_5,status_6,status_7,status_8)\
####   VALUES (2,	'Olivia'	,'Moore'	,'0000-00-00'	,'0000-00-00',		'no',	'no',	'no',	'yes',	'yes',	'no',	'yes',	'no')");

#curs.execute("INSERT  INTO COMPANY(EmpID,First_Name,Last_Name,datetoday,datetoday_1,status_1,status_2,status_3,status_4,status_5,status_6,status_7,status_8)\
 #     VALUES (3,'William','Thomas','0000-00-00'	,'0000-00-00','yes'	,'no'	,'no'	,'yes'	,'no'	,'no'	,'yes'	,'yes')");

#curs.execute("INSERT  INTO COMPANY(EmpID,First_Name,Last_Name,datetoday,datetoday_1,status_1,status_2,status_3,status_4,status_5,status_6,status_7,status_8)\
 # VALUES (4,'Samantha','Smith',0000-00-00	,0000-00-00,'yes'	,'no'	,'no'	,'no'	,'yes'	,'yes'	,'no'	,'yes')");)
curs.execute("INSERT  INTO COMPANY(EmpID,First_Name,Last_Name,datetoday,datetoday_1,status_1,status_2,status_3,status_4,status_5,status_6,status_7,status_8)\
  VALUES (5,'amy','Smith',0000-00-00	,0000-00-00,'yes'	,'no'	,'no'	,'yes'	,'yes'	,'yes'	,'no'	,'yes')");
curs.execute("INSERT  INTO COMPANY(EmpID,First_Name,Last_Name,datetoday,datetoday_1,status_1,status_2,status_3,status_4,status_5,status_6,status_7,status_8)\
  VALUES (6,'david','pivale',0000-00-00	,0000-00-00,'yes'	,'yes'	,'yes'	,'yes'	,'yes'	,'yes'	,'yes'	,'yes')");
curs.execute("INSERT  INTO COMPANY(EmpID,First_Name,Last_Name,datetoday,datetoday_1,status_1,status_2,status_3,status_4,status_5,status_6,status_7,status_8)\
  VALUES (7,'jane','nile',0000-00-00	,0000-00-00,'yes'	,'no'	,'yes'	,'no'	,'yes'	,'yes'	,'no'	,'yes')");
curs.execute("INSERT  INTO COMPANY(EmpID,First_Name,Last_Name,datetoday,datetoday_1,status_1,status_2,status_3,status_4,status_5,status_6,status_7,status_8)\
  VALUES (8,'warner','gore',0000-00-00	,0000-00-00,'yes'	,'no'	,'no'	,'yes'	,'yes'	,'yes'	,'no'	,'no')");
curs.execute("INSERT  INTO COMPANY(EmpID,First_Name,Last_Name,datetoday,datetoday_1,status_1,status_2,status_3,status_4,status_5,status_6,status_7,status_8)\
  VALUES (9,'will','kale',0000-00-00	,0000-00-00,'yes'	,'no'	,'yes'	,'no'	,'yes'	,'yes'	,'yes'	,'yes')");
curs.execute("INSERT  INTO COMPANY(EmpID,First_Name,Last_Name,datetoday,datetoday_1,status_1,status_2,status_3,status_4,status_5,status_6,status_7,status_8)\
  VALUES (10,'sam','Smith',0000-00-00	,0000-00-00,'yes'	,'no'	,'no'	,'yes'	,'yes'	,'yes'	,'no'	,'yes')");
conn.commit()
print ("Records created successfully");

def check_eight_consecutive_days(emp_id, localdb):
    # Connect to the database
    conn = sqlite3.connect(localdb)

    # Retrieve the employee data from the database
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM COMPANY WHERE EmpID=?", (emp_id,))
    row = cursor.fetchone()
    if row is None:
        # Employee not found in the database
        return f"Employee {emp_id} not found"

    # Extract the status values from the row
    print("status_1 =", row[5])
    print("status_2 =", row[6])
    print("status_3 =", row[7])
    print("status_4 =", row[8])
    print("status_5 =", row[9])
    print("status_6 =", row[10])
    print("status_7 =", row[11])
    print("status_8 =", row[12])

    # Check if the employee has eight consecutive "yes" values
    if row[5:13] == ("yes",) * 8:
        # Return an error message
        error_message = f"Employee {emp_id} has come in eight consecutive days"
        return error_message

    # If no errors were found, return None
    return None

error_message = check_eight_consecutive_days(6, 'localdb.db')

# Check if there was an error message
if error_message is not None:
    print(error_message)
    print("Employee has been coming for 8 straight days. He/She needs to be stopped")
else:
    print("This employee has not come in on the second day consecutively.")