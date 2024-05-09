"""The registering a student for living springs camp
Make a funtion to register a student, make a string checker
By Daniel C
"""

def string_checker(string, question_01):
    """Check if the input is in the alphahbet"""
    invaild = "\nSorry please enter a vaild option\n"
    while string.isalpha() is False:
        print (invaild)
        string = str(input(question_01))
    return string

def registering():
    """Funtion to ask for the student's name"""
    invaild = "\nSorry please enter a vaild option\n"
    student_registration = input("Would you like to register a student?"
                                 "(Y or N): ").title()
    student_registration_confirmed = string_checker(student_registration,
                                              "Would you like to register"
                                              "a student? (Y or N): " ).title()
    if student_registration_confirmed in NO:
        #End the program here in the final version
    elif student_registration_confirmed in YES:
        #Ask for age here in the final version
    else:
        print(f"{invaild}")
        registering()


YES = ["Yes","Y","YES"]
NO = ["NO","No","N"]

#Main Routine

registering()
