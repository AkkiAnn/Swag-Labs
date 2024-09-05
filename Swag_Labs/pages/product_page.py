from selenium.webdriver.common.by import By



# Initialize the ProductPage with a driver instance
# This constructor defines the locators
class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.product_name = By.CLASS_NAME, "inventory_item_name"  # Locator for the product name
        self.add_to_cart_button = By.CLASS_NAME, "btn_inventory"  # Locator for the 'Add to Cart' button
        self.product_image = By.CLASS_NAME, "inventory_item_img"  # Locator for the product image
        self.product_description = By.CLASS_NAME, "inventory_item_desc"  # Locator for the product description
        self.cart_icon = By.CLASS_NAME, "shopping_cart_badge"  # Locator for the cart icon to show the item count
        self.filter_dropdown = By.CLASS_NAME, "product_sort_container"  # Locator for the filter dropdown


# Clicks on the 'Add to Cart' button to add a product to the cart
    def click_add_to_cart(self):
        self.driver.find_element(self.add_to_cart_button).click()  # Click the 'Add to Cart' button


# Retrieves the text from the cart icon, which represents the number of items in the cart
    def get_cart_count(self):
        return self.driver.find_element(self.cart_icon).text  # Return the current count of items in the cart


# Retrieves and returns the product name from the product page
    def get_product_name(self):
        return self.driver.find_element(self.product_name).text  # Return the name of the product


# Retrieves and returns the product description from the product page
    def get_product_description(self):
        return self.driver.find_element(self.product_description).text  # Return the product description


# Clicks on the product image to navigate to the product's detail page
    def click_product_image(self):
        self.driver.find_element(self.product_image).click()  # Click the product image to view product details


# Selects a filter from the filter dropdown based on the given option
    def select_filter(self, filter_option):
        dropdown = self.driver.find_element(self.filter_dropdown)  # Find the dropdown element
        for option in dropdown.find_elements(By.TAG_NAME, 'option'):  # Iterate through the available options
            if option.text == filter_option:  # If the filter option matches the desired filter
                option.click()  # Select the filter option
                break
