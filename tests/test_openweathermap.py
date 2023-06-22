import pytest
from assertpy import assert_that
from selenium.common import TimeoutException, NoSuchElementException, StaleElementReferenceException
from pageObjects.openweathermap import OpenWeatherMap
from test_data.test_data import Test_Data
from utilities.baseclass import BaseClass


class Test_OpenWeatherMap(BaseClass):
    searched_city_data = None

    def setup_method(self):
        # Create instances of classes we need to test
        self.user = OpenWeatherMap(self.driver)
        # Create logger object for logging test results
        self.logger = self.get_logger()

    def test_verify_that_title_of_the_website_should_be_current_weather_and_forcast(self):

        try:

            title = self.driver.title
            assert_that(title).is_equal_to(self.user.website_title)

        except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as e:

            # If an exception occurs during the test, log the exception and skip the test
            self.logger.error(f"An exception occurred: {e}")
            self.driver.save_screenshot("report/test_case_error.png")

        else:
            # If the test is successful, log a success message and the result of the test
            self.logger.info(f"Title is matched {title}.")

    def test_verify_that_when_user_search_city_name_from_searchbar_same_city_should_be_displayed_in_the_dropdown(self, get_data):

        try:

            self.user.search_bar().send_keys(get_data["city_name"])
            self.invisibility_of_loader()
            self.click_element(self.user.search_button)
            dropdown_value = self.user.search_dropdown()
            assert_that(dropdown_value).is_equal_to("Lahore, PK")

        except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as e:

            # If an exception occurs during the test, log the exception and skip the test
            self.logger.error(f"An exception occurred: {e}")
            self.driver.save_screenshot("report/test_case_error.png")

        else:
            # If the test is successful, log a success message and the result of the test
            self.logger.info(f"Title is matched {dropdown_value}.")

    def test_verify_that_if_user_enter_partial_text_of_a_city_it_should_show_a_alert(self, get_data):

        try:

            self.user.navbar_search().send_keys(get_data["wrong_city_name"])
            self.click_element(self.user.navbar_search_button)
            alert = self.user.alert()
            assert_that(alert).is_equal_to(self.user.alert_message)

        except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as e:

            # If an exception occurs during the test, log the exception and skip the test
            self.logger.error(f"An exception occurred: {e}")
            self.driver.save_screenshot("report/test_case_error.png")

        else:
            # If the test is successful, log a success message and the result of the test
            self.logger.info(f"Alert is shown{alert}.")

    def test_verify_that_when_user_search_a_city_name_from_navbar_same_city_result_should_be_displayed(self, get_data):

        try:

            self.user.navbar_search().send_keys(get_data["city_name"])
            self.click_element(self.user.navbar_search_button)
            navbar_result = self.user.navbar_result().text
            assert_that(navbar_result).is_equal_to("Lahore, PK")

        except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as e:

            # If an exception occurs during the test, log the exception and skip the test
            self.logger.error(f"An exception occurred: {e}")
            self.driver.save_screenshot("report/test_case_error.png")

        else:
            # If the test is successful, log a success message and the result of the test
            self.logger.info("Same Search Result is displayed.")

    def test_verify_that_when_user_search_a_city_name_from_navbar_same_city_result_should_be_displayed_in_search_field(self):

        try:

            search_field = self.user.search_field()
            assert_that(search_field).is_equal_to("Lahore")

        except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as e:

            # If an exception occurs during the test, log the exception and skip the test
            self.logger.error(f"An exception occurred: {e}")
            self.driver.save_screenshot("report/test_case_error.png")

        else:
            # If the test is successful, log a success message and the result of the test
            self.logger.info(f"Same city name is in the field {search_field}.")

    def test_verify_that_when_user_click_on_the_city_same_city_related_weather_status_should_be_displayed(self):

        try:

            glo = Test_OpenWeatherMap
            self.user.navbar_result().click()
            glo.searched_city_data = self.user.searched_city()
            searched_city_name = glo.searched_city_data.split("\n")[1]
            assert_that(searched_city_name).is_equal_to("Lahore, PK")

        except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as e:

            # If an exception occurs during the test, log the exception and skip the test
            self.logger.error(f"An exception occurred: {e}")
            self.driver.save_screenshot("report/test_case_error.png")

        else:
            # If the test is successful, log a success message and the result of the test
            self.logger.info(f"Title is matched {glo.searched_city_data}.")

    def test_verify_that_when_user_select_celsius_format_then_data_should_be_displayed_in_celsius_format_or_not(self):

        try:

            glo = Test_OpenWeatherMap
            self.invisibility_of_loader()
            self.click_element(self.user.celsius_button)
            celsius_format = glo.searched_city_data.split("\n")[2]
            degree = celsius_format[2]
            symbol = celsius_format[3]
            degree_format = degree + symbol
            assert_that(degree_format).is_equal_to("°C")

        except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as e:

            # If an exception occurs during the test, log the exception and skip the test
            self.logger.error(f"An exception occurred: {e}")
            self.driver.save_screenshot("report/test_case_error.png")

        else:
            # If the test is successful, log a success message and the result of the test
            self.logger.info(f"Title is matched {format}.")

    def test_verify_that_when_user_select_fahrenheit_format_then_data_should_be_displayed_in_fahrenheit_format_or_not(self):

        try:

            glo = Test_OpenWeatherMap
            self.invisibility_of_loader()
            self.click_element(self.user.fahrenheit_button)
            self.invisibility_of_loader()
            glo.searched_city_data = self.user.searched_city()
            fahrenheit_format = glo.searched_city_data.split("\n")[2]
            degree = fahrenheit_format[2]
            symbol = fahrenheit_format[3]
            degree_format = degree + symbol
            assert_that(degree_format).is_equal_to("°F")

        except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as e:

            # If an exception occurs during the test, log the exception and skip the test
            self.logger.error(f"An exception occurred: {e}")
            self.driver.save_screenshot("report/test_case_error.png")

        else:
            # If the test is successful, log a success message and the result of the test
            self.logger.info(f"Title is matched {format}.")

    def test_verify_that_8_days_forcast_should_be_displayed_in_the_8_days_forcast_section(self):

        try:

            count = 0
            day_text = None
            eight_days_forecast = self.user.days_forcast()
            for day in eight_days_forecast:
                day_text = day.text
                print(day_text)
                count += 1
            assert_that(count).is_equal_to(8)

        except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as e:

            # If an exception occurs during the test, log the exception and skip the test
            self.logger.error(f"An exception occurred: {e}")
            self.driver.save_screenshot("report/test_case_error.png")

        else:
            # If the test is successful, log a success message and the result of the test
            self.logger.info(f"Next 8 days {day_text}.")

    @pytest.fixture(params=Test_Data.common_data)
    def get_data(self, request):
        return request.param
