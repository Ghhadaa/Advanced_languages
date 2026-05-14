import database


def admin_login():

    print("\n========== ADMIN LOGIN ==========")

    username = input("Username: ")
    password = input("Password: ")

    if database.login(username, password):

        print("\nLogin successful.")
        return True

    else:

        print("\nInvalid username or password.")
        return False