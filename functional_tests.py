from selenium import webdriver
import time
import unittest


class TestCostEstimator(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_title_of_home_page(self):
        "Test title is shown as Cost Estimator for the project"
        # First user enters url and sees a page with title "Cost Estimator"
        self.browser.get('http://localhost:8000')

        # Page title "Cost Estimator"
        self.assertIn("Cost Estimator", self.browser.title)

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Cost Estimator', header_text)

        # User sees From input box to enter travel from
        inputbox_source = self.browser.find_element_by_id('source')
        self.assertEqual(inputbox_source.get_attribute("name"), 'source')

        # User sees From input box to enter travel To
        inputbox_dest = self.browser.find_element_by_id('destination')
        self.assertEqual(inputbox_dest.get_attribute("name"), 'destination')

        # User ses submit button to click on search for itineraries

        # self.fail("Finish test")


if __name__ == '__main__':
    unittest.main(warnings='ignore')
