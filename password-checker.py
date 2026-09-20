# Simple Password Strength Checker
# By GHOST_IN_SHELL

def check_password(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in "!@#$%^&*" for c in password):
        score += 1
    
    if score == 4:
        return "Strong Password"
    elif score == 3:
        return "Medium Password"
    else:
        return "Weak Password"

pwd = input("Enter password to check: ")
print(check_password(pwd))
