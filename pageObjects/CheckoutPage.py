from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    # products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
    products = (By.XPATH, "//div[@class='card h-100']")
    def getProducts(self):
        return self.driver.find_elements(*CheckoutPage.products)

    #productName = product.find_element_by_xpath("div/h4/a").text
    productName = (By.XPATH, "div/h4/a")
    def getProductName(self,product):
        return product.find_element(*CheckoutPage.productName)
