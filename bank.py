import os.path
import re

def deposit(n):
    status = "Deposit"
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:=+-]') 

    try:
        bal = "0"
        dr = open(n, "r")
        dt = open(n + "Trans", "r")
        amount = input("Enter amount you want to deposit: ")
        try:
            amount = int(amount)
        except ValueError:
            print("Invalid input! \nPlease only input numbers!")
            amount = None
            deposit(n)
        if amount == 0:
            print("Please enter amount higher than zero!")
            deposit(n)
        elif regex.search(str(amount)) != None:
            print("Please do not input special characters!")
            deposit(n)
        else:
            lst = append(n)
        try:
            if len(lst) != 0:
                try:
                    lst[-1] = int(lst[-1])
                    bal = int(bal)
                    bal = amount + lst[-1]
                    bal = str(bal)
                    amount = str(amount)
                    dr = open(n, "a")
                    dt = open(n + "Trans", "a")
                    dr.write(n + ", " + bal + "\n")
                    dt.write(amount + ", " + status + "\n")
                    print("Deposit successful.")
                    dr.close()
                    dt.close()
                except TypeError:
                    print("")
            else:
                bal = int(bal)
                bal += amount
                bal = str(bal)
                amount = str(amount)
                dr = open(n, "a")
                dt = open(n + "Trans", "a")
                dr.write(n + ", " + bal + "\n")
                dt.write(amount + ", " + status + "\n")
                print("Deposit successful.")
                dr.close()
                dt.close()
        except UnboundLocalError:
            print("")
    except FileNotFoundError:
        createFile(n)

def withdraw(n):
    status = "Withdraw"
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:=+-]') 

    try:
        amount = input("Enter amount you want to withdraw: ")
        try:
            amount = int(amount)
        except ValueError:
            print("Invalid input! \nPlease only input numbers!")
            amount = None
        if amount == 0:
            print("Please enter amount higher than zero!")
            withdraw(n)
        elif regex.search(str(amount)) != None:
            print("Please do not input special characters!")
            withdraw(n)
        else:
            lst = append(n)
        try:
            try:
                if len(lst) != 0:
                    lst[-1] = int(lst[-1])
                    try:
                        if amount > lst[-1]:
                            print("Insufficient balance.")
                        else:
                            bal = lst[-1] - amount
                            bal = str(bal)
                            amount = str(amount)
                            dr = open(n, "a")
                            dt = open(n + "Trans", "a")
                            dr.write(n + ", " + bal + "\n")
                            dt.write(amount + ", " + status + "\n")
                            print("Withdraw successful.")
                            dr.close()
                            dt.close()
                    except TypeError:
                        withdraw(n)
                else:
                    print("There is no balance in your account!")
            except UnboundLocalError:
                print("")
        except ValueError:
            print("Account empty!")
    except FileNotFoundError:
        createFile(n)

def append(n):
    dr = open(n, "r")
    dt = open(n + "Trans", "r")
    f = []
    d = []
    for i in dr:
        a, b = i.split(", ")
        b = b.strip()
        f.append(a)
        d.append(b)
    j = []
    k = []
    for i in dt:
        a, b = i.split(", ")
        b = b.strip()
        j.append(a)
        k.append(b)
    dr.close()
    dt.close()
    return d
    
def createFile(n):
    x = open(n, "x")
    y = open(n + "Trans", "x")
    x.close()
    y.close()
    print("New account has been made!")
    print("Enter again your choice!")


class NorthernBank:

    def userDeposit(self, n):
        return deposit(n)

    def userWithdraw(self, n):
        return withdraw(n)

    def userBalance(self, n):
        try:
            dr = open(n, "r")
            print("{} Account".format(n))
            try:
                f = []
                d = []
                for i in dr:
                    a, b = i.split(", ")
                    b = b.strip()
                    f.append(a)
                    d.append(b)
                bal = d[-1]
                print("Available balance: " + bal)
            except IndexError:
                print("Available balance: 0")
            dr.close()
        except FileNotFoundError:
            createFile(n)

    def userTransaction(self, n):
        try:
            dt = open(n + "Trans", "r")
            print("Your past transaction {}:".format(n))
            fileSize = os.stat(n + "Trans").st_size != 0
            if fileSize != 0:
                trans = dt.read()
                print(trans)
                dt.close()
            else:
                print("You have not made a transaction yet.")
        except FileNotFoundError:
            createFile(n)
