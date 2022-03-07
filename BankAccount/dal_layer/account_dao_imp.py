from abc import ABC

from custom_exception.id_not_found import IdNotFound
from custom_exception.insufficient_funds import InsufficientFunds
from dal_layer.account_dao_interface import AccountDAOInterface
from entities.account import Account


class AccountDAOImp(AccountDAOInterface, ABC):
    account_list = []
    def __init__(self):
        account_needed_for_id_catch = Account(1, "Sash", "Smrith", 1, 100.00)
        self.balance = account_needed_for_id_catch.balance
        self.id_generator = 2
        self.account_list.append(account_needed_for_id_catch)

    def create_account(self, account: Account) -> Account:
        account.account_id = self.id_generator
        self.account_list.append(account)
        self.id_generator += 10
        return account

    def get_account_info_by_id(self, account_id: int) -> Account:
        for account in self.account_list:
            if account.account_id == account_id:
                return account
        raise IdNotFound("No Account info for the id")

    def update_account_balance(self, balance: Account) -> Account:
        for current_account in self.account_list:
            if current_account.account_id == balance.account_id:
                current_account.balance = balance.balance
                return balance
        raise IdNotFound("you don't have enough balance")

    def delete_account_by_id(self, account_id: int) -> bool:
        for account in self.account_list:
            if account.account_id == account_id:
                self.account_list.remove(account)
                return True
        raise IdNotFound("No Account info for the id")
