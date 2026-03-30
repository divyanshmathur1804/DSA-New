password = str(input("Enter your password: "))
if len(password) < 8:
    print("Your password is too short. It must be at least 8 characters long.")
if(password.isalpha()): # isalpha() checks if the string contains only letters
    print("Your password must contain at least one number.")

# creating own method to check if the password contains at least one number
def contains_number(password):
    for ch in password:
        if int(ch) >= 0 and int(ch) <= 9:
            return True