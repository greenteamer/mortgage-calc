# Calcualate mortgage for codeacedemy computer science certification
from datetime import datetime
from utils.take_input import take_input
from mortgage import MortgageTable


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
