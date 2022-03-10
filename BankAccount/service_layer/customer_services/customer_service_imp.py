from abc import ABC

from custom_exception.bad_customer_name import BadCustomerName
from custom_exception.bad_customer_name_length import BadCustomerNameLength
from custom_exception.id_not_found import IdNotFound
from dal_layer.customer_dao_interface import CustomerDAOInterface
from entities.customer import Customer
from service_layer.customer_services.customer_service_interface import CustomerServiceInterface


class CustomerServiceImp(CustomerServiceInterface, ABC):

    def __init__(self, customer_dao: CustomerDAOInterface):
        self.customer_dao = customer_dao

    def service_create_customer(self, customer: Customer) -> Customer:
        if type(customer.first_name) != str or type(customer.last_name) != str:
            print(type(customer.last_name))
            raise BadCustomerName("Please enter a valid Name")
        elif len(customer.first_name) > 20:
            raise BadCustomerName("First name too long")
        elif len(customer.last_name) > 20:
            raise BadCustomerName("Last name too long")
            return self.customer_dao.create_customer(customer)

    def service_delete_customer_by_id(self, customer_id: int) -> bool:
        if type(customer_id) == int:
            return self.customer_dao.delete_customer_by_id(customer_id)
        else:
            raise IdNotFound("Please provide a valid customer id")
