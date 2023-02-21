import time

from selenium.webdriver.common.by import By

from Locators.locators import CalenderLocators

class CalenderHandle:
    def __init__(self,driver):
        self.driver=driver
        self.calendertab=CalenderLocators.calendertab
        self.nextbutton=CalenderLocators.nextbutton
        self.month_year_select=CalenderLocators.month_year_select
        self.alldates=CalenderLocators.alldates

    def enter_date(self,date):
        driver=self.driver
        driver.find_element(By.ID, self.calendertab).click()
        time.sleep(2)
        nextbtn = driver.find_element(By.XPATH, self.nextbutton)
        month_year = driver.find_element(By.XPATH, self.month_year_select)
        tvsplit = date.split()

        while True:
            if ' '.join(tvsplit[1:3]) == month_year.text.strip():
                break
            else:
                nextbtn.click()
                time.sleep(2)
        dates = driver.find_elements(By.XPATH, self.alldates)
        time.sleep(1)

        for date in dates:
            if date.text == tvsplit[0]:
                date.click()
                break
