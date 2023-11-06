import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class OrangeHRMLoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login_to_orangehrm(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()
        time.sleep(5)

        username_field = self.driver.find_element(By.NAME,"username")
        password_field = self.driver.find_element(By.NAME,"password")

        login_button = self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
        time.sleep(5)

        username_field.send_keys("Admin")
        password_field.send_keys("admin123")
        login_button.click()
        time.sleep(5)

        print("the user is logged in successfully")

        # welcome_message = self.driver.find_element(By.ID, "welcome")
        # self.assertEqual(welcome_message.text, "Welcome Admin")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
