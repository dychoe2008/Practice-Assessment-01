"""The welcome screen for the living springs registration site
Make a welcome screen, create constants, 
make the big loop, make some variables
By Daniel :D
"""
SHUTTLE_COST = 80
NO_SHUTTLE_COST = 0
YES_OR_NO = ["Yes", "Y", "No", "N"]
MEALS = [["1. Standard",],
         ["2. Vegan",],
         ["3. Vegetarian"]
         ]
yes = True

while yes:
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("******** Living Springs Holiday Camp - registration ********")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

    decision = input("Do you like men?: ")
    if decision != 1:
        print(":D")
    else:
        yes = False
