
class StatisticEric:
    def __init__(self, values):
        self.values = values

    def count(self):
        return len(self.values)

    def sum(self):
        return sum(self.values)

    def min(self):
        return min(self.values)

    def max(self):
        return max(self.values)

    def range(self):
        range_values = max(self.values) - min(self.values)
        return range_values

    def mean(self):
        average = sum(self.values) / len(self.values)
        return average

    def median(self):
        sorted_median = sorted(self.values)
        median_e = len(self.values) // 2
        return sorted_median[median_e]

    def mode(self):
        mode_e = max(set(self.values), key=self.values.count)
        mode_dict = {
            'mode': mode_e,
            'count': self.values.count(mode_e)
        }
        return mode_dict

    def std(self):
        std_e = (sum((x-(sum(self.values) / len(self.values)))**2 for x in self.values) / (len(self.values)-1))**0.5
        return "{:.2f}".format(std_e)

    def var(self):
        mean = sum(self.values) / len(self.values)
        res = sum((i - mean) ** 2 for i in self.values) / len(self.values)
        return "{:.2f}".format(res)

    def freq_dist(self):
        set_values = set(self.values)
        result_list = []
        for e in set_values:
            result_list.append(((self.values.count(e)/len(self.values))*100, e))
        return sorted(result_list, reverse=True)

    def describe(self):
        return f'Count: {self.count()}\nSum: {self.sum()}\nMin: {self.min()}\nMax: {self.max()}\n' \
               f'Range: {self.range()}\nMean: {self.mean()}\nMedian: {self.median()}\nMode: {self.mode()}\n' \
               f'Standard Deviation: {self.std()}\nVariance: {self.var()}\nFrequency Distribution: {self.freq_dist()}'


ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
# data = StatisticEric(ages)
# print(data.describe())


class PersonAccount:
    def __init__(self, firstname, lastname, incomes, expenses):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expenses = expenses

    def total_income(self):
        total_in = 0
        for i in self.incomes:
            total_in += i[0]
        return "{:.2f}".format(total_in)

    def total_expenses(self):
        total_ex = 0
        for e in self.expenses:
            total_ex += e[0]
        return "{:.2f}".format(total_ex)

    def account_info(self):
        print(f"This is {self.firstname} {self.lastname} account.")
        print("INCOMES")
        for i in self.incomes:
            print(f"{i[0]}\t{i[1]}")
        print("EXPENSES")
        for e in self.expenses:
            print(f"{e[0]}\t{e[1]}")

    def add_income(self, income_to_add):
        self.incomes.append(income_to_add)

    def add_expense(self, expense_to_add):
        self.expenses.append(expense_to_add)

    def account_balance(self):
        income = self.total_income()
        expense = self.total_expenses()
        balance = float(income) - float(expense)
        return "{:.2f}".format(balance)


my_first_name = 'Eric'
my_last_name = 'Sacchetto'
my_incomes = [
    [500.00, 'Company payment'],
    [3000, 'Bike sell'],
    [80.5, 'Trade Me board game']
]
my_expenses = [
    [100.00, 'Xbox game'],
    [30.28, 'Arduino Uno'],
    [10.87, 'Raspberry Pico'],
    [49.99, 'Gift to wife']
]

my_account = PersonAccount(my_first_name, my_last_name, my_incomes, my_expenses)
print(my_account.account_info())
print(my_account.total_income())
print(my_account.total_expenses())
print(my_account.account_balance())
my_account.add_expense([4000, 'New car'])
print(my_account.account_balance())
print(my_account.incomes)
print(my_account.expenses)

