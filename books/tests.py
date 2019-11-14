from django.test import TestCase, Client, LiveServerTestCase
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BookTest(TestCase):
    def test_book_url(self):
        c = Client()
        response = c.get("/books")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "books.html")

class BookFunctionalTest(LiveServerTestCase):
    
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--dns-prefetch-disable')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('disable-gpu')
        self.selenium = webdriver.Chrome(
            './chromedriver', chrome_options=chrome_options)
        super(BookFunctionalTest, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(BookFunctionalTest, self).tearDown()

    def test_if_search_clicked_show_content(self):
        selenium = self.selenium
        selenium.get('http://127.0.0.1:8000/books')

        searchbox = selenium.find_element_by_css_selector(".searchbox")
        searchbox.send_keys("Algorithm")

        time.sleep(2)
        
        btnSearch = selenium.find_element_by_css_selector(".btn-search")

        time.sleep(2)
        self.assertIn('The Master Algorithm', selenium.page_source)
        time.sleep(2)