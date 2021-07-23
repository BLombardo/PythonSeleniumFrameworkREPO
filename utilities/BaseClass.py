import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def verifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def getLogger(self):

        loggerName = inspect.stack()[1][3] # gets the name of the class that logging is being used for
        logger = logging.getLogger(str(loggerName))

        fileHandler = logging.FileHandler('logfile.log')  # set log file name
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")  # set log format in C code
        fileHandler.setFormatter(formatter)  # pass format to file handeler

        if (logger.hasHandlers()):
            logger.handlers.clear()
        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.INFO)  # will send all logs levels 3 and up

        #use these commands in the test case to add log entries
        #logger.debug("A debug statement is executed")  # 1 lowest severity
        #logger.info("Information statement")  # 2
        #logger.debug("A debug statement is executed")  # 3
        #logger.warning("Something is in warning mode")  # 4
        #logger.error("A Major error has happend")  # 5
        #logger.critical("Critical issue")  # 6 highest severity

        return logger