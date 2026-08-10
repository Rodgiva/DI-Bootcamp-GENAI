class BankAccount():
    def __init__(self, balance: int, username: str, password: str, authenticated: bool = False):
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated = authenticated

    def deposit(self, amount: int):
        if not self.authenticated:
            raise Exception("Operation not authorized")
        if amount < 0:
            raise Exception("The amount must be positive")
        self.balance += amount
        return self

    def withdraw(self, amount: int):
        if not self.authenticated:
            raise Exception("Operation not authorized")
        if amount < 0:
            raise Exception("The amount must be positive")
        self.balance -= amount
        return self

    def authenticate(self, username: str, password: str):
        if username == self.username and password == self.password:
            self.authenticated = True


class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance: int, username: str, password: str, minimum_balance: int = 0, authenticated: bool = False):
        super().__init__(balance, username, password, authenticated)
        self._minimum_balance = minimum_balance

    def withdraw(self, amount: int):
        if not self.authenticated:
            raise Exception("Operation not authorized")
        if amount < 0:
            raise Exception("The amount must be positive")
        if self.balance - amount < self._minimum_balance:
            raise Exception("Operation not authorized")
        self.balance -= amount
        return self


class ATM():
    def __init__(self, try_limit: int, account_list=None):
        self._current_tries = 0

        if try_limit > 0:
            self.try_limit = try_limit
        else:
            print("Invalid try_limit, defaulting to 2")
            self.try_limit = 2

        if account_list is None:
            self.account_list = []
        else:
            for account in account_list:
                if not isinstance(account, (BankAccount, MinimumBalanceAccount)):
                    raise Exception("Account is not an instance of BankAccount or MinimumBalanceAccount")
            self.account_list = list(account_list)

        self.show_main_menu()

    def show_main_menu(self):
        choice = None
        while choice != "2":
            print("1. Log in")
            print("2. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                username = input("Username: ")
                password = input("Password: ")
                self.log_in(username, password)
                if self._current_tries >= self.try_limit:
                    print("Max tries reached, the program will shut down")
                    return
            elif choice != "2":
                print("Invalid choice, try again.")

    def log_in(self, username: str, password: str):
        for account in self.account_list:
            if account.username == username and account.password == password:
                account.authenticate(username, password)
                self.show_account_menu(account)
                return
        self._current_tries += 1

    def show_account_menu(self, account):
        choice = None
        while choice != "3":
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                amount = int(input("The amount you want to deposit: "))
                account.deposit(amount)
            elif choice == "2":
                amount = int(input("The amount you want to withdraw: "))
                account.withdraw(amount)
            elif choice != "3":
                print("Invalid choice, try again.")


account_list = [
    BankAccount(500, "Bob", "1234"),
    BankAccount(800, "Avi", "1234"),
    BankAccount(700, "Ari", "1234"),
    BankAccount(5000, "Eli", "1234"),
]
an_atm = ATM(3, account_list)