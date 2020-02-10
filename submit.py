import random

# challenge
def password():
    p = input("Enter password: ")
    ln = len(p)
    lower = False
    upper = False
    special = False

    if ln < 6 or ln > 16:
        print("bad password")
        return

    for c in p:
        if 97 <= ord(c) <= 122:
            lower = True
        if 65 <= ord(c) <= 90:
            upper = True
        if ord(c) == 35 or ord(c) == 36 or ord(c) == 44:
            special = True

    if(lower and upper and special):
        print("valid password")
    else:
        print("bad password")
