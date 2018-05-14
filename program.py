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


def get_date_difference(original, target):
    year = datetime.date(target.year, original.month, original.day)
    dt = year - target
    return dt.days


def print_birthday_info(days):
    if days < 0:
        print("You've already had your birthday this year, {} days ago. Hope it was a good one!".format(-days))
    elif days > 0:
        print("Your birthday's in {} days!".format(days))
    else:
        print("Happy Birthday!")


def main():
    print_header()
    bday = get_birthday()
    today = datetime.date.today()
    days = get_date_difference(bday, today)
    print_birthday_info(days)


main()