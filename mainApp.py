import os
import json
from datetime import date


def main_menu():
    print("1. Input cost")
    print("2. Statistics")
    ans = input("please choose 1 or 2 (0 for exit): ")

    if ans == "0":
        exit()

    if ans == "2":
        print("\n1. Show costs per month\n"
              + "2. Show costs per month per day\n"
              + "3. Show costs per month per cost category\n"
              + "4. Show costs per month per day per cost category")


def getLastEntryMonth(filename):
    with open(filename, "r") as f:
        data = json.load(f)
        sorted_dates = sorted(data.keys())
        # print(sorted_dates)
        d = date.fromisoformat(sorted_dates[-1])
        # print(d.isoformat())

    return d.strftime("%B")


def runApp():
    cur_month = date.today().strftime("%B")

    if os.path.isfile("account.json"):
        # get last entry's month
        last_entry_month = getLastEntryMonth("account.json")

        # check if current month is last entry's month
        if cur_month != last_entry_month:
            print("The current month is ", cur_month)
            target = input("Please give me the target expenses for "
                           + cur_month + ": ")
    else:
        print("Welcome to wallet hero!")
        name = input("Please could you share your name? ")
        print(name + ", the current month is ", cur_month)
        target = input(name + ", please give me the target expenses for "
                       + cur_month
                       + ": ")

        # TODO create account object

        # create account.json
        # TODO write dictionary object of the account
        with open("account.json", "w") as f:
            json.dump({date.today().isoformat(): []}, f, indent=2)

    main_menu()


if __name__ == "__main__":
    runApp()
