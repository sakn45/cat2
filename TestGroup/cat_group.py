# -*- coding: utf-8 -*-
import unittest

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException


class UntitledTestCase(unittest.TestCase):
    def setUp(wd):
        wd.driver = webdriver.Chrome()
        wd.driver.implicitly_wait(30)

    
    def test_untitled_test_case(self):
        wd = self.driver
        self.open_home_page(wd)
        self.login(wd)
        self.open_groups_page(wd)
        self.create_group(wd)
        self.return_to_groups_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element(By.LINK_TEXT, "Logout").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys("admin")
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys("secret")

    def return_to_groups_page(self, wd):
        wd.find_element(By.LINK_TEXT, "group page").click()

    def create_group(self, wd):
        # init group creation
        wd.find_element(By.NAME, "new").click()
        # fill group form
        wd.find_element(By.ID, "content").click()
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").clear()
        wd.find_element(By.NAME, "group_name").send_keys("huwud")
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").clear()
        wd.find_element(By.NAME, "group_header").send_keys("ueuffjub")
        wd.find_element(By.NAME, "group_footer").click()
        wd.find_element(By.NAME, "group_footer").clear()
        wd.find_element(By.NAME, "group_footer").send_keys("dhubdegb")
        # submit group creation
        wd.find_element(By.NAME, "submit").click()

    def open_groups_page(self, wd):
        wd.find_element(By.LINK_TEXT, "groups").click()

    def login(self, wd):
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys("admin")
        wd.find_element(By.NAME, "pass").click()
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys("secret")
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://127.0.0.1/addressbook/group.php")

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    

    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
