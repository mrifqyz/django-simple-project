from django.test import TestCase, Client, LiveServerTestCase
from django.contrib.auth.models import User
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        super().setUp()
        self.user = User(username='keongRacun')
        self.user.set_password("alphaMale")
        self.user.save()

class LoginTest(TestCase):
    def test_url_login(self):
        c = Client()
        response = c.get('/login')
        self.assertEqual(response.status_code, 200)

    def test_url_register(self):
        c = Client()
        response = c.get('/register')
        self.assertEqual(response.status_code, 200)

    def test_check_content(self):
        c = Client()
        response = c.get('/login')
        self.assertTemplateUsed(response, 'login.html')
        self.assertTemplateUsed(response, 'register.html')
        self.assertIn('login', response)

    def test_user_login(self):
        c = Client()
        response = c.get('/login')
        self.assertJSONEqual(response.content, {"loggedIn":False})
        self.client.login(username='keongRacun', password='alphaMale')
        self.assertJSONEqual(response.content, {"loggedIn":True})
        
class FunctionalTestLogin(LiveServerTestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--dns-prefetch-disable')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('disable-gpu')
        self.selenium = webdriver.Chrome(
            './chromedriver', chrome_options=chrome_options)
        super(FunctionalTestLogin, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(FunctionalTestLogin, self).tearDown()

    def test_login_user(self):
        selenium = self.selenium
        selenium.get("localhost:8000/login")

        userInput = selenium.find_element_by_css_selector("#userInput")
        passInput = selenium.find_element_by_id("passInput")
        loginBtn = selenium.find_element_by_id("login")

        userInput.send_keys("keongRacun")
        passInput.send_keys("alphaMale")
        loginBtn.send_keys(Keys.RETURN)

        time.sleep(2)

        self.assertEqual(selenium.current_url, "localhost:8000/welcome")

        time.sleep(2)

        self.client.logout()






        
