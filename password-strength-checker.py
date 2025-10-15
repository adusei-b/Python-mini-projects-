while True:
    password = input("Enter your password ")
    has_length = len(password) >= 8
    has_number = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_symbol = any(char in "!@#$%^&*()_+}{:/.,<>" for char in password)
    if has_length and has_number and has_upper and has_symbol:
        print("your password is strong and secure!")
    else:
           print("your password is so weak try including")
    if not has_length:
        print("- At least 8 characters")
        if not has_number:
            print("At least one number")
            if not has_upper:
                print("At least one upper case letter")
                if not has_symbol:
                    print("At least one symbol (!@#$) etc.")
                    print()  # just a blank line for readability
