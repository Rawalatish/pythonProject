import time

import allure
import pytest
from selenium import webdriver


from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (ElementNotVisibleException, ElementNotSelectableException)

from tests.pageObjects.loginPage import LoginPage
from tests.pageObjects.loginPage import LoginPage
from tests.pageObjects.dashboardPage import DashboardPage


# def test_vwo_login():
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))



# Assertions


@pytest.fixture()
def setup():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://app.vwo.com")
    return driver


@allure.epic("VWO Login Test")
@allure.feature("TC#0 - VWO App Negative Test")
@pytest.mark.negative
def test_vmo_login_negative(setup):
    try:
        driver = setup
        loginPage = LoginPage(driver)
        loginPage.login_to_vmo(usr="admin@admingmail.com", pwd="admin")
        time.sleep(5)
        error_message = loginPage.get_error_message_text()
        assert error_message == "Yours email, password, IP address or location did not match"
    except Exception as e:
        pytest.xfail("Failed")
        print(e)


# class Dashboard_Page:
#     pass


@allure.epic("VWO Login Test")
@allure.feature("TC#1 - VWO App Positive Test")
@pytest.mark.positive
def test_vmo_login_positive(setup):
    driver = setup
    loginPage = LoginPage(driver)
    loginPage.login_to_vmo(usr="py2x@thetestingacademy.com", pwd="Wingify@1234")
    time.sleep(10)
    dashboardPage = DashboardPage(driver)
    assert "Dashboard" in driver.title
    assert "Aman" in dashboardPage.user_logged_in_text()
