from pages.base_page import BasePage
from playwright.sync_api import expect



class HomePage(BasePage):
    url = 'https://autofaq.ai/'

    def check_element_exists_by_locator(self, locator):
        element = self.page.locator(locator)
        expect(element).to_be_visible()

    def check_element_exists_by_text(self, text):
        element = self.page.get_by_text(text)
        expect(element).to_be_visible()

    def click_button(self, locator):
        button = self.page.locator(locator)
        button.click()

    def fill_field(self, locator, text):
        msg_field = self.page.locator(locator)
        msg_field.fill(text)
