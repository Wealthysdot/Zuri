from initails import money_at_hand


class Budget:
    category_balance = list()
    cat = dict()

    def __init__(self, name):
        self.name = name
        self.money_at_hand = money_at_hand
        self.depositExpenses = list()
        self.withdrawalExpenses = list()

    def deposit(self, category_amount, category_type):
        category = self.name = category_type
        """
        function for deposit
        Money deposited to each categories from main budget
        """
        if category_amount > self.money_at_hand:
            print(f"Insufficient funds \n"
                  f"You have assigned {self.money_at_hand} to total budget")
        else:
            self.money_at_hand += category_amount
            self.depositExpenses.append(
                {
                    "Budget Description": category,
                    "Deposit_Amount": category_amount
                })
            print(f"You have made a {category_amount} budget to  {category}")

    def withdrawal(self, expenses, expenses_description, budget):
        """
        function for withdraw
        The amount you withdrew from each categories
        Like if 5k was budgeted for food and you spent 200,
        so 200 is the amount withdrew from food budget to cover the
        expenses
        """
        if budget.money_at_hand > expenses:
            budget.money_at_hand -= expenses
            self.withdrawalExpenses.append({
                "category_expenses_description": expenses_description,
                "Withdrawal_Amount": expenses
            })
        else:
            print(f"Insufficient Funds. Unable to withdraw {expenses} from {budget.money_at_hand}")

    def total_deposit_expenses(self):
        total_deposit = 0
        for item in self.depositExpenses:
            total_deposit += item["Deposit_Amount"]
            if total_deposit > self.compute_category_balance():
                print("You have exceeded you budget for this category")
        return total_deposit

    def total_withdrawal_expenses(self):
        total_withdrawal = 0
        for item in self.withdrawalExpenses:
            total_withdrawal += item["Withdrawal_Amount"]
        return total_withdrawal

    def display_deposit_expenses(self):
        print(f"\n********Total Deposit Expense********")
        total_category_expense = 0
        for item in self.depositExpenses:
            expenses_desc = item["Budget Description"]
            expenses_amount = item["Deposit_Amount"]
            print(f"{expenses_desc}: {expenses_amount}")
            total_category_expense += expenses_amount
            if total_category_expense >= money_at_hand:
                break
        print(f"Your Total Deposit Expenses is : {self.total_deposit_expenses()}")

    def display_withdrawal_expenses(self):
        category_type = self.name
        print(f"     {category_type}     ")
        for item in self.withdrawalExpenses:
            expenses_desc = item["category_expenses_description"]
            expenses_amount = item["Withdrawal_Amount"]
            print(f"{expenses_desc}:{expenses_amount}")
        print(f"Total Expenses on {self.name} is: {self.total_withdrawal_expenses()}")

    def remain_Balance_after_Balance(self):
        category_balance = self.total_deposit_expenses() - self.total_withdrawal_expenses()
        self.category_balance.append(category_balance)
        return f"Remaining Balance after expense on {self.name} is {category_balance}\n" \
               f"You have Made a Total of {Budget.compute_category_balance()} from budget" \
               f"You have a Balance of {self.total_balance()}"

    @classmethod
    def compute_category_balance(cls):
        cat_balance = 0
        for balance in cls.category_balance:
            cat_balance += balance
        return cat_balance

    def transfer_funds(self, amount, budget):
        if self.money_at_hand > amount:
            self.money_at_hand -= amount
            budget.money_at_hand += amount
        else:
            print(f"Insufficient funds")

    def total_balance(self):
        total_balance = self.money_at_hand - Budget.compute_category_balance()
        return total_balance

    @staticmethod
    def enter_cat(cat_name, cat_budget_amount):
        Budget.cat.update({cat_name: cat_budget_amount})

    def calc_cat_budget_amount(self):
        # self.money_at_hand = int(input("Please Enter amount for total budget \n"))
        total_cat_budget = 0
        while self.money_at_hand > 0:
            name = input("enter budget category name")
            amount = int(input(f"enter {name} budget amount"))
            Budget.enter_cat(name, amount)
            total_cat_budget = total_cat_budget + Budget.cat.get(name)
            if self.money_at_hand <= total_cat_budget:
                print("You have made your budget \n"
                      "Please spend your money wisely ")
                break
        return total_cat_budget

    def enter_expenses(self):
        if Budget.cat.__len__() != 0:
            cat_expenses = dict()
            for name in Budget.cat:
                expense = input(f"enter expense for {name}")
                while cat_expenses.get(name) > Budget.cat.get(name):
                    expense = input(f"enter expense for {name}")
                cat_expenses.update({name: expense})
        else:
            print("You have not made a budget")