"""Living springs v1
By Daniel C
"""
# pylint: disable = c0103
def string_checker(string, question_01):
    """Check if the input is in the alphahbet"""
    invaild_str = "\nSorry please enter a vaild option\n"
    while string.isalpha() is False:
        print (invaild_str)
        string = str(input(question_01))
    return string

def int_checker(question_02):
    """Checks the input was a null or string repeats until receives a int."""
    invaild_int = "\n You must enter an integer that's 15-18\n"
    num = ""
    while not num:
        try:
            num = int(input(question_02))
            return num
        except ValueError:
            print(invaild_int)

def welcome_screen():
    """Welcome screen title"""
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("****** Living Springs Holiday Camp - registration ******")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")


SHUTTLE_COST = 80
NO_SHUTTLE_COST = 0
YES_NO = ["Yes","Y","YES", "NO","No","N"]
YES = ["Yes","Y","YES"]
NO = ["NO","No","N"]
MINIMUM_AGE = 15
MAXIMUM_AGE = 18
CAMP_OPTIONS = [["1. Walking and social skills",5,"easy",800],
                ["2. Kayaks and swimming",3,"moderate",400],
                ["3. Tramping and biking",4,"difficult",900],
                ]
RANGE_OF_ACTIVITIES = [1, 2, 3]
RANGE_FOR_MEALS = [1, 2, 3]
MEALS_AVALIABLE = [["1. Standard",],
         ["2. Vegan",],
         ["3. Vegetarian"]
         ]
#Main Routine
go = True
invaild = "\nSorry please enter a vaild option\n"
invaild_age = "\n You must enter an whole number that's from 15-18\n"
while go:
    welcome_screen()
