from selenium.webdriver.common.by import By

# Initialize the LoginPage with a driver instance
# The constructor defines the locators
class LoginPage:
    def __init__(self, driver):

        self.driver = driver
        self.username_input = By.ID, "user-name"  # Locator for the username input field
        self.password_input = By.ID, "password"   # Locator for the password input field
        self.login_button = By.ID, "login-button"  # Locator for the login button
        self.error_message = By.XPATH, "//h3[@data-test='error']"  # Locator for the error message displayed after login failure
        self.company_logo = By.CLASS_NAME, "app_logo"  # Locator for the company logo on the login page

# Clears the username input field and enters the provided username
    def enter_username(self, username):
        self.driver.find_element(self.username_input).clear()  # Clear any pre-existing text in the username field
        self.driver.find_element(self.username_input).send_keys(username)  # Enter the given username

# Clears the password input field and enters the provided password
    def enter_password(self, password):
        self.driver.find_element(self.password_input).clear()  # Clear any pre-existing text in the password field
        self.driver.find_element(self.password_input).send_keys(password)  # Enter the given password

# Simulates a click on the login button
    def click_login(self):
        self.driver.find_element(self.login_button).click()  # Click the login button to attempt to log in

# Returns the error message text when login fails
# This method is used to verify the presence of an error message after an invalid login attempt
    def get_error_message(self):
        return self.driver.find_element(self.error_message).text  # Fetch and return the error message


# Checks whether the company logo is displayed on the login page
# This is useful for verifying the page's UI elements
    def is_company_logo_displayed(self):
        return self.driver.find_element(self.company_logo).is_displayed()  # Return True if the logo is visible, False otherwise
