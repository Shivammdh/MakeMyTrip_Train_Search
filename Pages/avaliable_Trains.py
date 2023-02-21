from selenium.webdriver.common.by import By

from Locators.locators import AvaliableTrainsLocators

class AvaliableTrains:
    def __init__(self,driver):
        self.driver=driver
        self.avltrains=AvaliableTrainsLocators.avltrains
        self.trainname=AvaliableTrainsLocators.trainname
        self.depttime=AvaliableTrainsLocators.depttime
        self.dptstation=AvaliableTrainsLocators.dptstation
        self.arvtime=AvaliableTrainsLocators.arvtime
        self.arvstation=AvaliableTrainsLocators.arvstation

    def find_trains_data(self):

        avaliableTrains = self.driver.find_elements(By.XPATH,self.avltrains)
        print(len(avaliableTrains))
        traindata = []
        for trains in avaliableTrains:
            data = {}
            # //div[@class='train-list']/div/div[1]/div[1]/div[1]
            data['Train Name'] = trains.find_element(By.XPATH, self.trainname).text
            # print(train_name)
            # //div[@class='train-list']/div/div[1]/div[2]/div/div[1]/div
            # //div[@class='train-list']/div/div[1]/div[2]/div/div[1]
            data['departure'] = trains.find_element(By.XPATH, self.depttime).text

            data['Departure Station'] = trains.find_element(By.XPATH, self.dptstation).text
            # //div[@class='train-list']/div/div[1]/div[2]/div/div[3]/div[1]
            data['Arrival'] = trains.find_element(By.XPATH, self.arvtime).text
            data['Arrival Station'] = trains.find_element(By.XPATH, self.arvstation).text
            traindata.append(data)
        return traindata