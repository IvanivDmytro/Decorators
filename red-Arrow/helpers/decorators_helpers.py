
def is_email_valid(func):
    def wrapper(email, y, a, z):
        if "@" in email:
            if "." in email.split("@")[1]:
                func(email, y, a, z)
            else:
                print("Email invalid without dot!!!!")
        else:
            print("Email invalid without @ !!!!")
    return wrapper


def error_phone_number(func):
    def wrapper(x, y, a, phone):
        if len(phone) != 10:
            print("error phone number!")
        else:
            func(x, y, a, phone)

    return wrapper