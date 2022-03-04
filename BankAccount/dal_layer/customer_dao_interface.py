from entities.customer import Customer

from abc import ABC, abstractmethod


class CustomerDAOInterface(ABC):
    # create
    @abstractmethod
    def create_customer(self, customer: Customer) -> Customer:
        pass

    # delete
    @abstractmethod
    def delete_customer_by_id(self, customer_id: int) -> bool:
        pass
