"""The welcome screen for the living springs registration site
Make a welcome screen, create constants, 
make the big loop, make some variables
By Daniel C
"""
def welcome_screen():
    """Welcome screen title"""
    go = True
    while go:
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("****** Living Springs Holiday Camp - registration ******")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")



SHUTTLE_COST = 80
NO_SHUTTLE_COST = 0
MEALS = [["1. Standard",],
         ["2. Vegan",],
         ["3. Vegetarian"]
         ]
CAMP_OPTIONS = [["1.Walking and social skills",5,"easy",800],
                ["2.Kayaks and swimming",3,"moderate",400],
                ["3.Tramping and biking",4,"difficult",900],
                ]

#Main Routine
welcome_screen()
