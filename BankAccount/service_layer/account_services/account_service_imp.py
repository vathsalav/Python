from abc import ABC

from custom_exception.id_not_found import IdNotFound
from entities.account import Account

from service_layer.account_services.account_service_interface import AccountServiceInterface


class AccountServiceImp(AccountServiceInterface, ABC):
    account_list = []

    def __init__(self, account_dao: AccountServiceInterface):
        account_needed_for_id_catch = Account(1, "Sash", "Smrith", 1, 500.00)
        self.account_dao = account_dao
        self.balance = account_needed_for_id_catch.balance
        self.id_generator = 2
        self.account_list.append(account_needed_for_id_catch)

    def service_create_account(self, account: Account) -> Account:
        account.account_id = self.id_generator
        self.account_list.append(account)
        self.id_generator += 10
        return account

    def service_get_account_info_by_customer_id(self, customer_id: int) -> Account:
        for account in self.account_list:
            if account.customer_id == customer_id:
                return account
        raise IdNotFound("No accounts for the customer")

    def deposit_service_update_account(self, account_id: int, deposit_amount: float, balance: float) -> Account:
        for current_account in self.account_list:
            if current_account.account_id == balance.account_id:
                current_account.balance = (deposit_amount + balance).balance
                return balance
        raise IdNotFound("Invalid amount")

    def withdrawal_service_update_account(self, account_id: int, withdrawal_amount: float, balance: float) -> Account:
        pass

    def transfer_service_update_account(self, account_id: int, transfer_account_id: int) -> Account:
        pass

    def service_delete_account_by_id(self, account_id: int) -> bool:
        for account in self.account_list:
            if account.account_id == account_id:
                self.account_list.remove(account)
                return True
        raise IdNotFound("No Account info for the id")
