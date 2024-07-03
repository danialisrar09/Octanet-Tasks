import datetime


class Atm:

    #Constructor which contain PIN and Balance as instance variable
    def __init__(self):

        # We applied encapsulation on pin and balance variable to make it private, since both of these info are confidential
        self.__pin = " "
        self.__balance = 0
        self.deposit_history = []
        self.withdraw_history = []
        self.menu()

    #This method is main menu and perform conditional process of the atm machine
    def menu(self):
        # Here the atm machine is taking input from the user
        Customer_input = int(input("""
                    Press 1 to set pin,
                    Press 2 for Cash deposit,
                    Press 3 for Cash withdrawal,
                    Press 4 for Acc balance inquiry,
                    Press 5 for Pin change,
                    Press 6 for Transaction history,
                    Press 7 to exit,
                """))

        # Here we are applied the condition statement where it is checking against all the desired input.
        # If user input 1, set pin method will be called
        if Customer_input == 1:
            self.set_pin()
            print("Pin Succesfully set")
            self.menu()

        # If user input 2, cash deposit method will be called
        elif Customer_input == 2:
            self.Cash_deposit()
            print("Deposit Successfull!")
            # self.date_time = datetime.datetime
            self.menu()
            # return self.date_time

        # If user input 3, cash withdrawal method will be called
        elif Customer_input == 3:
            self.Cash_withdrawal()
            print("Withdrawal Successfull!")
            # self.date__time = datetime.datetime
            self.menu()
            # return self.date__time

        # If user input 4, account balance inquiry method will be called
        elif Customer_input == 4:
            self.Acc_Balance_inquiry()
            self.menu()

        # If user input 5, machine will ask user to input new pin and change pin method will be called
        elif Customer_input == 5:
            new_pin = int(input("Enter the new pin for account: "))
            self.Change_pin(new_pin)
            print("Pin successfully changed! ")
            self.menu()

        elif Customer_input == 6:
            self.transaction_history()

        # If user input 7, machine will automatically terminated process and print a thankyou message
        else:
            print("Thankyou for your transaction!")
            return

    # This method takes input and saves in self.__pin and return it
    def set_pin(self):
        self.__pin = int(input("Set a pincode for your account: "))
        return self.__pin

    # This method takes input, add the input amount from the acc balance and saves in self.__balance and return it
    def Cash_deposit(self):
        deposit_amount = int(input("Enter the amount you want to deposit in your account: "))
        self.deposit_history.append(deposit_amount)
        self.__balance += deposit_amount
        self.deposit_date = datetime.date
        self.deposit_time = datetime.time
        return self.__balance, self.deposit_date, self.deposit_time

    # This method takes input, minus the input amount from the acc balance and saves in self.__balance and return it
    def Cash_withdrawal(self):
        withdraw_amount = int(input("Enter the amount your want to withdraw: "))
        self.withdraw_history.append(withdraw_amount)
        self.__balance -= withdraw_amount
        self.withdraw_date = datetime.date
        self.withdraw_time = datetime.time
        return self.__balance, self.withdraw_date, self.withdraw_time

    # This method displays self.__balance.
    def Acc_Balance_inquiry(self):
        print(f"Your current account balance is: {self.__balance}")

    # This method takes new_pin as parameter and saves the new_pin in self.__pin and return it
    def Change_pin(self, new_pin):
        self.__pin = new_pin
        return self.__pin

    def transaction_history(self):
        Deposit_or_withraw = int(input("""
            Enter 1, to view deposit history
            Enter 2, to view withdraw history
        """))

        if Deposit_or_withraw == 1:
            for i in self.deposit_history:
                print(f"You deposited {i} amount at {self.deposit_time} on {self.deposit_date}")
        elif Deposit_or_withraw == 2:
            for i in self.withdraw_history:
                print(f"You deposited {i} amount at {self.withdraw_time} on {self.withdraw_date}")
        else:
            return "Invalid input!"






# Here we called an object named "Cust" of the class named "Atm"
Cust = Atm()
