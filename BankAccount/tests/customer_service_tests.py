from custom_exception.bad_customer_name import BadCustomerName
from custom_exception.bad_customer_name_length import BadCustomerNameLength
from custom_exception.id_not_found import IdNotFound
from dal_layer.customer_dao_imp import CustomerDAOImp
from entities.customer import Customer
from service_layer.customer_services.customer_service_imp import CustomerServiceImp

customer_dao = CustomerDAOImp()
customer_service = CustomerServiceImp(customer_dao)
non_string_first_name = Customer(0, "123", "last name")
long_first_name = Customer(0, "abcdjkfjdjfjjljdjjhhjhkjljkl", "last name")
non_string_last_name = Customer(0, "first name", "678")
long_last_name = Customer(0, "first name", "fdjhshkjhhfuhjdjjyjhjkhhhhhfmm")


def test_catch_non_string_first_name():
    try:
        customer_service.service_create_customer(non_string_first_name)
    except BadCustomerName as e:
        assert str(e) == "Please enter a valid Name"


def test_catch_long_first_name():
    try:
        customer_service.service_create_customer(long_first_name)
    except BadCustomerName as e:
        assert str(e) == "First name too long"


def test_catch_non_string_last_name():
    try:
        customer_service.service_create_customer(non_string_last_name)
    except BadCustomerName as e:
        assert str(e) == "Please enter a valid Name"


def test_catch_long_last_name():
    try:
        customer_service.service_create_customer(long_last_name)
        assert False
    except BadCustomerName as e:
        assert str(e) == "Last name too long"


def test_catch_non_numeric_id_delete_customer():
    try:
        customer_service.service_delete_customer_by_id("one")
        assert False
    except IdNotFound as e:
        assert str(e) == "Please provide a valid customer id"
