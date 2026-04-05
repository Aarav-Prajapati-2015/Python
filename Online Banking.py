import os
import time

# login
name = input("Enter your name: ")
print("Hello", name, "welcome to online banking")
password = int(input("Enter your password: "))
if password == 12345678:
    balance = 1000
    while True:
        os.system("cls")
        print("---------------------------- Online Banking ------------------------------------")
        print()
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print()
        opt = int(input("Choose an option: "))
        if opt == 1:
            print("Balance =", balance)
            time.sleep(3)
        elif opt == 2:
            dmoney = float(input("How much money you want to deposit? "))
            balance += dmoney
            print("Total money deposited =", dmoney, "and Balance =", balance)
            time.sleep(3)
        elif opt == 3:
            wmoney = float(input("How much money you want to withdraw? "))
            if wmoney > balance:
                print("No money mad!")
                time.sleep(3)
            else:
                print("Money Withdrawn = ", wmoney, " and Balance = ", balance - wmoney)
                balance -= wmoney
                time.sleep(3)
        else:
            print("Invalid choice you mad!")
            time.sleep(3)
else:
    print("Incorrect password you mad!")