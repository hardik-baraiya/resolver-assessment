from selenium.webdriver.common.by import By
from selenium import webdriver
import unittest

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestCases(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "https://hardik-baraiya.github.io/resolver-assessment/index.html"
    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_1_login_page(self):
        self.driver.get(self.url)                                                                                       # Navigate to home page
        username_field = self.driver.find_element(By.ID, "inputEmail")
        self.assertTrue(username_field.is_displayed(), "Email input field is not displayed on the login page")     # Assert email address field is present
        username_field.clear()
        username_field.send_keys("Test1email@test.com")
        password_field = self.driver.find_element(By.ID, "inputPassword")
        self.assertTrue(password_field.is_displayed(), "Password input field is not displayed on the login page")  # Assert password field is present
        password_field.clear()
        password_field.send_keys("Test1@password1")
        login_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Sign in')]")
        self.assertTrue(login_button.is_displayed(), "Login button is not displayed")                              # Assert login button is present
        login_button.click()
        print("Test 1 successfully passed")

    def test_2_lists(self):
        self.driver.get(self.url)                                                                                       # Navigate to home page
        test_2_div = self.driver.find_element(By.ID, "test-2-div")
        self.assertTrue(test_2_div.is_displayed(), "Test 2 div is not displayed")
        list_items = test_2_div.find_elements(By.XPATH, '//ul[@class="list-group"]/li')
        assert len(list_items) == 3, "Three values are not present in the listgroup"                                    # Assert three values present in the listgroup
        badge_span = self.driver.find_element(By.XPATH, '//span[contains(text(),"6")]').text.strip()
        assert badge_span == "6", "Badge value for second list item is not '6'"                                         # Assert the second list item's badge value is 6
        second_list_item = list_items[1].text.strip()
        desired_text = second_list_item.replace(badge_span, "").strip()
        assert desired_text == "List Item 2", "Second list item's value is not set to 'List Item 2'"                    #Assert second list item's value is set to "List Item 2"
        print("Test 2 successfully passed")

    def test_3_select_options(self):
        self.driver.get(self.url)                                                                                       # Navigate to home page
        default_dropdown = self.driver.find_element(By.ID, "dropdownMenuButton")
        default_option1 = default_dropdown.text.strip()
        assert default_option1 == "Option 1", "Option 1 is not the default option in the dropdown"                      # Assert "Option 1" is the default selected value
        default_dropdown.click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Option 3')]").click()
        option3_selected = default_dropdown.text.strip()
        assert option3_selected == "Option 3", "Option 3 is not selected in the dropdown"                               # Assert "Option 3" from the select list
        print("Test 3 successfully passed")

    def test_4_buttons(self):
        self.driver.get(self.url)                                                                                       # Navigate to home page
        enabled_button = self.driver.find_element(By.XPATH, "//div[@id='test-4-div']/button[1]")
        assert enabled_button.is_enabled(), "First button is not enabled"                                               # Assert first button is enabled
        disabled_button = self.driver.find_element(By.XPATH, "//div[@id='test-4-div']/button[2]")
        assert not disabled_button.is_enabled(), "Second button is enabled"                                             # Assert second button is disabled
        print("Test 4 successfully passed")

    def test_5_wait_for_button_displayed(self):
        self.driver.get(self.url)                                                                                       # Navigate to home page
        button_div = self.driver.find_element(By.ID, "test-5-div")
        button_random = WebDriverWait(button_div, 20).until(
            expected_conditions.visibility_of_element_located((By.ID, 'test5-button')))
        button_random.click()                                                                                           # Waiting for the button to be displayed and then click
        success_message = self.driver.find_element(By.ID, "test5-alert").text.strip()
        assert success_message == "You clicked a button!", "No success message was displayed"                           # Asserting success message after click
        assert not button_random.is_enabled(), "Button is still enabled"                                                # Assert button is disabled
        print("Test 5 successfully passed")

    def get_cell_value(self, row, col):                                                                                 # Method that allows to find the value of any cell on the grid
        table = self.driver.find_element(By.XPATH, "//*[@id='test-6-div']//table")
        rows = table.find_elements(By.XPATH, "//*[@id='test-6-div']//table/tbody/tr")
        cell = rows[row].find_elements(By.TAG_NAME, "td")[col]
        return cell.text

    def test_6_find_cell_value(self):
        self.driver.get(self.url)                                                                                       # Navigate to the home page
        cell_value = self.get_cell_value(2, 2)                                                                 # Value of the cell at coordinates 2, 2
        assert cell_value == "Ventosanzap", "Expected value is not 'Ventosanzap'"                                       # Assert that the value of the cell is "Ventosanzap"
        print("Test 6 successfully passed")


if __name__ == "__main__":
    unittest.main()
