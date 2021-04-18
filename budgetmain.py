from budgetApp import Budget

budget = Budget("budget")


# food = Budget("Food")
# clothing = Budget("Clothing")
# transport = Budget("Transport")
# entertainment = Budget("entertainment")
#
# food.name = input("Enter your budget category\n")
# try:
#     food_amount = int(input("Enter your budget amount \n"))
#     budget = Budget.deposit(food, food_amount, food.name)
# except ValueError:
#     print("Please input amount in digit")
#
# clothing.name = input("Enter your budget category\n")
# try:
#     clothing_amount = int(input("Enter your budget amount "))
# except ValueError:
#     print("Please input amount in digit")
#
# budget = Budget.deposit(clothing, clothing_amount, clothing.name)
#
# transport.name = input("Enter your budget category\n")
# transport_amount = int(input("Enter your budget amount "))
# budget = Budget.deposit(transport, transport_amount, transport.name)
#
# entertainment.name = input("Enter your budget category\n")
# entertainment_amount = int(input("Enter your budget amount "))
# budget = Budget.deposit(entertainment, entertainment_amount, entertainment.name)
#
# user_selection = int(input("Select 1 to enter expenses or 2 to exit"))
# if user_selection == 1:
#     expense_description = input("Enter your expenses description: ")
#     expense_amount = int(input("Enter your budget amount: "))
# else:
#     exit()
#
# food.withdrawal(expense_amount, expense_description, food)
# expense_description = input("Enter your expenses description: ")
# expense_amount = int(input("Enter your budget amount: "))
# food.withdrawal(expense_amount, expense_description, food)
# expense_description = input("Enter your expenses description: ")
# expense_amount = int(input("Enter your budget amount: "))
# food.withdrawal(expense_amount, expense_description, food)
# expense_description = input("Enter your expenses description: ")
# expense_amount = int(input("Enter your budget amount: "))
# food.withdrawal(expense_amount, expense_description, food)
#
# expense_description = input("Enter your expenses description: ")
# expense_amount = int(input("Enter your budget amount: "))
# clothing.withdrawal(expense_amount, expense_description, clothing)
#
# expense_description = input("Enter your expenses description: ")
# expense_amount = int(input("Enter your budget amount: "))
# clothing.withdrawal(expense_amount, expense_description, clothing)
#
# expense_description = input("Enter your expenses description: ")
# expense_amount = int(input("Enter your budget amount: "))
# clothing.withdrawal(expense_amount, expense_description, clothing)
#
# expense_description = input("Enter your expenses description: ")
# expense_amount = int(input("Enter your budget amount: "))
# clothing.withdrawal(expense_amount, expense_description, clothing)
#
#
# def main():
#     print(food.display_deposit_expenses())
#     print(food.display_withdrawal_expenses())
#     print(clothing.display_deposit_expenses())
#     print(clothing.display_withdrawal_expenses())
#     print(food.remain_Balance_after_Balance())
#     print(Budget.total_balance())

def main():
    print(budget.calc_cat_budget_amount())


if __name__ == '__main__':
    main()
