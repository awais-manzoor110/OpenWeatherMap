from selenium.webdriver.common.by import By


class OpenWeatherMap:

    def __init__(self, driver):
        self.driver = driver

    website_title = "Сurrent weather and forecast - OpenWeatherMap"
    nav_search = (By.NAME, "q")
    searchbar = (By.XPATH, "//input[@placeholder='Search city']")
    search_button = "//button[@type='submit']"
    navbar_search_button = "(//input[@type='submit'])[1]"
    search_drp = (By.XPATH, "//ul[@class='search-dropdown-menu']/li")
    navbar_reslt = (By.XPATH, "//td/b/a")
    search_b = (By.ID, "search_str")
    validation = (By.XPATH, "//div[@role='alert']")
    alert_message = "Not found"
    search_city = (By.XPATH, "//div[@class='current-container mobile-padding']")
    celsius_button = "(//div[@class='switch-container']/div[@class='option'])[1]"
    fahrenheit_button = "(//div[@class='switch-container']/div[@class='option'])[2]"
    day_forcast = (By.XPATH, "//div/ul[@class='day-list']/li/span")

    def search_bar(self):
        return self.driver.find_element(*OpenWeatherMap.searchbar)

    def navbar_search(self):
        return self.driver.find_element(*OpenWeatherMap.nav_search)

    def search_dropdown(self):
        ele = self.driver.find_element(*OpenWeatherMap.search_drp).text
        text = ele.split('\n')[-3]
        return text

    def navbar_result(self):
        return self.driver.find_element(*OpenWeatherMap.navbar_reslt)

    def search_field(self):
        return self.driver.find_element(*OpenWeatherMap.search_b).get_attribute("value")

    def alert(self):
        ele = self.driver.find_element(*OpenWeatherMap.validation).text
        text = ele.split("\n")[-1]
        return text

    def searched_city(self):
        return self.driver.find_element(*OpenWeatherMap.search_city).text

    def days_forcast(self):
        return self.driver.find_elements(*OpenWeatherMap.day_forcast)
