import random

# dictionary
database = {
    8651378502: ['Adunni', 'Eagle', 'sobamboadedotun@gmail.com', 'password', 200]
}


def init():
    print("Welcome to bank Eagle")
    try:
        have_account = int(input("Do you have an account: Enter 1(Yes) or 2(NO) \n"))
    except ValueError:
        print("Please enter the correspondent number for your transaction")
        return

    if have_account == 1:
        login()

    elif have_account == 2:
        register()

    else:
        print("You have selected invalid option")
        init()


def login():
    print("=== ==== === Login === === ===")

    account_number_from_user = input("Enter account number \n")
    is_valid_account_number = accountNumberValidation(account_number_from_user)

    if is_valid_account_number:
        password = input("Enter password \n")

        for account_number, user_details in database.items():
            if account_number == int(account_number_from_user):
                if user_details[3] == password:
                    bankOperation(user_details)
        print('Invalid account or password')
        login()
    else:
        init()


def accountNumberValidation(account_number):
    if account_number:

        if len(str(account_number)) == 10:

            try:
                int(account_number)
                return True
            except ValueError:
                print("Invalid Account Number, account number should not contain alphabets")
                return False
            except TypeError:
                print("Invalid account type")
                return False

        else:
            print("Please enter a 10 digit account number")
            return False

    else:
        print("Account number is a require field")
        return False


def register():
    print("Please Register your new account")
    email = input("Enter e-mail address \n")
    first_name = input("Enter first Name \n")
    last_name = input("Enter last Name \n")
    password = input("Create password \n")

    try:
        account_number = generateAccountNumber()
    except ValueError:
        print("Account generation failed due to connection failure")
        init()
    # account number is forming the key and the information(value) is the form
    # the list inside the dictionary
    database[account_number] = [first_name, last_name, email, password, 0]

    print("Your account has been created")
    print("=== ==== === === === ===")
    print("Your account number is: %d" % account_number)
    print("make sure to keep it safe")
    print("=== ==== === === === ===")

    login()


def bankOperation(user):
    print("Welcome %s %s" % (user[0], user[1]))

    try:
        selected_option = int(input("Press 1 to make a deposit \n"
                                    "Press 2  to make withdrawals \n"
                                    "Press 3 to Logout\n"
                                    "Press 4 to Exit\n"))
    except ValueError:
        print("Please the correct option for your transaction")
        return

    if selected_option == 1:
        depositOperation()
    elif selected_option == 2:
        withdrawalOperation()
    elif selected_option == 3:
        logout()
    elif selected_option == 4:
        exit()
    else:
        print("Invalid option selected")
        bankOperation(user)


def setCurrentBalance(user_details, deposit):
    user_details[4] = user_details[4] + deposit
    return user_details[4]


def getCurrentBalance(user_detail):
    return user_detail[4]


def withdrawalOperation():
    for account_number, user_details in database.items():
        try:
            withdraw = int(input(print('How much do you want to withdraw')))
        except ValueError:
            print("Please input amount to withdraw in digit")
            return
        if withdraw > getCurrentBalance(user_details):
            print("Insufficient funds")
        else:
            print("Please take your cash")
            print("your current balance is " + str(getCurrentBalance(user_details) - withdraw))

    whatToDoNext()


def depositOperation():
    for account_number, user_details, in database.items():
        try:
            deposit = int(input(print('How much do you want to deposit?')))
        except ValueError:
            print("Please input amount to deposit in digit")

        print("You have just deposited, " + str(deposit))

    whatToDoNext()


def whatToDoNext():
    try:
        proceed = int(input((print("Do you want to perform another transaction\n"
                                   "Press 1 to continue \n"
                                   "Press 2 to exit"))))
    except ValueError:
        print("Please input the ")

    if proceed == 1:
        for account_number, user_details in database.items():
            bankOperation(user_details)
    elif proceed == 2:
        exit()

    else:
        print("Invalid option entered")
        whatToDoNext()


def generateAccountNumber():
    return random.randrange(1111111111, 9999999999)


def logout():
    login()


init()
