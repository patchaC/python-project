# ATM part 1

import random
import pandas as pd


class ATM :
    def __init__(self, name, bank) :
        self.name = name
        self.bank = bank
        self.balance = 0
        self.movement = pd.DataFrame([['Start', 0]],
                                     columns = ['transaction','amount'])


    def deposit(self, dep_amount) :
        if (dep_amount < 0) :
            print("\033[31mCannot deposit less than 0 amount !!\033[0m")
        else :
            self.balance += dep_amount
            new_move = {'transaction': 'Deposit', 'amount': dep_amount}
            self.movement.loc[len(self.movement)] = new_move
            print(f"\033[32mTransaction successfull. Your balance is {self.balance} THB\033[0m \n")

    def withdraw(self, with_amount) :
        if (with_amount <0) :
            print("\033[31mCannot withdraw less than 0 amount !!\033[0m")

        elif(with_amount > self.balance) :
            print("\033[31mYour balance is not enough !!\033[0m")

        else :
            self.balance -= with_amount
            new_move = {'transaction': 'Withdraw', 'amount': with_amount}
            self.movement.loc[len(self.movement)] = new_move
            print(f"\033[32mTransaction successfull. Your balance is {self.balance} THB\033[0m \n")

    def transfer(self, tf_amount, destination) :
        if (tf_amount <0) :
            print("\033[31mCannot transfer less than 0 amount !!\033[0m")

        elif(tf_amount > self.balance) :
            print("\033[31mYour balance is not enough !!\033[0m")

        else :
            self.balance -= tf_amount
            new_move = {'transaction': 'Transfer', 'amount': tf_amount}
            self.movement.loc[len(self.movement)] = new_move
            print("\033[32mTransaction successfull.\033[0m")
            print(f"\033[32mYour money {tf_amount} THB is transfered to the account {destination}.\033[0m")
            print(f"\033[32mYour balance is {self.balance} THB\033[0m \n")

    def history(self) :

        print(">> Welcome to your online bank account <<\n")
        print(f"     ** Your balance is {self.balance} THB **\n")
        print("> Your recent transaction are...\n", self.movement.iloc[:] )

    def OTP(self) :
        otp = random.random()
        otp = int((otp*10**6) // 1)
        print(f"\033[32mRequest successfull. Your otp is {otp} \033[0m")


# atm part2 input

banklist = ['none','scb','bkkb','ttb','ktb']

print("Welcome to your ATM. It's a great day today. Let's do some quick register!\n")

name = input("please name your account (only alphabet): ")
b_list = input("please select the bank(1-4): \n[1]scb          [3]ttb\n[2]bkkb         [4]ktb ")
b_list = int(b_list)
bank = banklist[b_list]

user = ATM(name, bank)

print(f"\n           HI {user.name} !! This is your {user.bank} Bank Account")
user.history()
print(" ")

while True :
    print("Please select the services you want to go through (1-6)")
    print("[1] Deposit")
    print("[2] Withdraw")
    print("[3] Transfer")
    print("[4] History")
    print("[5] Request OTP")
    print("[6] exit")
    go = int(input())

    try :
        if(go == 1) :
            dep_amount = int(input("please insert the amount you want to deposit: "))
            user.deposit(dep_amount)
        elif(go == 2) :
            with_amount = int(input("Please insert the amount you want to withdraw: "))
            user.withdraw(with_amount)
        elif(go == 3) :
            tf_amount = int(input("Please insert the amount you want to transfer: "))
            destination = input("Type the destination account number (xxx-xxx): ")
            user.transfer(tf_amount, destination)
        elif(go == 4) :
            user.history()
        elif(go == 5) :
            user.OTP()
        elif(go == 6) :
            print(f"\n   Bye {name}! You have a wonderful day :)")
            break
        else :
            print(">> please try again")
    except :
        print(">> please try again")
