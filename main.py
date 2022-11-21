# Calcualate mortgage for codeacedemy computer science certification
from datetime import datetime
from dateutil.relativedelta import relativedelta
from tabulate import tabulate
from utils.take_input import take_input


def get_coefficient(issue_rate):
    result = (1 + issue_rate / 100) ** (1 / 12)
    return result


class MortgageTable:
    def __init__(self, amount, issue_rate, loan_term, issue_date):
        self.table = []
        self.amount = amount
        self.issue_rate = issue_rate
        self.loan_term = loan_term
        self.issue_date = issue_date
        self.coefficient = get_coefficient(issue_rate)
        self.month_amount = self.get_month_amount()
        self.calc()

    def __repr__(self) -> str:
        headers = ["date", "payment", "month %", "main", "rest"]
        return tabulate(self.table, headers, tablefmt="presto")

    def calc(self):
        rest_amount = self.amount
        for m in range(self.loan_term):
            date = self.issue_date + relativedelta(months=+m)
            month_percent_amount = self.get_month_percent_by_amount(rest_amount)
            month_main_amount = self.month_amount - month_percent_amount
            rest_amount -= month_main_amount
            self.table.append(
                [
                    date.strftime("%b %d %Y"),
                    round(self.month_amount, 2),
                    round(month_percent_amount, 2),
                    round(month_main_amount, 2),
                    round(rest_amount, 2),
                ]
            )

    def get_month_amount(self):
        month_issue_rate = self.coefficient - 1
        result = (
            self.amount
            * pow(self.coefficient, self.loan_term)
            * month_issue_rate
            / (pow(self.coefficient, self.loan_term) - 1)
        )
        return result

    def get_month_percent_by_amount(self, amount):
        month_issue_rate = self.coefficient - 1
        result = month_issue_rate * amount
        return result


def main():
    print("Wellcome to Mortgage Calculator!")
    mortgage_amount = take_input("mortgage amount", "$")
    issue_rate = take_input("interest rate", "%")
    # loan_term = years * 12 months
    loan_term = take_input(data_name="loan term", sign="", hint="years") * 12
    issue_date = datetime.today()
    mortgage = MortgageTable(mortgage_amount, issue_rate, loan_term, issue_date)
    print(mortgage)


main()
