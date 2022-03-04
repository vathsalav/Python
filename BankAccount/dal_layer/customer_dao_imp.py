from abc import ABC

from custom_exception.id_not_found import IdNotFound
from dal_layer.customer_dao_interface import CustomerDAOInterface
from entities import customer
from entities.customer import Customer


class CustomerDAOImp(CustomerDAOInterface, ABC):
    #customers_list = []
    #id_generator = 2

    def __init__(self):
        customer_needed_for_id_catch = Customer(1, "Vathsala", "Vijay")
        self.customers_list = []
        self.id_generator = 2
        self.customers_list.append(customer_needed_for_id_catch)

    def create_customer(self, customer: Customer) -> Customer:
        customer.customer_id = self.id_generator
        self.id_generator += 1
        self.customers_list.append(customer)
        return customer

    def delete_customer_by_id(self, customer_id: int) -> bool:
        for customer in self.customers_list:
            if customer.customer_id == customer_id:
                self.customers_list.remove(customer)
                return True
        raise IdNotFound("No customer info for the id")
