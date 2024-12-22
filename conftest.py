from playwright.sync_api import Page
import pytest


@pytest.fixture()
def page(context):
    page: Page = context.new_page()
    page.set_viewport_size({'height': 500, 'width': 1000})
    yield page