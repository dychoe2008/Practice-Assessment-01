"""Ask for their age
Make funtion to check the input for a integer, repeat if it's not.
By Daniel C
"""
def int_checker(question_02):
    """Checks the input was a null or string repeats until receives a int."""
    invaild = "\n You must enter an integer that's 15-18\n"
    num = ""
    while not num:
        try:
            num = int(input(question_02))
            return num
        except ValueError:
            print(invaild)


def student_age():
    """Checks if the integer is within 15-18"""
    invaild = "\n You must enter an whole number that's from 15-18\n"
    age_of_student = int_checker("What is the age of your student?: ")
    if age_of_student <= MAXIMUM_AGE and age_of_student >= MINIMUM_AGE:
        print(age_of_student)
        return age_of_student
    else:
        print(invaild)
        student_age()


MINIMUM_AGE = 15
MAXIMUM_AGE = 18

#Main routine
student_age()
