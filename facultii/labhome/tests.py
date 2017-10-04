from selenium import webdriver
from django.test import TestCase
import unittest

# Create your tests here.
class IconTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()

    def test_will_count_to_9999_and_stop(self):
        self.browser.get('http://127.0.0.1:8000/emailicon')
        unread_element = self.browser.find_element_by_id('unreadcount')
        unread_number_start = int(unread_element.get_attribute("text"))
        self.assertEqual(unread_number_start, 1000)
        start_button = self.browser.find_element_by_id('start')
        start_button.click()
        unread_number_end = int(unread_element.get_attribute("text"))
        self.assertEqual(unread_number_end, 9999)