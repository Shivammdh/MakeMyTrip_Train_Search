import time
from pprint import pprint

from selenium import webdriver
from Pages.source_destination_select import SourceDestinationSelect
from Pages.calenderselect import CalenderHandle
from Pages.classselection import ClassSelect
from Pages.avaliable_Trains import AvaliableTrains
from Utilites.collect_train_data import data_inot_csv
import unittest

class TestMakeMyTrip(unittest.TestCase):
    def setUp(self) -> None:
        options1 = webdriver.ChromeOptions()
        options1.add_argument("disable-infobars")
        options1.add_argument("--disable-extensions")
        options1.add_argument('--no-sandbox')
        options1.add_experimental_option("useAutomationExtension", False)
        options1.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36")
        options1.add_argument('--headless')

        self.driver=webdriver.Chrome(options=options1)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://railways.makemytrip.com/railways/listing?classCode=&className=All%20Classes&date=20230220&destCity=Satna&destStn=STA&srcCity=Bhopal&srcStn=BPL&trainNumber=")

    def test_Make_My_Trip(self):
        driver=self.driver
        sd=SourceDestinationSelect(driver)
        # From city selection
        sd.from_city_select('Katni')
        # To City Selection
        sd.to_city_select('Jabalpur')


        # Calender handng
        # trvdate=input('''Enter your Traveling date in format
                # date monthname year
                # Example: 20 February 2023: ''')
        trvdate = '20 May 2023'
        calender=CalenderHandle(driver)
        calender.enter_date(trvdate)


        # Select class
        clselect=ClassSelect(driver)
        clselect.class_select()
        # click on Search button
        clselect.search_train()


        # Available trains data
        avtrain=AvaliableTrains(driver)
        traindata=avtrain.find_trains_data()


        # convert train data into csv
        data_inot_csv(traindata)

        # Display Data
        pprint(traindata)
        time.sleep(5)

    def tearDown(self) -> None:
        self.driver.close()

if __name__ == '__main__':
    unittest.main()

