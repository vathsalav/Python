from abc import ABC

from custom_exception.bad_customer_firstname import BadCustomerFirstname
from custom_exception.bad_customer_lastname import BadCustomerLastname
from custom_exception.id_not_found import IdNotFound
from dal_layer.customer_dao_interface import CustomerDAOInterface
from entities.customer import Customer
from service_layer.customer_services.customer_service_interface import CustomerServiceInterface


class CustomerServiceImp(CustomerServiceInterface, ABC):

    def __init__(self, customer_dao: CustomerDAOInterface):
        self.customer_dao = customer_dao

    def service_create_customer(self, customer: Customer) -> Customer:
        if type(customer.first_name) != str:
            raise BadCustomerFirstname("Please enter a valid Firstname")
        elif len(customer.first_name) > 20:
            raise BadCustomerFirstname("Please enter a valid FirstName")
        elif type(customer.last_name) != str:
            raise BadCustomerLastname("Please enter a valid Lastname")
        elif len(customer.last_name) > 20:
            raise BadCustomerLastname("Please enter a valid Lastname")
        return self.customer_dao.create_customer(customer)

    def service_delete_customer_by_id(self, customer_id: int) -> bool:
        if type(customer_id) == int:
            return self.customer_dao.delete_customer_by_id(customer_id)
        else:
            raise IdNotFound("Please provide a valid customer id")