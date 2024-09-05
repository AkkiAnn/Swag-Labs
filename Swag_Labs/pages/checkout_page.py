from selenium.webdriver.common.by import By

class CheckoutPage:

# Initializes the CheckoutPage with the driver instance
# Defines locators
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = By.ID, "checkout"  # Locator for the "Checkout" button
        self.first_name_input = By.ID, "first-name"  # Locator for the first name input field
        self.last_name_input = By.ID, "last-name"  # Locator for the last name input field
        self.zip_code_input = By.ID, "postal-code"  # Locator for the zip/postal code input field
        self.continue_button = By.ID, "continue"  # Locator for the "Continue" button in the checkout process
        self.finish_button = By.ID, "finish"  # Locator for the "Finish" button
        self.thank_you_message = By.CLASS_NAME, "complete-header"  # Locator for the thank you message after completing the checkout


# Simulates clicking the 'Checkout' button to initiate the checkout process
    def click_checkout(self):
        self.driver.find_element(self.checkout_button).click()


# Enters the shipping information including first name, last name, and zip code
# These fields are mandatory for proceeding with the checkout
    def enter_shipping_information(self, first_name, last_name, zip_code):
        self.driver.find_element(self.first_name_input).send_keys(first_name)  # Enters the first name
        self.driver.find_element(self.last_name_input).send_keys(last_name)  # Enters the last name
        self.driver.find_element(self.zip_code_input).send_keys(zip_code)  # Enters the zip code


# Clicks the 'Continue' button to proceed with the checkout after entering shipping details
    def click_continue(self):
        self.driver.find_element(self.continue_button).click()

# Retrieves the thank you message text displayed after successful checkout completion
    def get_thank_you_message(self):
        return self.driver.find_element(self.thank_you_message).text
