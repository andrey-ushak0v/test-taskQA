from playwright.sync_api import Page, expect


def test_open_page(page: Page):
    page.goto('https://autofaq.ai/')


def test_search_chat(page: Page):
    page.goto('https://autofaq.ai/')
    button = page.locator('.svg-bg')
    expect(button).to_be_visible()


def test_opening_chat(page: Page):
    page.goto('https://autofaq.ai/')
    button = page.locator('.svg-bg')
    expect(button).to_be_visible()
    button.click()


def test_send_message_in_chat(page: Page):
    page.goto('https://autofaq.ai/')
    button = page.locator('.svg-bg')
    button.click()
    msg_field = page.locator('.f21textarea')
    msg_field.fill('Пример текста')
    send_msg_button = page.locator('#chat21-button-send')
    send_msg_button.click()
    sended_msg = page.get_by_text('Пример текста')
    expect(sended_msg).to_be_visible()