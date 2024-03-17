from selenium import webdriver
import pytest
import pytest
from playwright.sync_api import sync_playwright
from playwright.sync_api import expect

TEST_PAGE = "https://stellarburgers.nomoreparties.site/"


class BrowserSet:
    DEFAULT_WAIT_2_SEC = 2000
    @pytest.fixture
    def browser_fixture(self):
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            page.goto(TEST_PAGE)
            yield page
            page.close()
            browser.close()