from abc import ABC, abstractmethod

from entities.customer import Customer


class CustomerServiceInterface(ABC):

    @abstractmethod
    def service_create_customer(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def service_delete_customer_by_id(self, customer: Customer) -> bool:
        pass
