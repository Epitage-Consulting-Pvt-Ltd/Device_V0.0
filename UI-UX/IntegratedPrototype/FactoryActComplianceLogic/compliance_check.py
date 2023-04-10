import csv
from datetime import datetime, timedelta

def check_eight_consecutive_days(emp_id, file_path):
    # Read the employee data from the .csv file
    with open(file_path, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        # Create a dictionary to hold the status for each employee
        employee_status = {}
        for row in reader:
            id = int(row["emp id"])
            status_1 = row["status_1"]
            status_2 = row["status_2"]
            status_3 = row["status_3"]
            status_4 = row["status_4"]
            status_5 = row["status_5"]
            status_6 = row["status_6"]
            status_7 = row["status_7"]
            status_8 = row["status_8"]

            # Save the status for this employee
            if id == emp_id:
                employee_status = {"status_1": status_1,"status_2": status_2,"status_3": status_3,"status_4": status_4,"status_5": status_5,"status_6": status_6,"status_7": status_7,"status_8": status_8}
                break

    # Check if the employee has a "yes" value for both "status today" and "status tomorrow"
    if employee_status["status_1"] == "yes" and employee_status["status_2"] == "yes" and employee_status["status_3"] == "yes" and employee_status["status_4"] == "yes" and employee_status["status_5"] == "yes" and employee_status["status_6"] == "yes" and employee_status["status_7"] == "yes" and employee_status["status_8"] == "yes":
        # Return an error message
        error_message = f"Employee {emp_id} has come in two consecutive days"
        return error_message

    # If no errors were found, return None
    return None
