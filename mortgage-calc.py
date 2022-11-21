# Calcualate mortgage for codeacedemy computer science certification
from datetime import datetime
from dateutil.relativedelta import relativedelta
from tabulate import tabulate


def take_input(data_name, sign="", hint=""):
    value = 0
    hint_text = "({})".format(hint) if hint != "" else hint
    prompt = "* Type {name}{hint}: {sign}".format(
        name=data_name, hint=hint_text, sign=sign
    )
    while value == 0:
        try:
            value = int(input(prompt))
        except ValueError:
            print("{} should be a number".format(data_name.title()))
    return value


def get_coefficient(issue_rate):
    result = (1 + issue_rate / 100) ** (1 / 12)
    return result


def get_month_amount(amount, issue_rate, loan_term):
    coefficient = get_coefficient(issue_rate)
    month_issue_rate = coefficient - 1
    result = (
        amount
        * pow(coefficient, loan_term)
        * month_issue_rate
        / (pow(coefficient, loan_term) - 1)
    )

    return result


def get_month_percent_amount(rest_amount, issue_rate):
    coefficient = get_coefficient(issue_rate)
    month_issue_rate = coefficient - 1
    result = month_issue_rate * rest_amount
    return result


def main():
    print("Wellcome to Mortgage Calculator!")
    mortgage_amount = take_input("mortgage amount", "$")
    issue_rate = take_input("interest rate", "%")

    # loan_term = years * 12 months
    loan_term = take_input(data_name="loan term", sign="", hint="years") * 12

    issue_date = datetime.today()
    print(issue_date)
    month_amount = get_month_amount(mortgage_amount, issue_rate, loan_term)
    rest_amount = mortgage_amount

    table = []

    for m in range(loan_term):
        issue_date += relativedelta(months=+1)
        month_percent_amount = get_month_percent_amount(rest_amount, issue_rate)
        month_main_amount = month_amount - month_percent_amount
        rest_amount = rest_amount - month_main_amount

        table.append(
            [
                issue_date.strftime("%b %d %Y"),
                round(month_amount, 2),
                round(month_percent_amount, 2),
                round(month_main_amount, 2),
                round(rest_amount, 2),
            ]
        )
    headers = ["date", "payment", "month %", "main", "rest"]
    print(tabulate(table, headers, tablefmt="presto"))


main()
