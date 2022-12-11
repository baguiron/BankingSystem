def signup(self):
    db = open("userfile", "r")
    print("""
                        ===== Sign up =====
                """)

    name = input("Enter your username: ")
    pwd = input("Enter your password: ")
    cPwd = input("Confirm your password: ")

    n = []
    p = []
    for i in db.readlines():
        a, b = i.split(", ")
        b = b.strip()
        n.append(a)
        p.append(b)

    if pwd != cPwd:
        print("Password do not match!")
        signup(self)

    else:
        if len(pwd) <= 5:
            print("Password too short, try again.")
            signup(self)

        elif name in db.read():
            print("Username already exits!")
            db.close()
            signup(self)

        else:
            db = open("userfile", "a")
            db.write(name + ", " + pwd + "\n")
            db.close()
            print("Sign up successful!")


def login():
    db = open("userfile", "r")
    print(""" 
                            ===== Login =====
        """)

    name = input("Enter your username: ")
    pwd = input("Enter your password: ")

    if not len(name or pwd) < 1:
        n = []
        p = []
        for i in db:
            try:
                a, b = i.split(", ")
                b = b.strip()
                n.append(a)
                p.append(b)
                data = dict(zip(n, p))
            except ValueError:
                print("Error login")

        try:
            try:
                if data[name]:
                    try:
                        if pwd == data[name]:
                            print("Login success!")
                            print("Welcome {}!".format(name))
                            db.close()
                            return 1, name
                        else:
                            print("Username or Password incorrect.")
                            db.close()
                            return 0, name
                    except KeyError:
                        print("Incorrect password or username.")
                        db.close()
                        return 0, name
                else:
                    print("User not found.")
                    db.close()
                    return 0, name
            except KeyError:
                print("Incorrect password or username.")
                db.close()
                return 0, name
        except NameError:
            print("User not found.")
            db.close()
            return 0, name


class UserAccount:

    def userSignup(self):
        return signup(self)

    def userLogin(self):
        return login()
