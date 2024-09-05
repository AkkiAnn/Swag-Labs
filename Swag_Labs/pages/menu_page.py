from selenium.webdriver.common.by import By

class MenuPage:

# Initializes the MenuPage with a driver instance
# The constructor defines the locators
    def __init__(self, driver):
        self.driver = driver
        self.reset_app_state_button = By.ID, "reset_sidebar_link"  # Locator for the "Reset App State" button
        self.logout_button = By.ID, "logout_sidebar_link"  # Locator for the "Logout" button


# Clicks the "Reset App State" button to reset the application state
# This method is used when you want to reset the app to its default state
    def click_reset_app_state(self):
        self.driver.find_element(self.reset_app_state_button).click()  # Click on the reset app state button


# Clicks the "Logout" button to log out of the application
# This method helps in simulating the logout action, useful for session management tests
    def click_logout(self):
        self.driver.find_element(self.logout_button).click()  # Click on the logout button
