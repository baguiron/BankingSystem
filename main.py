from user import UserAccount
from bank import NorthernBank
import os.path

user = UserAccount(" ", " ", " ")
bank = NorthernBank("0")


def main():
    while True:
        print ("""
        ===== Northern Bank =====
              1. Login
              2. Sign up
              3. Exit
        """)
        choice = input("Enter your choice: ")
        try:
            choice = int(choice)
        except ValueError:
            print("Invalid input! \nPlease input a Number!")
            main()

        if choice == 1:
            account = user.userLogin()
            userAcc, userName = account
            if userAcc == 1:
                while True:
                    print("""
                        ===== Northern Bank =====
                              1. Deposit
                              2. Withdraw
                              3. Balance
                              4. Transaction
                              5. Log out
                              6. Exit
                        """)
                    choice = input("Enter your choice: ")
                    try:
                        choice = int(choice)
                    except ValueError:
                        print("Invalid input! \nPlease input a Number!")
                        userAcc = 1

                    if choice == 1:
                        bank.userDeposit(userName)

                    elif choice == 2:
                        bank.userWithdraw(userName)

                    elif choice == 3:
                        bank.userBalance(userName)

                    elif choice == 4:
                        bank.userTransaction(userName)

                    elif choice == 5:
                        main()

                    elif choice == 6:
                        print("Thank you for using Northern Bank!")
                        print("Hope we see you again!")
                        exit()

                    else:
                        print("Invalid input! Please enter a value from 1-5!")
                        userAcc = 1

            main()

        elif choice == 2:
            user.userSignup()
            main()

        elif choice == 3:
            print("Thank you for using Northern Bank!")
            print("Hope we see you again!")
            exit()

        else:
            print("Invalid input! Please enter a value from 1-3!")
            main()


if __name__ == "__main__":
    fileExist = os.path.exists("userfile")
    try:
        if fileExist:
            main()
        else:
            x = open("userfile", "x")
            x.close()
            main()

    except FileExistsError:
        print("File alraedy exist.")
