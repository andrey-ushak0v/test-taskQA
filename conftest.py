from playwright.sync_api import Page
import pytest
import allure
from _pytest.fixtures import FixtureRequest


@pytest.fixture()
def page(context):
    page: Page = context.new_page()
    page.set_viewport_size({'height': 500, 'width': 1000})
    yield page


@pytest.fixture(autouse=True)
def attach_playwright_results(page: Page, request: FixtureRequest):
    yield
    if request.node.rep_call.failed:
        screenshot_path = f"screenshots/{request.node.name}.png"
        allure.attach.file(
            page.screenshot(path=screenshot_path),
            name="Screen shot on failure",
            attachment_type=allure.attachment_type.PNG,
        )
        
#@pytest.hookimpl(trylast=True, hookwrapper=True)
#def pytest_runtest_makereport(item):
#outcome = yield
#page = item.funcargs.get("page")
#report = outcome.get_result()
#if report.when == 'call' and report.outcome == "failed":
#    screenshot_path = f"screenshots/123.png"
#    allure.attach.file(
#        page.screenshot(path=screenshot_path),
#        name="Screen shot on failure",
#        attachment_type=allure.attachment_type.PNG,
#    )