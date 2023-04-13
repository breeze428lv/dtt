#!/usr/bin/env python
"""
Terminal Commands ----
    1. python3 manage.py runserver
    2. open another terminal
      functional test:  python3 functional_tests.py(NOT USED)
      functional test:  python3 manage.py test functional_tests
      unit test:        python3 manage.py test lists
      migration:        python3 manage.py makemigrations

      ----------------------------------------
      NOTE: "python3 manage.py test" executes all tests in tests.py within the whole app



"""
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest




class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    '''
    def tearDown(self):
        self.browser.quit()
    '''
    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element(by=By.ID, value='id_list_table')
        rows = table.find_element(by=By.TAG_NAME, value='tr')


    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard a cool new online to-do list app. She goes
        # to check out its homepage
        # Item.objects.create(text='itemey 1')
        # Item.objects.create(text='itemey 2')

        """
            According to urls.urlpatterns, views.home_page() is called, where
            'home.html' is rendered
        """
        self.browser.get('http://localhost:8000')
        self.browser.set_window_size(1024, 768)
        # self.browser.get(self.live_server_url)
        # self.browser.get('%s%s' % (self.live_server_url, '/'))
        # She notices the page title and header mention to-do lists
        # self.assertIn('To-Do', self.browser.title)

        edith_url = self.browser.current_url
        # print("edith_url", edith_url)
        header_text = self.browser.find_element(by=By.TAG_NAME, value='h1').text
        # print("header_text: " + header_text)
        self.assertIn('To-Do', header_text)
        # self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element(by=By.ID, value='id_new_item')

        print(inputbox.get_attribute('placeholder'))
        print(inputbox.location['x'])
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>")


        # self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # She types "Buy peacock feathers" into a text box(Edith's hobby
        # is tying fly-fishing lures)
        # inputbox.send_keys('Buy peacock feathers')
        # inputbox.send_keys(Keys.ENTER)




        # table = self.browser.find_element(by=By.ID, value='id_list_table')
        #
        # rows = table.find_elements(by=By.TAG_NAME, value='tr')
        # print("rows:")
        # for row in rows:
        #     print(row.text)



        # self.browser.implicitly_wait(3)
        #
        # self.browser.quit()
        # self.browser = webdriver.Firefox()
        # self.browser.get(self.live_server_url)
        #
        # francis_url = self.browser.current_url
        # print("francis_url", francis_url)
        # header_text = self.browser.find_element(by=By.TAG_NAME, value='h1').text
        # print("header_text: " + header_text)
        # self.assertIn('To-Do', header_text)
        #
        #
        # # She is invited to enter a to-do item straight away
        # inputbox = self.browser.find_element(by=By.ID, value='id_new_item')
        # print(inputbox.get_attribute('placeholder'))
        # print(">>>>>>>>>>>>>>>>>>>>>>>>>>")
        #
        # inputbox.send_keys('Buy milk')
        # inputbox.send_keys(Keys.ENTER)


        # When she hits enter, the page updates, and now the page lists:
        #  "1: Buy peacock feathers" as an item in a to-do list

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly"(Edith is very methodical)
        # inputbox = self.browser.find_element(by=By.ID, value='id_new_item')
        # self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')
        # inputbox.send_keys('Use peacock feathers to make a fly')
        # inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items, on her list
        # self.check_for_row_in_list_table('1: Buy peacock feathers')
        # self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')


        # table = self.browser.find_element(by=By.ID, value='id_list_table')
        # rows = table.find_element(by=By.TAG_NAME, value='tr')

        # Edith wonders whether the site remembers her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect

        # She visits that URL - her to-do list is still there.

        # Satified, she goes back to sleep


# if __name__ == '__main__':
#     unittest.main(warnings='ignore')

