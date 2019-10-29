from django.test import TestCase, Client, LiveServerTestCase
from .models import Status
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
# Create your tests here.


class LandingTest(TestCase):
    def test_check_content(self):
        c = Client()
        response = c.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "landing.html")
        self.assertContains(response, "Halo, apa kabar?")
        self.assertContains(response, "<form")

    def test_make_status(self):
        Status.objects.create(
            status='Coba-Coba'
        )
        self.assertEqual(Status.objects.all().count(), 1)

    def test_add_status_page(self):
        c = Client()
        toBePosted = {
            'status': 'Coba-Coba',
        }
        c.post("/", data=toBePosted)
        Status.objects.create(
            status=toBePosted['status']
        )
        response = c.get("/")
        content = response.content.decode('utf8')
        self.assertIn(toBePosted['status'], content)
        self.assertContains(response, toBePosted['status'])

    def test_status_is_more_than_300(self):
        c = Client()
        response = c.get("/")
        toBePosted = "Lorem ipsum dolor sit amet, cinoy ganteng consectetur adipiscing elit. Cras libero velit, dapibus ac condimentum vitae, fermentum non risus. Ut interdum pellentesque mollis. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aenean porttitor hahahahahhahahahahahahahaha"

        self.assertNotContains(response, toBePosted)


class LandingTestOnSelenium(LiveServerTestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--dns-prefetch-disable')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('disable-gpu')
        self.selenium = webdriver.Chrome(
            './chromedriver', chrome_options=chrome_options)
        super(LandingTestOnSelenium, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(LandingTestOnSelenium, self).tearDown()

    def test_add_status(self):
        selenium = self.selenium
        selenium.get('http://127.0.0.1:8000/')
        form = selenium.find_element_by_name("status")
        btn = selenium.find_element_by_name("submit")

        form.send_keys('Coba-coba')
        time.sleep(3)
        btn.send_keys(Keys.RETURN)
        time.sleep(3)
        self.assertIn('Coba-coba', selenium.page_source)


    def test_status_is_more_than_300(self):
        selenium = self.selenium
        selenium.get('http://127.0.0.1:8000/')
        form = selenium.find_element_by_name("status")
        btn = selenium.find_element_by_name("submit")

        form.send_keys("Lorem ipsum dolor sit amet, cinoy ganteng consectetur adipiscing elit. Cras libero velit, dapibus ac condimentum vitae, fermentum non risus. Ut interdum pellentesque mollis. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aenean porttitor bacot kamu nak gilaaaa hahahahahhahahahahahahahaha")
        time.sleep(3)
        btn.send_keys(Keys.RETURN)
        time.sleep(3)
        
        self.assertNotIn("Lorem ipsum dolor sit amet, cinoy ganteng consectetur adipiscing elit. Cras libero velit, dapibus ac condimentum vitae, fermentum non risus. Ut interdum pellentesque mollis. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aenean porttitor bacot kamu nak gilaaaa hahahahahhahahahahahahahaha", selenium.page_source)

