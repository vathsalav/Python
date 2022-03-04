from entities.account import Account

from abc import ABC, abstractmethod


class AccountDAOInterface(ABC):
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
    def update_account_balance(self, balance: float) -> Account:
        pass

    #delete
    @abstractmethod
    def delete_account_by_id(self, account_id: int) -> bool:
        pass



