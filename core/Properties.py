from enum import Enum

class Properties:
    FECHAR_BROWSER = False

    Browsers = Enum('CHROME', 'FIREFOX')
    BROWSER = Browsers.CHROME

