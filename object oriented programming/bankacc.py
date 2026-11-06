class Bank:
    def __init__(self,ini_bal):
        self.bal=ini_bal
        # self.wih=wih
        # self.dep=dep
    def deposit(self,dep):
        self.balance += dep
        return self.bal
    def withdraw(self,wih):
        if(self.bal<wih):
            return "balance is less"
        else:
            self.balance-=wih
            return self.bal
        # return self.
    def display(self):
        print(f"balance is {self.bal}")
withd=int(input("enter the number you want to withdraw"))
depo=int(input("enter the number you want deposit"))
banker=Bank(30000)
choice=int(input("do you wanna withdraw or deposit press 1 for withdrawal and press 2 for deposit or 3 for displaying balance"))
if choice == 1:
    withd = int(input("Enter the amount you want to withdraw: "))
    result = banker.withdraw(withd)
    if result == "balance is less":
        print("Transaction Failed: Insufficient balance.")
    else:
        print(f"Balance is now {result}")

elif choice == 2:
    depo = int(input("Enter the amount you want to deposit: "))
    print(f"Balance is now {banker.deposit(depo)}")

elif choice == 3:
    banker.display()
    
else:
    print("Invalid choice!")