"""Ask the student for their name
Make a funtion to ask for their first and last name along with a string checker
By Daniel C
"""

def string_checker(string, question_01):
    """Check if the input is in the alphahbet"""
    invaild = "\nSorry please enter a vaild option\n"
    while string.isalpha() is False:
        print (invaild)
        string = str(input(question_01))
    return string

def student_name():
    """Asks for students, check if it's a string"""
    first_name = input("Enter the students first name: ")
    first_name_confirmed = string_checker(first_name,
                                        "Enter the students"
                                         " first name: ").title()
    last_name = input("Enter the students last name: ")
    last_name_confirmed = string_checker(last_name,
                                        "Enter the students "
                                        "last name: ").title()
    print(first_name_confirmed, last_name_confirmed)



#main routine
student_name()
