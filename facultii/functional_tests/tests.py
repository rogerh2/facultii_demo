from selenium import webdriver
from django.test import LiveServerTestCase
from django.test import Client
import time

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_homepage(self):
        # Smith is researching Prof. Kimani's lab
        # he visits her lab websites hompage
        self.browser.get(self.live_server_url)

        # He notices that it loads properly
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_links_to_members_page(self):
        #Smith likes what he sees on the homepage
        #and decides to contact the lab, he clicks
        #link entitled members
        self.browser.get('http://127.0.0.1:8000')
        members_link = self.browser.find_element_by_id('members')
        members_link.click()
        time.sleep(1)
        self.assertIn('member', self.browser.current_url)
