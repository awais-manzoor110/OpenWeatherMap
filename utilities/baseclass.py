# use the setup method at base class
import inspect
import logging
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def invisibility_of_loader(self):
        # Explicit wait
        wait = WebDriverWait(self.driver, 20, poll_frequency=5)
        wait.until(expected_conditions.invisibility_of_element_located((By.CLASS_NAME, 'owm-loader')))

    def click_element(self, text):
        target_element = self.driver.find_element(By.XPATH, text)
        self.driver.execute_script("arguments[0].click();", target_element)

    def get_logger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        filehandler = logging.FileHandler("C:/Myfiles/manafah_financing_v2/manafa_scripts/reports/logFile.log", encoding='utf-8')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s ")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger