"""The registering a student for living springs camp
Make a funtion to register a student, make a string checker
By Daniel
"""

def string_checker(string, question):
    """Check if the input is in the alphahbet"""
    invaild = "\nSorry please enter a vaild option\n"
    while string.isalpha() is False:
        print (invaild)
        string = str(input(question))
    return string

def registering():
    """Funtion to ask for the student's name"""
    invaild = "\nSorry please enter a vaild option\n"
    student_registration = input("Would you like to register a student? (Y or N): ").title()
    student_registration_confirm = string_checker(student_registration,
                                              "Would you like to register a student?"
                                               " (Y or N): " ).title()
    if student_registration_confirm in NO:
        #End the program here
    elif student_registration_confirm in YES:
        #Ask for age here
    else:
        print(f"{invaild}")
        registering()


YES = ["Yes","Y","YES"]
NO = ["NO","No","N"]

#Main Routine

registering()
