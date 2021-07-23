from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    # driver.find_element_by_css_selector("a[href*='shop']").click() this is the step we are creating
    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    def shopButton(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckoutPage(self.driver)
        return checkOutPage

