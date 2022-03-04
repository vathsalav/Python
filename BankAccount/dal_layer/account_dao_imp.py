from abc import ABC

from custom_exception.id_not_found import IdNotFound
from custom_exception.insufficient_funds import InsufficientFunds
from dal_layer.account_dao_interface import AccountDAOInterface
from entities.account import Account


class AccountDAOImp(AccountDAOInterface, ABC):

    def __init__(self):
        account_needed_for_id_catch = Account(1, "Sash", "Smrithi", 1, 100.00)
        self.account_list = []
        self.id_generator = 2
        self.account_list.append(account_needed_for_id_catch)

    def create_account(self, account: Account) -> Account:
        account.account_id = self.id_generator
        self.account_list.append(account)
        self.id_generator += 1
        return account

    def get_account_info_by_id(self, account_id: int) -> Account:
        for account in self.account_list:
            if account.account_id == account_id:
                return account
            raise IdNotFound("No Account info for the id")

    def update_account_balance(self, balance: float) -> Account:
        for old_balance in self.balance:
            if old_balance.balance <= 0:
                return old_balance
            raise IdNotFound("you don't have enough balance")

    def delete_account_by_id(self, account_id: int) -> bool:
        for account in self.account_list:
            if account.account_id == account_id:
                self.account_list.remove(account)
                return True
        raise IdNotFound("No Account info for the id")
