from datetime import datetime

name = input("What is your name? \n")
allowedUsers = ['Seyi', 'Mike', 'Love']
allowedPassword = ['passwordSeyi', 'passwordMike', 'passwordLove']
now = datetime.now()
date = now.strftime("%Y/%m/%d %H:%M:%S")
balance = 5000

if name in allowedUsers:
    password = input("Your password? \n")
    userId = allowedUsers.index(name)

    if password == allowedPassword[userId]:
        print('Welcome' + ' ' + name + ',' + ' ' + 'You logged in at' + ' ' + date)
        print('These are the available options:')
        print('1.Withdrawal')
        print('2.Cash Deposit')
        print('3.Complaint')

        selectedOption = int(input('Please select an option \n'))

        if selectedOption == 1:

            print('You selected %s' % selectedOption)
            amountToWithdraw = int(input('How much would you like to withdraw \n'))

            if balance < amountToWithdraw:
                print("Insufficient balance")
            else:
                (print("Take your cash"))

        elif selectedOption == 2:
            print('you selected %s' % selectedOption)
            depositCash = int(input('How much would you like to deposit? \n'))
            print('Your current balance is' + ' ' + str((balance + depositCash)))
        elif selectedOption == 3:
            print('you selected %s' % selectedOption)
            complaint = input('What issue will you like to report? \n')
            print("Thank you for contacting us")
        else:
            print('Invalid option selected, please try again')
    else:
        print('Password Incorrect, please try again')

else:
    print('Name not found, please try again')
