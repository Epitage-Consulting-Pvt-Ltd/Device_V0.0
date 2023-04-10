# Import the function
from compliance_check import check_eight_consecutive_days

# Call the function
error_message = check_eight_consecutive_days(6,'employee_data.csv')

# Check if there was an error message
if error_message is not None:
    print(error_message)
    print("Employess has been coming for 8 straight days . He/She needs to be stopped")
else:
    print("This employee has not come in on the second day consecutively.")


#TODO multiple persons check ?