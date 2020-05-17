from selenium import webdriver
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
        self.fail("Finish test")

        # User sees From input box to enter travel from

        # User sees Destination input box to enter travel to

        # User ses submit button to click on search for itineraries


if __name__ == '__main__':
    unittest.main(warnings='ignore')
