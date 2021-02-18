from selenium.webdriver.common.by import By
from core.BasePage import BasePage


class LoginPage(BasePage):
    idCampoEmail = 'txtEmail'
    idCampoSenha = 'txtSenha'
    classeBotaoAcessar = 'btnStyle'
    email = ''
    senha = ''

    def preencherCampoEmail(self):
        BasePage.dsl.escreverPorId((By.ID, self.idCampoEmail), self.email)

    def preencherCampoSenha(self):
        BasePage.dsl.escreverPorId((By.ID, self.idCampoSenha), self.senha)

    def clicarNoBotaoAcessar(self):
        BasePage.dsl.clicarNoBotao((By.CLASS_NAME, self.classeBotaoAcessar))
