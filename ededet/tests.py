from django.test import TestCase, Client
from .models import Status

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
            status = 'Coba-Coba'
        )
        self.assertEqual(Status.objects.all().count(), 1)

    def test_add_status_page(self):
        c = Client()
        toBePosted = { 
 			'status': 'Coba-Coba',
        }
        c.post("/", data=toBePosted)
        Status.objects.create(
            status = toBePosted['status']
        )
        response = c.get("/")
        content = response.content.decode('utf8')
        self.assertIn(toBePosted['status'], content)