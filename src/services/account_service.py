from src.dao.account_dao import AccountDao


class AccountService(object):
    @staticmethod
    def get_account_names():
        accounts = AccountDao.get_accounts()
        return [account["name"] for account in accounts]
