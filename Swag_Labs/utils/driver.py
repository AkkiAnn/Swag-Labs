from selenium import webdriver

class Driver:
    @staticmethod
    def get_driver(browser="chrome"):
        if browser == "chrome":
            driver = webdriver.Chrome()
        elif browser == "firefox":
            driver = webdriver.Firefox()
        else:
            raise Exception(f"Browser '{browser}' is not supported.")
        driver.maximize_window()
        return driver
