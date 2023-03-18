from user import PyUser

def login():
    userId = str(input('id : '))
    userPswd = str(input('password : '))
    res = user.userLogin(userId, userPswd)
    return res
    
def signup():
    userId = str(input('id : '))
    userMAIL = str(input('email : '))
    userPswd = str(input('password : '))
    res = user.userSignup(userId, userMAIL, userPswd)
    return res

user = PyUser()

while True:
    print('[1] Login\n[2] Sign up')
    n = int(input('Enter a number : '))
    if n == 1:
        res = login()
        print(f'LOGIN : {res}\n')
        if res == "success":
            break
    elif n == 2:
        res = signup() 
        print(f'SIGN UP : {res}\n')
        if res == "success":
            break