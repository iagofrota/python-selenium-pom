from core.BaseTest import BaseTest
from core.DriverFactory import DriverFactory


class TesteLogin(BaseTest):

    @classmethod
    def setUp(cls):
        DriverFactory.getDriver().get('')

    def test_deve_realizar_login_com_sucesso(self):
        pass

    def test_deve_realizar_login_sem_sucesso(self):
        pass

    def test_deve_realizar_login_e_logou_com_sucesso(self):
        pass
