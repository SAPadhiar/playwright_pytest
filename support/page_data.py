"""
This module holds information about instances of locators
"""
from support.locators import Locators
from support.test_base import TestBase


class PageData:
    """
    Class that contains instances of locators
    """
    welcome_str = "It’s easy to apply, tell us about yourself and see if you’re instantly approved for coverage! It’ll only take about 5-10 mins to complete your application."
    help_panel = "Email us\nyoursupport@insure.com\nIf you have questions specific to your coverages, please reach out to your HR Representative."


    def __init__(self):
        self.header_logo = TestBase.get_page().locator(Locators.header_logo)
        self.header_need_help_link = TestBase.get_page().locator(Locators.header_need_help_link)
        self.get_started_button = TestBase.get_page().locator(Locators.get_started_button)
        self.footer_text = TestBase.get_page().locator(Locators.footer_text)
        self.welcome_text = TestBase.get_page().locator(Locators.welcome_text)
        self.welcome_message = TestBase.get_page().locator(Locators.welcome_message)
        self.need_help_panel = TestBase.get_page().locator(Locators.need_help_panel)
        self.loading_icon = TestBase.get_page().locator(Locators.loading_icon)
        self.applicant_type = TestBase.get_page().locator(Locators.applicant_type)
        self.next_button = TestBase.get_page().locator(Locators.next_button)
        self.back_button = TestBase.get_page().locator(Locators.back_button)
        self.employee_label = TestBase.get_page().locator(Locators.employee_label)
        self.spouse_label = TestBase.get_page().locator(Locators.spouse_label)
        self.your_name_label = TestBase.get_page().locator(Locators.your_name_label)
        self.first_label = TestBase.get_page().locator(Locators.first_label)
        self.last_label = TestBase.get_page().locator(Locators.last_label)
        self.first_name_input = TestBase.get_page().locator(Locators.first_name_input)
        self.last_name_input = TestBase.get_page().locator(Locators.last_name_input)
