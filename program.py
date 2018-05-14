import datetime

def print_header():
    print("-------------------------------------")
    print("          BIRTHDAY CHECK")
    print("-------------------------------------")


def get_birthday():
    print("When were you born? ")
    year = int(input("Year [YYYY]: "))
    month = int(input("Month [MM]: "))
    day = int(input("Day [DD]: "))

    bday = datetime.date(year, month, day)
    return bday


def get_date_difference():
    pass


def print_birthday_info():
    pass


def main():
    print_header()
    bday = get_birthday()
    print(bday)
    now = None
    days = get_date_difference(bday, now)
    print_birthday_info(days)


main()