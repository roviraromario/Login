login = "yes"

while login == "yes":
    username = input("Write your username: ")

    email = input("Write your email: ")

    if len(email) >= 4:
        for character in email:
            if email.startswith("@"):
                print("email cannot start with @")
            if email.startswith("."):
                print("email cannot start with dot")

        if email.count("@") > 1 or email.count(".") > 1 or email.count("@") == 0 or email.count(".") == 0:
            print("your email must contain @ and .")

        if "@." in email:
            print("@ and . cannot be together")

    else:
        print("email must have at least 4 characters")

    user_password = input(f"Write your password {username}: ")

    has_special_character = 0
    has_number = 0
    has_uppercase = 0

    if len(user_password) >= 8:
        print("password has 8 characters")

        for password in user_password:
            if password.isdigit():
                has_number += 1

            if password.isupper():
                has_uppercase += 1

            if password.isalnum():
                has_special_character += 1

        if has_number == 0:
            print("your password does not contain numbers")

        elif has_uppercase == 0:
            print("your password does not contain uppercase letters")

        elif has_special_character == 0:
            print("your password does not contain special characters")

        else:
            print("login successful")

        login = "no"

    else:
        print("your password does not have 8 characters")
        login = input("do you want to try again: ")
