from selenium import webdriver
# from selenium.webdriver.common.service import Service
import pytest

@pytest.fixture()
def setup(browser):
      if browser == 'chrome':
            driver = webdriver.Chrome()
            print("*****Launching chrome browser***********")

      elif browser == "firefox":
            driver =webdriver.Firefox()
            print("******launching firefox browser************")

      else:
            driver =webdriver.Chrome()

      return driver

########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Pavan'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


def pytest_addoption(parser): #This will get the value from CLI/hooks
      parser.addoption("--browser")

@pytest.fixture()
def browser(request): #This will return the browser value to setup method
      return request.config.getoption("--browser")



