"""Ask for what activities they want sign up for
Show the list of activities, ask for which one they want,
make an integer checker, check the range of the integer
By Daniel C
"""
def int_checker(question_02):
    """Checks the input was a null or string repeats until receives a int."""
    invaild = "\n You must enter an whole number that's from 1 to 3\n"
    num = ""
    while not num:
        try:
            num = int(input(question_02))
            return num
        except ValueError:
            print(invaild)

def activity_choice():
    """Checks that's what's entered is in the range 1,2,3"""
    invaild = "\n You must enter an whole number that's from 1 to 3\n"
    print("\nThese are the avaliable activities and cost:")
    for options in CAMP_OPTIONS:
        print(f"\t{options[0]} for {options[1]} days, rated {options[2]},"
              f" and costing ${options[3]:.2f}")
    student_choice = int_checker("Please enter your "
                                 "camp option: '1', '2', or '3': ")
    while student_choice not in RANGE_OF_ACTIVITIES:
        print(invaild)
        student_choice = int_checker("Please enter your "
                                 "camp option: '1', '2', or '3': ")
    chosen_camp = CAMP_OPTIONS[int(student_choice)-1]
    print()
    print(f"You have chose '{chosen_camp[0]}', over {chosen_camp[1]}"
          f" days, with a skill level of '{chosen_camp[2]}' and costing"
          f" ${chosen_camp[3]:.2f}!\n")
    return chosen_camp

CAMP_OPTIONS = [["1. Walking and social skills",5,"easy",800],
                ["2. Kayaks and swimming",3,"moderate",400],
                ["3. Tramping and biking",4,"difficult",900],
                ]
RANGE_OF_ACTIVITIES = [1, 2, 3]

#Main routine
activity_choice()
