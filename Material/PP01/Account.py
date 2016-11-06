class Account():
    def __init__(self, money=0):
        self.money = money
    def print_deposit(self):
        if self.money != 0:
            print("I have " + str(self.money) + "!")
        else:
            print("You have no money HaHa!!")
    def deposit(self, money):
        self.money = self.money + money
    def withdraw(self, money):
        if self.money >= money:
            self.money = self.money - money
        else:
            print("You don't have enought money")
class LimitedAccount(Account):
    def __init__(self, money, limit_money):
        super(LimitedAccount, self).__init__(money)
        self.limit_money = limit_money
    def withdraw(self, money):
        if self.money-money < self.limit_money:
            print("You need to keep at least "+str(self.limit_money)+"!!")
        else:
            self.money = self.money-money

def main():
    a1 = Account()
    a2 = LimitedAccount(limit_money=50,money=100)
    a1.print_deposit()
    a2.print_deposit()
    a1.deposit(50)
    a1.print_deposit()
    a2.withdraw(60)
    a2.print_deposit()
    a2.withdraw(50)
    a2.print_deposit()

if __name__ == '__main__':
    main()
