"""Ask if the student wants to use the shuttle to Living Springs
Ask if they want to use a shuttle (show the price), use a string checker
check the yes and no list
if they don't want the shuttle move on
By Daniel C
"""

def string_checker(string, question_01):
    """Check if the input is in the alphahbet"""
    invaild = "\nSorry please enter a vaild option\n"
    while string.isalpha() is False:
        print (invaild)
        string = str(input(question_01))
    return string

def student_shuttle():
    """Ask if the students wants to use the shuttle"""
    invaild = "\nSorry please enter a vaild option\n"
    shuttle_student = input(f"Would you like the ride the shuttle for "
                        f"${SHUTTLE_COST} to 'Living Springs? Y or N: ").title()
    while shuttle_student not in YES_NO:
        print(invaild)
        shuttle_student = input(f"Would you like the ride the shuttle for "
                                f"${SHUTTLE_COST} to "
                                "'Living Springs? Y or N: ").title()
    if shuttle_student in NO:
        #add the SHUTTLE_COST to the total cost
        print("Thank you for using the shuttle!")
        #Move on to the meals
    else:
        #Add the NO_SHUTTLE_COST to the total cost
        print(":(")
        #Move on to the meals

SHUTTLE_COST = 80
NO_SHUTTLE_COST = 0
YES_NO = ["Yes","Y","YES", "NO","No","N"]
YES = ["Yes","Y","YES"]
NO = ["NO","No","N"]


#Main routine
student_shuttle()
