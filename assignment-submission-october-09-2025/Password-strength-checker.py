# Password Strength Checker

import re

def check_password_strength(password):
    strength = 0
    remarks = ""

    # Criteria
    if len(password) >= 8:
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"\d", password):
        strength += 1
    if re.search(r"[@$!%*?&]", password):
        strength += 1

    # Rating logic
    if strength == 5:
        remarks = "Excellent! Very strong password."
    elif strength == 4:
        remarks = "Strong password."
    elif strength == 3:
        remarks = "Moderate. Could be stronger."
    elif strength == 2:
        remarks = "Weak. Add more complexity."
    else:
        remarks = "Very weak. Please choose a better password."

    return remarks


def main():
    print("Password Strength Checker")
    print("Type 'exit' to quit.\n")

    while True:
        pwd = input("Enter password: ")
        if pwd.lower() == 'exit':
            print("Goodbye!")
            break
        print(check_password_strength(pwd), "\n")

main()
