from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import pytest

#@pytest.mark.usefixtures("setup") # not needed if BaseClass is inherited
from TestData.e2eData import e2eData
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self,getData): #     def test_e2e(self,setup): if not inheriting BaseClass

        log = self.getLogger()

        log.info("log test comment divice: "+getData["device"])

        homePage = HomePage(self.driver)
        #homePage.shopButton().click if not integrated click into shopButton method
        checkoutPage = homePage.shopButton()

        #self.driver.find_element_by_css_selector("a[href*='shop']").click() moved to page object model

        #products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
        #checkoutPage = CheckoutPage(self.driver) not needed if integrated from homePage.shopButton
        products = checkoutPage.getProducts()

        for product in products:
            #productName = product.find_element_by_xpath("div/h4/a").text
            productName = checkoutPage.getProductName(product).text

            if productName == getData["device"]:
                # Add item into cart
                product.find_element_by_xpath("div/button").click()

        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        self.driver.find_element_by_id("country").send_keys(getData["countryAbbreviation"])

        # put into utility
        #wait = WebDriverWait(self.driver, 7)
        #wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.verifyLinkPresence(getData["countryName"])

        self.driver.find_element_by_link_text(getData["countryName"]).click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("[type='submit']").click()
        successText = self.driver.find_element_by_class_name("alert-success").text

        assert "Success! Thank you!" in successText

        self.driver.refresh()

    @pytest.fixture(params=e2eData.test_e2e_data)
    def getData(self,request):
        return request.param
        # test will run multiple times, one for each data set
        # so you need to navigate back to starting screen by moving the command back from conftest or refreshing
