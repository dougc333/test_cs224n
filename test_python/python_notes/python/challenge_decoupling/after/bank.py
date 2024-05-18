from dataclasses import dataclass
from decimal import Decimal
from stripe_service import StripePaymentService


@dataclass
class SavingsAccount:
    account_number: str
    balance: Decimal


@dataclass
class CheckingAccount:
    account_number: str
    balance: Decimal


class BankService:
    payment_service: StripePaymentService
    checking_account: CheckingAccount
    savings_account: SavingsAccount

    def __init__(self, stripePaymentService: StripePaymentService, checking_account: CheckingAccount, savings_account: SavingsAccount):
        self.payment_service = stripePaymentService
        self.payment_service.set_api_key("sk_test_1234567890")
        self.checking_account = checking_account
        self.savings_account = savings_account

    def deposit(
        self, amount: Decimal, account: SavingsAccount | CheckingAccount
    ) -> None:
        if isinstance(account, SavingsAccount):
            print(
                f"Depositing {amount} into Savings Account {account.account_number}.")
            self.savings_account.balance += amount
        else:
            print(
                f"Depositing {amount} into Checking Account {account.account_number}."
            )
            self.checking_account.balance += amount

        # self.payment_service.set_api_key("sk_test_1234567890")
        self.payment_service.process_payment(amount)
        # Balance is part of checking accuont and saavings account
        # th checking and savings account balance has to be incremented
        # self.account.balance += amount

    def withdraw(
        self, amount: Decimal, account: SavingsAccount | CheckingAccount
    ) -> None:
        if isinstance(account, SavingsAccount):
            print(
                f"Withdrawing {amount} from Savings Account {account.account_number}."
            )
            if amount >= self.savings_account.balance:
               # self.payment_service.set_api_key("sk_test_1234567890")
                self.payment_service.process_payout(amount)
                self.savings_account.balance -= amount
            else:
                print("insufficient balance")
        else:
            print(
                f"Withdrawing {amount} from Checking Account {account.account_number}."
            )
            if amount >= self.checking_account.balance:
               # self.payment_service.set_api_key("sk_test_1234567890")
                self.payment_service.process_payout(amount)
                self.checking_account.balance = - amount

            else:
                print("insufficient balance")
