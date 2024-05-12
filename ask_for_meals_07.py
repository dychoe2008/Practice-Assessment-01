"""Ask what meal the student would like at Living Springs
Use a integer check to check the input from a range of 1-3
Show the avaliable meals
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

def student_meal():
    """Ask what kind of meal the student wants"""
    invaild = "\n You must enter an whole number that's from 1 to 3\n"
    print("Avaliable Meals:")
    for options in MEALS_AVALIABLE:
        print(f"\t{options[0]}")
    ask_meal = int_checker("What type of meal would "
                          "you like for the camp? 1-3: ")
    while ask_meal not in RANGE_FOR_MEALS:
        print(invaild)
        ask_meal = int_checker("What type of meal would "
                                  "you like for the camp? 1-3: ")
    if ask_meal == 1:
        chosen_meal = MEALS_AVALIABLE[int(ask_meal)-1]
        for meal in chosen_meal:
            print(f"You have chosen '{meal}' as your meal")
    elif ask_meal == 2:
        chosen_meal = MEALS_AVALIABLE[int(ask_meal)-1]
        for meal in chosen_meal:
            print(f"You have chosen '{meal}' as your meal")
    else:
        chosen_meal = MEALS_AVALIABLE[int(ask_meal)-1]
        for meal in chosen_meal:
            print(f"You have chosen '{meal}' as your meal")


RANGE_FOR_MEALS = [1, 2, 3]
MEALS_AVALIABLE = [["1. Standard",],
         ["2. Vegan",],
         ["3. Vegetarian"]
         ]

#Main routine
student_meal()
