from django.test import TestCase, Client, LiveServerTestCase
from django.contrib.auth.models import User
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

class LoginTest(TestCase):
    def setUp(self):
        super().setUp()
        self.user = User(username='keongRacun')
        self.user.set_password("alphaMale")
        self.user.save()

    def test_url_login(self):
        c = Client()
        response = c.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_url_register(self):
        c = Client()
        response = c.get('/register')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    # def test_user_login(self):
    #     c = Client()
    #     response = c.get('/login')
    #     self.client.login(username='keongRacun', password='alphaMale')
        
# class FunctionalTestLogin(LiveServerTestCase):
#     def setUp(self):
#         chrome_options = Options()
#         # chrome_options.add_argument('--headless')
#         chrome_options.add_argument('--dns-prefetch-disable')
#         chrome_options.add_argument('--no-sandbox')
#         chrome_options.add_argument('disable-gpu')
#         self.selenium = webdriver.Chrome(
#             './chromedriver', chrome_options=chrome_options)
#         self.user = User.objects.create_user(username="keongRacun", password="alphaMale")
#         super(FunctionalTestLogin, self).setUp()

#     def tearDown(self):
#         self.selenium.quit()
#         super(FunctionalTestLogin, self).tearDown()

#     def test_login_user(self):
#         selenium = self.selenium
#         selenium.get("localhost:8000/login")
#         time.sleep(2)
        
#         userInput = selenium.find_element_by_css_selector("#user")
#         passInput = selenium.find_element_by_css_selector("#pswd")
#         loginBtn = selenium.find_element_by_css_selector("#login")

#         userInput.send_keys("keongRacun")
#         passInput.send_keys("alphaMale")

#         loginBtn.click()

#         time.sleep(2)

#         self.assertEqual(selenium.current_url, "localhost:8000")

#         time.sleep(5)






        
