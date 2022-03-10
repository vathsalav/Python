from abc import ABC

from custom_exception.id_not_found import IdNotFound
from entities.account import Account

from service_layer.account_services.account_service_interface import AccountServiceInterface


class AccountServiceImp(AccountServiceInterface, ABC):
    account_list = []
    id_generator = 2

    def service_create_account(self, account: Account) -> Account:
        account.account_id = self.id_generator
        self.account_list.append(account)
        self.id_generator += 1
        return account

    def service_get_account_info_by_customer_id(self, customer_id: int) -> Account:
        for account in self.account_list:
            if account.customer_id == customer_id:
                return account
        raise IdNotFound("No account for the customer")

    def deposit_service_update_account(self, account_id: int, deposit_amount: float) -> float:
        for current_account in self.account_list:
            if current_account.account_id == account_id:
                current_account.balance += deposit_amount
                return current_account.balance
        raise IdNotFound("Invalid Transaction")

    def withdrawal_service_update_account(self, account_id: int, withdrawal_amount: float) -> float:
        for current_account in self.account_list:
            if current_account.account_id == account_id:
                if current_account.balance > withdrawal_amount:
                    current_account.balance -= withdrawal_amount
                    return current_account.balance
                else:
                    raise IdNotFound("Insufficient balance")

    def transfer_service_update_account(self, account_id: int, transfer_account_id: int, transfer_amount: float) -> Account:
        for current_account in self.account_list:
            if current_account.account_id == account_id:
                if current_account.balance >= transfer_amount:
                    current_account.balance -= transfer_amount
                    transfer_account_id.balance += transfer_amount
                    return current_account.balance
                else:
                    raise IdNotFound("Please enter valid account id")


    def service_delete_account_by_id(self, account_id: int) -> bool:
        for account in self.account_list:
            if account.account_id == account_id:
                self.account_list.remove(account)
                return True
        raise IdNotFound("No account info for the id")
