from custom_exception.id_not_found import IdNotFound
from dal_layer.customer_dao_imp import CustomerDAOImp
from entities.customer import Customer

customer_dao = CustomerDAOImp()


def test_create_customer_success():
    test_customer = Customer(1, "Vathsala", "Vijay")
    result = customer_dao.create_customer(test_customer)
    assert result.customer_id != 0


def test_catch_non_unique_id():
    test_customer = Customer(1, "Sam", "Sund")
    result = customer_dao.create_customer(test_customer)
    assert result.customer_id != 1


def test_delete_customer_by_id_success():
    result = customer_dao.delete_customer_by_id(1)
    assert result


def test_delete_customer_using_non_existant_id():
    try:
        customer_dao.delete_customer_by_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No customer info for the id"
