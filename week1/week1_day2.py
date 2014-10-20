from itertools import combinations


class CashDesk:

    def __init__(self):
        self.money = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}

    def take_money(self, notedict):
        for i in notedict:
            if i in self.money:
                self.money[i] += notedict[i]
            else:
                print("Nqma para sus stoinost" + str(i))

    def total(self):
        totalsum = 0
        for i in self.money:
            totalsum += i * self.money[i]
        return totalsum

    def can_withdraw_money(self, amount_of_money):
        copy_of_money = dict(self.money)
        all_moneyzzz = []
        combinationslist = []
        for i in copy_of_money:
            for j in range(0, copy_of_money[i]):
                all_moneyzzz.append(i)
        for i in range(1, len(all_moneyzzz) + 1):
            combinationslist.append(list(combinations(all_moneyzzz, i)))
        for i in combinationslist:
            for j in i:
                if sum(j) == amount_of_money:
                    return True
        return False


class Product:

    def __init__(self, name, stockprice, finalprice):
        self.name = name
        self.stockprice = stockprice
        self.finalprice = finalprice

    def profit(self):
        return self.finalprice - self.stockprice


class Laptop(Product):

    def __init__(self, name, stockprice, finalprice,
                 diskspace, RAM):
        Product.__init__(self, name, stockprice, finalprice)
        self.diskspace = diskspace
        self.RAM = RAM


class Smartphone(Product):

    def __init__(self, name, stockprice, finalprice,
                 displaysize, megapixels):
        Product.__init__(self, name, stockprice, finalprice)
        self.displaysize = displaysize
        self.megapixels = megapixels


class Store:

    def __init__(self, name):
        self.name = name
        self.products = {}
        self.profit = 0

    def load_new_products(self, product, amount):
        if product in self.products:
            self.products[product] += 1
        else:
            self.products[product] = amount

    def list_products(self, class_product=object):
        for i in self.products:
            if isinstance(i, class_product):
                print("{} {}".format(i.name, self.products[i]))

    def sell_product(self, product):
        if product in self.products and self.products[product] > 0:
            self.products[product] -= 1
            self.profit += product.profit()
            return True
        else:
            return False

    def total_income(self):
        return self.profit


class Employee:

    def __init__(self, name):
        self.name = name


class HourlyEmployee(Employee):

    def __init__(self, name, pay_per_hour):
        Employee.__init__(self, name)
        self.pay_per_hour = pay_per_hour

    def weeklyPay(self, hours):
        if hours > 40:
            return 40 * self.pay_per_hour + (hours - 40) *\
                self.pay_per_hour * 1.5
        else:
            return hours * self.pay_per_hour


class SalariedEmployee(Employee):

    def __init__(self, name, salary):
        Employee.__init__(self, name)
        self.salary = salary

    def weeklyPay(self, hours):
        return self.salary / 48


class Manager(SalariedEmployee):

    def __init__(self, name, salary, bonus):
        SalariedEmployee.__init__(self, name, salary)
        self.bonus = bonus

    def weeklyPay(self, hours):
        return self.salary / 48 + self.bonus
