import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class OrangeHRMLoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()
        time.sleep(5)

    def test_invalid_login(self):
        username_input = self.driver.find_element(By.NAME, "username")
        username_input.send_keys("admin")
        time.sleep(2)

        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys("Admin123")
        time.sleep(2)

        login_button = self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
        login_button.click()
        time.sleep(2)

        print("invalid credentials")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
