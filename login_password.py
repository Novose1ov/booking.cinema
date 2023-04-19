USER_LOGIN = []
USER_PASSWORD = []
TYPE = []

class Authentication:
    def __init__(self, login:str, password:str):
        self.login = login
        self.password = password
        USER_LOGIN.append(self.login)
        USER_PASSWORD.append(self.password)

a1 = Authentication ("admin", "admin")
u1 = Authentication ("user", "oooo")
u2 = Authentication ("123", "1233445")

if a1.login == a1.password == "admin":


print (USER_LOGIN)
print (USER_PASSWORD)
print (TYPE)