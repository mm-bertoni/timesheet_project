'''
Margaret Bertoni
Module with functions to create a basic time sheet program
'''
def user_response_truth_false_handling(user_response:str):
    '''
    Function: user_response_truth_false_handling
    Inputs: A True or False response from a user
    Returns: Standardized Representation of T or F
    '''

    # Strip any spaces
    user_response = user_response.strip()

    # Standardize responses to uppercase
    user_response = user_response.upper()

    # If entered Full Word, drop so only T or F
    user_response = user_response[0]

    return user_response

def user_response_name_handling(user_response:str):
    '''
    Function: user_response_name_handling
    Input: User response for a name
    Return: Cleaned up name with captilization
    '''
    # Strip any spaces
    user_response = user_response.strip()

    # Capitalize first letter in name
    user_response = user_response.capitalize()

    return user_response

def setup_employee_roster(employee_roster=set()):
    '''
    Function: setup_employee_roster
    Inputs: Can pass existing roster list, otherwise prompts users to enter employee names
    Returns: Employee roster
    '''
    # Determine if user has new employees to add and use user_response_truth_false_handling
    have_new_employees = user_response_truth_false_handling(input("Do you have new employees to add? Type Y for yes and N for no "))

    
    # Loop through adding new employees
    while have_new_employees == 'Y':
        new_employee = user_response_name_handling(input("Type the name of your new employee "))
        employee_roster.add(new_employee)
        have_new_employees = user_response_truth_false_handling(input("Do you have more employees to add? Type Y for yes and N for no "))
    
    return employee_roster

# def write_employee_roster_file(employee_roster:set):
#     '''
#     Function: write_employee_roster_file
#     Input: employee_roster set
#     Return: 

#     '''
        

def main():
    # So far, can create a new employee roster list from user inputs. 

if __name__ == "__main__":
    main()