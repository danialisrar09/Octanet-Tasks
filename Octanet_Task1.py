class Atm:

    #Constructor which contain PIN and Balance as instance variable
    def __init__(self):

        self.__pin = " "
        self.__balance = 0
        self.Transaction_counter = 0
        self.menu()

    #This method is taking input
    def menu(self):
        Customer_input = int(input("""
                    Press 1 to set pin,
                    Press 2 for Cash deposit,
                    Press 3 for Cash withdrawal,
                    Press 4 for Acc balance inquiry,
                    Press 5 for Pin change,
                    Press 6 for Transaction history,
                    Press 7 to exit,
                """))

        if Customer_input == 1:
            self.set_pin()
            print("Pin Succesfully set")
            self.Transaction_counter += 1
            self.menu()

        elif Customer_input == 2:
            self.Cash_deposit()
            print("Deposit Successfull!")
            self.menu()

        elif Customer_input == 3:
            self.Cash_withdrawal()
            print("Withdrawal Successfull!")
            self.menu()

        elif Customer_input == 4:
            self.Acc_Balance_inquiry()
            self.menu()

        elif Customer_input == 5:
            new_pin = int(input("Enter the new pin for account: "))
            self.Change_pin(new_pin)
            print("Pin successfully changed! ")
            self.menu()
        else:
            print("Thankyou for your transaction!")
            return


    def set_pin(self):
        self.__pin = int(input("Set a pincode for your account: "))
        return self.__pin


    def Cash_deposit(self):
        self.__balance += int(input("Enter the amount you want to deposit in your account: "))
        return self.__balance

    def Cash_withdrawal(self):
        self.__balance -= int(input("Enter the amount your want to withdraw: "))
        return self.__balance

    def Acc_Balance_inquiry(self):
        print(f"Your current account balance is: {self.__balance}")

    def Change_pin(self, new_pin):
        self.__pin = new_pin
        return self.__pin

    # def transaction_history(self):





Cust = Atm()
