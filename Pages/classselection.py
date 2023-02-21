import time

from selenium.webdriver.common.by import By

from Locators.locators import ClassLocators

class ClassSelect:
    def __init__(self,driver):
        self.driver=driver
        self.classtab=ClassLocators.classtab
        self.allclasses=ClassLocators.allclasses
        self.searchbtn=ClassLocators.searchbtn

    def class_select(self):
        driver=self.driver
        driver.find_element(By.ID, self.classtab).click()
        time.sleep(2)
        classes = driver.find_elements(By.XPATH, self.allclasses)

        for trvclass in classes:
            if trvclass.text == 'All Classes':
                trvclass.click()
                break

    def search_train(self):

        self.driver.find_element(By.XPATH, self.searchbtn).click()
        time.sleep(5)

