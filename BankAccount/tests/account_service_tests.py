from custom_exception.id_not_found import IdNotFound
from entities.account import Account
from service_layer.account_services.account_service_imp import AccountServiceImp

account_service = AccountServiceImp()

test_service_account1 = Account(0, "Sam", "Raj", 1, 1000.00)
test_service_account2 = Account(0, "Sowri", "sri", 2, 150.00)
test_service_account3 = Account(3, "Aswin", "Ram", 3, 500.00)
test_service_account4 = Account(0, "Arun", " kumar",4, 400.00)
test_service_account5 = Account(0, "Balaji", "Kann", 5, 700.00)
test_service_account6 = Account(0, "Sree", "Nidhi", 6, 1500.00)
test_service_account7 = Account(0, "Sree", "Niketh", 7, 100.00)
test_service_account8 = Account(0, "Shyam", "sri", 8, 1000.00)
test_service_account9 = Account(0, "ram", "sam", 9, 100.00)
test_service_account10 = Account(0, "shiv", "raj", 10, 800.00)


account_service.account_list.append(test_service_account1)
account_service.account_list.append(test_service_account2)
account_service.account_list.append(test_service_account3)
account_service.account_list.append(test_service_account4)
account_service.account_list.append(test_service_account5)
account_service.account_list.append(test_service_account6)
account_service.account_list.append(test_service_account7)
account_service.account_list.append(test_service_account8)
account_service.account_list.append(test_service_account9)
account_service.account_list.append(test_service_account10)

# Create

def test_create_service_account_success():
    result = account_service.service_create_account(test_service_account1)
    assert result.account_id != 0

def test_catch_service_non_unique_id():
    result = account_service.service_create_account(test_service_account2)
    assert result.account_id != 1


#
# #Read
#
def test_get_account_info_by_customer_id_success():
    result = account_service.service_get_account_info_by_customer_id(0)
    assert result.customer_id == 0
# 3#
def test_get_account_info_by_non_existant_customer_id():
    try:
        account_service.service_get_account_info_by_customer_id(100)
        assert False
    except IdNotFound as e:
        assert str(e) == "No account for the customer"

#Update
def test_deposit_service_update_account_success():
    new_balance = account_service.deposit_service_update_account(5, 20.00)
    assert new_balance == 720.00

def test_deposit_service_update_account_for_non_existant_id():
    try:
        account_service.deposit_service_update_account(27, 30.00)
    except IdNotFound as e:
        assert str(e) == "Invalid Transaction"

#
#
def test_withdrawal_service_update_account_success():
    new_balance = account_service.withdrawal_service_update_account(6, 300.00)
    assert new_balance == 1200.00
#
def test_withdrawal_service_update_account_for_insufficient_funds():
    try:
        account_service.withdrawal_service_update_account(7, 1000.00)
    except IdNotFound as e:
        assert str(e) == "Insufficient balance"
#
def test_transfer_service_update_account_success():
    result = account_service.transfer_service_update_account(9, 10, 100.00)
    assert result == 0

def test_transfer_service_update_account_for_invalid_account_id():
    try:
        account_service.transfer_service_update_account(23, 20, 100.00)
    except IdNotFound as e:
        assert str(e) == "Please enter valid account id"

#
#
#Delete

def test_delete_service_account_by_id_success():
    result = account_service.service_delete_account_by_id(8)
    assert result

def test_delete_service_account_by_non_existant_id():
    try:
        account_service.service_delete_account_by_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No account info for the id"

