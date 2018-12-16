import os
import sys
import json
from datetime import date


class WalletHeroApp:

    def getLastEntryMonth(self, filename):
        with open(filename, "r") as f:
            data = json.load(f)
            sorted_dates = sorted(data.keys())
            # print(sorted_dates)
            d = date.fromisoformat(sorted_dates[-1])
            # print(d.isoformat())

        return d.strftime("%B")

    def runApp(self):
        cur_month = date.today().strftime("%B")

        if os.path.isfile("account.json"):
            # get last entry's month
            last_entry_month = self.getLastEntryMonth("account.json")

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

        self.main_menu()

    def main_menu(self):
        # Main loop
        while True:
            ans = self.top_menu()

            if ans == "0":
                exit()
            elif ans == "1":
                # TODO implement input cost
                raise NotImplementedError()
            elif ans == "2":
                ans = self.statistics_sub_menu()

                if ans == "0":
                    exit()
                elif ans == "1":
                    # TODO implement costs per month
                    raise NotImplementedError()
                elif ans == "2":
                    # TODO implement costs per month per day
                    raise NotImplementedError()
                elif ans == "3":
                    # TODO implement costs per month per cost category
                    raise NotImplementedError()
                elif ans == "4":
                    # TODO implement costs per month per day per cost category
                    raise NotImplementedError()
                elif ans == "5":
                    continue
                else:
                    print(ans + " is not an available choice. Chose again.")
                    ans = self.statistics_sub_menu()
            else:
                print(ans + " is not an available choice. Chose again.")

    def clear_screen(self):
        if sys.platform == "win32":
            os.system('cls')
        else:
            os.system('clear')

    def top_menu(self):
        self.clear_screen()
        print("1. Input cost")
        print("2. Statistics")
        return input("please chose 1 or 2 (0 for exit): ")

    def statistics_sub_menu(self):
        self.clear_screen()
        print("1. Show costs per month\n"
              + "2. Show costs per month per day\n"
              + "3. Show costs per month per cost category\n"
              + "4. Show costs per month per day per cost category\n"
              + "5. Back")
        return input("please chose from the above (0 for exit): ")


if __name__ == "__main__":
    WalletHeroApp().runApp()
