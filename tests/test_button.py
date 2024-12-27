from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from locators.chat import Chat
from utils.string_generation import random_string
import allure


@allure.feature('chat')
@allure.story('existence')
def test_chat_exists(page: Page):
    home_page = HomePage(page)
    home_page.open_page()
    home_page.check_element_exists_by_locator(Chat.CHAT_BUTTON+'1112223')

@allure.feature('chat')
@allure.story('clickability')
def test_opening_chat(page: Page):
    home_page = HomePage(page)
    home_page.open_page()
    home_page.click_button(Chat.CHAT_BUTTON)

@allure.feature('chat')
@allure.story('sendability')
def test_send_message_in_chat(page: Page):
    home_page = HomePage(page)
    home_page.open_page()
    home_page.click_button(Chat.CHAT_BUTTON)
    home_page.fill_field(Chat.MSG_FIELD, random_string)
    home_page.click_button(Chat.SEND_MSG_BUTTON)
    home_page.check_element_exists_by_text(random_string)


@allure.feature('chat')
@allure.story('displayability')
def test_exists_menu_in_chat(page: Page):
    home_page = HomePage(page)
    home_page.open_page()
    home_page.click_button(Chat.CHAT_BUTTON)
    home_page.fill_field(Chat.MSG_FIELD, 'Меню')
    home_page.click_button(Chat.SEND_MSG_BUTTON)
    parent = page.locator('.chat21-window') 
    for i in Chat.MESSAGES_BUTTON_SUCSESS_TEXT:
        elem = parent.get_by_text(i)
        expect(elem).to_be_visible()
    
