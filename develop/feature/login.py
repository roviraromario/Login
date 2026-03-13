login = "yes"

while login == "yes":
    username = input("Write your username: ")

    correo = input("Write your correo: ")

    if len(correo) >= 4:
        for character in correo:
            if correo.startswith("@"):
                print("correo cannot start with @")
            if correo.startswith("."):
                print("correo cannot start with dot")

        if correo.count("@") > 1 or correo.count(".") > 1 or correo.count("@") == 0 or correo.count(".") == 0:
            print("your correo must contain @ and .")

        if "@." in correo:
            print("@ and . cannot be together")

    else:
        print("correo must have at least 4 characters")

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
