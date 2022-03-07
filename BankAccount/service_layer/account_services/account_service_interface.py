from abc import ABC, abstractmethod

from entities.account import Account


class AccountServiceInterface(ABC):
    # create
    @abstractmethod
    def service_create_account(self, account: Account) -> Account:
        pass

    # read
    @abstractmethod
    def service_get_account_info_by_customer_id(self, account_id: int) -> Account:
        pass

    # update
    @abstractmethod
    def deposit_service_update_account(self, account_id: int, deposit_amount: float, balance: float) -> Account:
        pass

    @abstractmethod
    def withdrawal_service_update_account(self, account_id: int, withdrawal_amount: float, balance: float) -> Account:
        pass

    @abstractmethod
    def transfer_service_update_account(self, account_id: int, transfer_account_id: int, transfer_amount: float) -> Account:
        pass

    # delete
    @abstractmethod
    def service_delete_account_by_id(self, account_id: int) -> bool:
        pass
