from budgetApp import Budget

start = Budget("budget")


def init():
    print("Welcome to EagleBudget")
    try:
        to_do = int(input("What would you like to do:\n"
                          "Enter 1 to create budget \n"
                          "Enter 2 to enter expenses \n"
                          "Enter 3 to transfer money from a category"))
    except ValueError:
        print("Please enter the correspondent number for your transaction")
        return

    if to_do == 1:
        start.calc_cat_budget_amount()
    #     Todo optional expenses

    elif to_do == 2:
     #    Todo compulsory expense
     #    Todo optional budget
    elif to_do == 3:

    else:
        print("You have selected invalid option")
        init()



P
