import re
def pattern_check(password):
    pattern=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=!]).{8,}$'
    return re.findall(pattern,password)

def result(pwd):
    for i in pwd:
        if pattern_check(i):
            print('It is a Strong Password! ',i)
        else:
            print('It is not strong password. ',i)

def main():
    passwords = [
        "Pass123!",
        "weakpass",
        "Admin@123",
        "12345678",
        "StrongPass1$"
    ]
    result(passwords)

main()