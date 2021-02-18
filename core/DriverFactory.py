from core.Properties import Properties
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class DriverFactory:

    @staticmethod
    def getDriver(self):
        if self.__driver == None:
            if Properties.BROWSER == 'CHROME':
                self.__driver = webdriver.Chrome(ChromeDriverManager().install())
            elif Properties.BROWSER == 'FIREFOX':
                self.__driver = webdriver.Firefox(GeckoDriverManager().install())

            self.__driver.set_window_size(1200, 765)

        return self.__driver

    def killDriver(self):
        if self.__driver != None:
            self.__driver.quit()
            self.__driver = None