import mock
import unittest
from src.services.account_service import AccountService


class TestAccountService(unittest.TestCase):
    """
    to mock function
    """
    from src.services.account_service import AccountDao

    # @mock.patch("src.services.account_service.AccountDao.get_accounts")
    @mock.patch("{}.{}.{}".format(AccountDao.__module__, AccountDao.__name__, AccountDao.get_accounts.__name__))
    def test_get_account_names_with_two_accounts(self, mock_get_accounts):
        mock_get_accounts.return_value = [{
            "name": "acc01"
        }, {
            "name": "acc02"
        }]
        account_names = AccountService.get_account_names()
        expect_account_names = ["acc01", "acc02"]
        self.assertEquals(expect_account_names, account_names)
