from selenium import webdriver
from django.test import LiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class BookAcceptanceTest(LiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_add_book(self):
        self.driver.get(self.live_server_url)
        
        self.driver.find_element(By.CLASS_NAME, "btn-add-book").click()
        
        self.driver.find_element(By.NAME, "title").send_keys("Test Book")
        self.driver.find_element(By.NAME, "author").send_keys("Test Author")
        self.driver.find_element(By.NAME, "publication_year").send_keys("2025")
        self.driver.find_element(By.ID, "submit").click()

        body = self.driver.find_element(By.TAG_NAME, "body").text
        self.assertIn("Test Book", body)
        self.assertIn("Test Author", body)
        self.assertIn("2025", body)
