# Login Page Class

# Responsibility ->
# get username and send keys - email
#  get password and send keys - email
#  click the submit button and navigate to dashboard Page
# Invalid -> error message
# Forgot password

#   Page class
# The page class contains the page Locators, Page Action, WebDriver init,Custom FUnction
# but not the Assertion


from selenium.webdriver.common.by import By


class LoginPage():
    def __init__(self, driver):
        self.driver = driver

        # Page Locators

    username = (By.ID, "login-username")
    password = (By.NAME, "password")
    submit_button = (By.XPATH, "//button[@id='js-login-btn']")
    # forgot_password_button = (By.XPATH, "//button[normalize-space()='Forgot Password?']")
    error_message = (By.CSS_SELECTOR, "#js-notification-box-msg")
    free_trail = (By.XPATH, "//a[normalize-space()='Start a free trial']")

    # sso_login = (By.XPATH, "//button[normalize-space()='Sign in using SSO']")
    # remember_checkbox = (By.XPATH, "//label[@for='checkbox-remember']//span[@class='checkbox-radio-button ng-scope']//*[name()='svg']")

    # Page action

    def get_username(self):
        return self.driver.find_element(*LoginPage.username)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_submit_button(self):
        return self.driver.find_element(*LoginPage.submit_button)

    def get_error_message(self):
        return self.driver.find_element(*LoginPage.error_message)

    def get_free_trail(self):
        return self.driver.find_element(*LoginPage.free_trail)

    # Page Action - Main Action

    def login_to_vmo(self, usr, pwd):
        self.get_username().send_keys(usr)
        self.get_password().send_keys(pwd)
        self.get_submit_button().click()

    def get_error_message_text(self):
        return self.get_error_message().text

    def click_free_trail(self):
        self.get_free_trail().click()

