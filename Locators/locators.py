class FromCityLocators:
    fromcitytab="fromCity"
    ftypecitbox="//div[@class='rsw_inputBox selectHtlCity inactiveWidget activeWidget']/div/div/input"
    fallresult="//div[@class='react-autosuggest__section-container react-autosuggest__section-container--first']/ul/li/div/p[1]"

class ToCityLocators:
    tocitytab = "toCity"
    ttypecitbox = "//div[@class='rsw_inputBox selectHtlCity inactiveWidget activeWidget']/div/div/input"
    tallresult = "//div[@class='react-autosuggest__section-container react-autosuggest__section-container--first']/ul/li/div/p[1]"

class CalenderLocators:
    calendertab="travelDate"
    nextbutton="//span[@class='DayPicker-NavButton DayPicker-NavButton--next']"
    month_year_select="//div[@class='DayPicker-Caption']/div"
    alldates="//div[@class='DayPicker-Month']/div[3]/div/div"

class ClassLocators:
    classtab="travelFor"
    allclasses="//ul[@class='travelForPopup']/li"
    searchbtn="//button[@class=' primaryBtn font18 latoBlack widgetSearchBtn']"

class AvaliableTrainsLocators:
    avltrains="//div[@class='train-list']/div"
    trainname="div[1]/div[1]/div[1]"
    depttime="div[1]/div[2]/div/div[1]/div[1]"
    dptstation="div[1]/div[2]/div/div[1]/div[2]"
    arvtime="div[1]/div[2]/div/div[3]/div[1]"
    arvstation="div[1]/div[2]/div/div[3]/div[2]"






