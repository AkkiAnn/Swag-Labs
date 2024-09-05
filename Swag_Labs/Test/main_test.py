import pytest
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from utils.driver import Driver


# Importing necessary page classes and custom driver utility for browser setup

@pytest.fixture(scope="function")
def driver():

    driver = Driver.get_driver()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


# Test Case 1: Verify that an invalid username displays an error message
def test_invalid_username(driver):
    login_page = LoginPage(driver)
    login_page.enter_username("invalid_user")  # Invalid username
    login_page.enter_password("secret_sauce")  # Valid password
    login_page.click_login()
    assert "sadface" in login_page.get_error_message()  # Check error message displayed for invalid username


# Test Case 2: Verify that valid username logs in successfully
def test_valid_username(driver):
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")  # Valid username
    login_page.enter_password("secret_sauce")  # Valid password
    login_page.click_login()
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"  # Validate URL after successful login


# Logs in with valid credentials
def standard_user_login(driver):
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()


# Test Case 3: Verify that adding a product to the cart updates the cart count
def test_add_to_cart(driver):
    standard_user_login(driver)  # Log in first
    product_page = ProductPage(driver)
    product_page.click_add_to_cart()  # Add product to cart
    assert product_page.get_cart_count() == "1"  # Check if cart count is updated


# Test Case 4: Verify that clicking the product image redirects to product details page
def test_product_image_click(driver):
    standard_user_login(driver)  # Log in first
    product_page = ProductPage(driver)
    product_page.click_product_image()  # Click on product image
    assert driver.current_url != "https://www.saucedemo.com/inventory.html"  # Check redirection to product details


# Test Case 5: Verify that filter by price works correctly
def test_filter_by_price(driver):
    standard_user_login(driver)  # Log in first
    product_page = ProductPage(driver)
    product_page.select_filter("Price (low to high)")  # Apply filter by price
    # Additional assertions can be added to check if prices are sorted correctly


# Test Case 6: Verify the checkout process works as expected
def test_checkout_process(driver):
    standard_user_login(driver)  # Log in first
    product_page = ProductPage(driver)
    product_page.click_add_to_cart()  # Add a product to the cart

    checkout_page = CheckoutPage(driver)
    checkout_page.click_checkout()  # Go to checkout page
    checkout_page.enter_shipping_information("John", "Doe", "12345")  # Enter shipping information
    checkout_page.click_continue()  # Continue checkout process
    assert "Thank you for your order!" in checkout_page.get_thank_you_message()  # Validate successful order message


# Negative Test Case: Verify that an error user login fails
def test_error_user_login(driver):
    login_page = LoginPage(driver)
    login_page.enter_username("error_user")  # Invalid username
    login_page.enter_password("secret_sauce")  # Valid password
    login_page.click_login()
    assert "sadface" in login_page.get_error_message()  # Check for error message for invalid login

