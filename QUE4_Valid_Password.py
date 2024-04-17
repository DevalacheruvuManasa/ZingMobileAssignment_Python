"""4. Validate the Password
I have an app for my employees in my company, I need my employees password to be safe, so I
want to make a Python App which says if the password is safe or no, the password is given by an
input assigned in a variable called password, it should go into the following points: 1) Minimum
8 characters.
2) The alphabets must be between [a-z]
3) At least one alphabet should be of Upper Case [A-Z]
4) At least 1 number or digit between [0-9].
5) At least 1 symbol like [ _ or @ or $ ]."""
import re#importing regular expression

def validate_password(password):
    if len(password) < 8:#checks length of passworrd is less than 8
        print("password should have more than 8 characters")
        return False

    if not re.search(r'[a-z]', password):#checks whether contains letters or not
        print("should contain small letters")
        return False

    if not re.search(r'[A-Z]', password):#checks whether contains Capital letters or not
        print("should contain capital letters")
        return False

    if not re.search(r'\d', password):#checks whether contaons digits or not
        print("should contain digits")
        return False

    if not re.search(r'[_@$]', password):#checks whether contains special characters or not
        print("contain special characters")
        return False

    return True

# Test the function
password = input("Enter your password: ")
if validate_password(password):
    print("The password is safe.")
else:
    print("The password is not safe.")