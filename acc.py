class BankAccount:
    def __init__(self,acc_no, bal):
        self.acc_no = acc_no
        self.balance= bal
    def deposit(self):
        amt = float(input("Enter amount to deposit"))
        self.balance = self.balance + amt
        print(f"deposited{amt}")

    def withdraw(self):
        amt = float(input("Enter amount to withdraw"))
        if amt <= self.balance:
            self.balance = self.balance - amt
            print(f"Withdrawn:{amt}")
        else:
            print("Not enouch balance")

    def check_balance(self):
        print(f"Current balance:{self.balance}")
        acc = input("Enter account number")
        bal = float(input("Enter initial balance"))
        obj = BankAccount(acc,bal)
        while True:
            print("\n1 Deposit")
            print("2 Withdraw")
            print("3 Check Balance")
            print("4 Exit")

            ch = input("Enter Choice: ")

            if ch == "1":
                obj.deposit()
            elif ch == "2":
                obj.withdraw()
            elif ch == "3":
                obj.check_balance
            elif ch == "4":
                print("Thank you")
                break
            else:
                print("Wrong choice")