from abc import ABC, abstractmethod

from entities.account import Account


class AccountServiceInterface(ABC):
    #create
    @abstractmethod
    def create_account(self, account: Account) -> Account:
        pass

    #read
    @abstractmethod
    def get_account_info_by_id(self, account_id: int) -> Account:
        pass

    #update
    @abstractmethod
    def update_account_balance(self, account: Account) -> Account:
        pass

    #delete
    @abstractmethod
    def delete_account_by_id(self, account_id: int) -> bool:
        pass