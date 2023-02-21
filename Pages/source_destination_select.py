import time

from selenium.webdriver.common.by import By

from Locators.locators import FromCityLocators,ToCityLocators

class SourceDestinationSelect:
    def __init__(self,driver):
        self.driver=driver
        self.fromcitytab=FromCityLocators.fromcitytab
        self.ftypecitbox=FromCityLocators.ftypecitbox
        self.fallresult=FromCityLocators.fallresult
        self.tocitytab=ToCityLocators.tocitytab
        self.ttypecitbox=ToCityLocators.ttypecitbox
        self.tallresult=ToCityLocators.tallresult

    def from_city_select(self,cityname):
        driver=self.driver
        driver.find_element(By.ID, self.fromcitytab).click()
        # fromcityname = input("Enter your source city name: ")
        # # fromcityname='Katni'
        driver.find_element(By.XPATH,self.ftypecitbox).send_keys(cityname)
        time.sleep(2)
        fromcity = driver.find_elements(By.XPATH,self.fallresult)
        for city in fromcity:
            if cityname in city.text:
                city.click()
                break

    def to_city_select(self,cityname):
        driver=self.driver
        driver.find_element(By.ID,self.tocitytab).click()
        # tocityname = input("Enter your Destination city name: ")
        # tocityname='Jabalpur'
        driver.find_element(By.XPATH,self.ttypecitbox).send_keys(cityname)
        time.sleep(2)
        tocity = driver.find_elements(By.XPATH,self.tallresult)

        for city in tocity:
            if cityname in city.text:
                city.click()
                break
