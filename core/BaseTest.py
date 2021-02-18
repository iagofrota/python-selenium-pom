import unittest
from time import sleep
from core.DriverFactory import DriverFactory

class BaseTest(unittest.TestCase):
    @classmethod
    def tearDown(self):
        sleep(5)
        DriverFactory.getDriver().quit()