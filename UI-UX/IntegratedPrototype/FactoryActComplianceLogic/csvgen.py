import csv
import random
from datetime import datetime, timedelta

# Set the number of employees to generate
num_employees = 10

# Create a list of first names and last names
first_names = ["John", "Jane", "David", "Amy", "Michael", "Samantha", "Eric", "Emily", "William", "Olivia"]
last_names = ["Smith", "Johnson", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson", "Thomas"]

# Create a list to hold the employee data
employee_data = []

# Generate the employee data
for i in range(num_employees):
    emp_id = i + 1
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    datetoday = datetime.now().strftime("%Y-%m-%d")
    datetoday_plus_1 = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    status_1 = random.choice(["yes", "no"])
    status_2 = random.choice(["yes", "no"])
    status_3 = random.choice(["yes", "no"])
    status_4 = random.choice(["yes", "no"])
    status_5 = random.choice(["yes", "no"])
    status_6 = random.choice(["yes", "no"])
    status_7 = random.choice(["yes", "no"])
    status_8 = random.choice(["yes", "no"])

    employee_data.append([emp_id, first_name, last_name, datetoday, datetoday_plus_1, status_1,status_2,status_3,status_4,status_5,status_6,status_7,status_8])

# Write the employee data to a .csv file
with open("employee_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["emp id", "first name", "last name", "datetoday", "datetoday+1", "status_1","status_2","status_3","status_4","status_5","status_6","status_7","status_8"])
    writer.writerows(employee_data)




