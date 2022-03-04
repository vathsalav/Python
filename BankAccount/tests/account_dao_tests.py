from custom_exception.id_not_found import IdNotFound
from custom_exception.insufficient_funds import InsufficientFunds
from dal_layer.account_dao_imp import AccountDAOImp
from entities.account import Account

account_dao = AccountDAOImp()


# Create

def test_create_account_success():
    test_account = Account(0, "sash", "Smrith", 27, 100.00)
    result = account_dao.create_account(test_account)
    assert result.account_id != 0


def test_catch_non_unique_id():
    test_account = Account(1, "sash", "smrith", 1, 100.00)
    result = account_dao.create_account(test_account)
    assert result.account_id != 1


# Read

def test_get_account_info_by_id_success():
    result = account_dao.get_account_info_by_id(1)
    assert result.account_id == 1


def test_get_account_using_non_existant_id():
    try:
        account_dao.get_account_info_by_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No Account info for the id"


# Update

def test_update_account_balance_success():
    new_balance = Account(1, "Sash", "Smrith", 1, 200.00)
    result = account_dao.update_account_balance(new_balance)
    assert result.balance == 200.00


def test_update_account_for_negative_balance():
    try:
        new_balance = Account(1, "Sash", "Smrith", 1, -100)
        account_dao.update_account_balance(new_balance)
        assert False
    except InsufficientFunds as e:
        assert str(e) == "you don't have enough balance"


# Delete
def test_delete_account_by_id_success():
    result = account_dao.delete_account_by_id(1)
    assert result


def test_delete_account_by_non_existant_id():
    try:
        account_dao.delete_account_by_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No Account info for the id"
