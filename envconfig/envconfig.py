import pytest
from playwright.sync_api import sync_playwright, Browser
from playwright.sync_api import expect

TEST_PAGE = "https://stellarburgers.nomoreparties.site/"

@pytest.fixture(scope="function")
def browser_page(browser: Browser):
    context = browser.new_context()
    page = context.new_page()
    page.wait_for_url(TEST_PAGE)
    page.set_default_timeout(DEFAULT_WAIT_2_SEC:=2000)

    yield page

    page.context.close()
