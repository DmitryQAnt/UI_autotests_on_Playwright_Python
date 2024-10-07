import pytest
from data.test_data import url
from playwright.sync_api import Browser


@pytest.fixture(scope="function")
def start_page(browser: Browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto(url)
    page.set_default_timeout(2000)

    yield page

    page.context.close()
