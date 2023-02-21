import time
from threading import Thread
from selenium import webdriver
from Tests.maintest import *
class Utilites:
    def comman_steps(self,driver):
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(
            "https://railways.makemytrip.com/railways/listing?classCode=&className=All%20Classes&date=20230220&destCity=Satna&destStn=STA&srcCity=Bhopal&srcStn=BPL&trainNumber=")
        sd = SourceDestinationSelect(driver)
        # From city selection
        sd.from_city_select('Katni')
        # To City Selection
        sd.to_city_select('Jabalpur')

        # Calender handng
        # trvdate=input('''Enter your Traveling date in format
        # date monthname year
        # Example: 20 February 2023: ''')
        trvdate = '20 May 2023'
        calender = CalenderHandle(driver)
        calender.enter_date(trvdate)

        # Select class
        clselect = ClassSelect(driver)
        clselect.class_select()
        # click on Search button
        clselect.search_train()

        # Available trains data
        avtrain = AvaliableTrains(driver)
        traindata = avtrain.find_trains_data()

        # convert train data into csv
        data_inot_csv(traindata)

        # Display Data
        pprint(traindata)
        time.sleep(5)


class ChromeBrowser(Thread,Utilites):
    def run(self) -> None:
        driver = webdriver.Chrome()
        self.comman_steps(driver)


class FirefoxBrowser(Thread,Utilites):
    def run(self) -> None:
        driver = webdriver.Firefox()
        self.comman_steps(driver)

class EdgeBrowser(Thread,Utilites):
    def run(self) -> None:
        driver=webdriver.Edge()
        self.comman_steps(driver)

chrome=ChromeBrowser()
firefox=FirefoxBrowser()
edge=EdgeBrowser()
chrome.start()
firefox.start()
edge.start()

chrome.join()
firefox.join()
edge.join()
print("Run test in all Browser successfully..")