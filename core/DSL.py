from selenium.webdriver.common.by import By
from core.DriverFactory import DriverFactory


class Dsl():
    def escrever(self, by: By, text: str):
        """
        Pesquisa o campo de texto e preencher com o valor informado
        
        :param by: recebe o locator
        :param text: str recebe o texto que será escrito
        """
        elemento = DriverFactory.getDriver().find_element(by)
        elemento.send_keys(text)

    def escreverPorId(self, id_field: str, text: str):
        """
        Pesquisa um campo do tipo input pelo id do campo e preenche o campo
        com o texto fornecido

        :param id_field: id do campo
        :param text: texto a ser inserido no campo
        """
        self.escrever((By.ID, id_field), text)

    def clicarNoBotao(self, by: By):
        """
        Clicar em um botão

        :param by: recebe o locator
        :return:
        """
        DriverFactory.getDriver().find_element(by).click()
