from dateutil.relativedelta import relativedelta
from tabulate import tabulate
from datetime import datetime
from typing import Tuple


def get_coefficient(issue_rate: int) -> float:
    exp = 1 / 12
    base = 1 + issue_rate / 100
    result: float = pow(base, exp)
    return result


class MortgageTable:
    table: list[Tuple[str, float, float, float, float]] = []

    def __init__(
        self,
        amount: float,
        issue_rate: int,
        loan_term: int,
        issue_date: datetime,
    ):
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

    def calc(self) -> None:
        rest_amount = self.amount
        for m in range(self.loan_term):
            date = self.issue_date + relativedelta(months=+m)
            month_percent_amount = self.get_month_percent_by_amount(rest_amount)
            month_main_amount = self.month_amount - month_percent_amount
            rest_amount -= month_main_amount
            new_row = (
                date.strftime("%b %d %Y"),
                round(self.month_amount, 2),
                round(month_percent_amount, 2),
                round(month_main_amount, 2),
                round(rest_amount, 2),
            )
            self.table.append(new_row)

    def get_month_amount(self) -> float:
        month_issue_rate = self.coefficient - 1
        result = (
            self.amount
            * pow(self.coefficient, self.loan_term)
            * month_issue_rate
            / (pow(self.coefficient, self.loan_term) - 1)
        )
        return result

    def get_month_percent_by_amount(self, amount: float) -> float:
        month_issue_rate = self.coefficient - 1
        result = month_issue_rate * amount
        return result
