import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
import time


class OrangeHRMLoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login_to_orangehrm(self, calendar_table=None):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()
        time.sleep(5)

        username_field = self.driver.find_element(By.NAME, "username")
        password_field = self.driver.find_element(By.NAME, "password")

        login_button = self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
        time.sleep(5)

        username_field.send_keys("Admin")
        password_field.send_keys("admin123")
        login_button.click()
        time.sleep(5)

        PIM = self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a")
        PIM.click()
        time.sleep(2)

        add_employee = self.driver.find_element(By.LINK_TEXT, "Add Employee")
        add_employee.click()
        time.sleep(2)

        first_name = self.driver.find_element(By.NAME, "firstName")
        first_name.click()
        first_name.send_keys("Sigirisetti")
        time.sleep(2)

        last_name = self.driver.find_element(By.NAME, "lastName")
        last_name.click()
        last_name.send_keys("Thirupathamma")
        time.sleep(2)

        emp_id = self.driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        emp_id.clear()
        emp_id.send_keys("101")
        time.sleep(2)

        create_login = self.driver.find_element(By.XPATH,
                                                "//span[@class='oxd-switch-input oxd-switch-input--active --label-right']")
        create_login.click()
        time.sleep(2)

        username2 = self.driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[3]")
        username2.click()
        username2.send_keys("thiru")
        time.sleep(2)

        password2 = self.driver.find_element(By.XPATH, "(//input[@type='password'])[1]")
        password2.click()
        password2.send_keys("Pavannaidu9@")
        time.sleep(2)

        confirm_password = self.driver.find_element(By.XPATH, "(//input[@type='password'])[2]")
        confirm_password.click()
        confirm_password.send_keys("Pavannaidu9@")
        time.sleep(2)

        save_butoon = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        save_butoon.click()
        time.sleep(2)

         emp_list=self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]")
        emp_list.click()
        time.sleep(2)


        del_person=self.driver.find_element(By.XPATH,"(//i[@class='oxd-icon bi-trash'])[8]")
        del_person.click()
        time.sleep(5)

        del_button=self.driver.find_element(By.XPATH,"//button[normalize-space()='Yes, Delete']")
        del_button.click()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
