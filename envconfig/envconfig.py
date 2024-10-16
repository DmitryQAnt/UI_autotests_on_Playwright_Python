"""
This module contains a pytest fixture for initializing a Playwright browser page.
The fixture starts a new browser context and opens the target URL before each test,
and ensures proper cleanup after the test finishes.
"""

import pytest
from data.test_data import url
from playwright.sync_api import Browser, Page


@pytest.fixture(scope="function")
def start_page(browser: Browser) -> Page:
    """
    Fixture for creating a new Playwright page, navigating to the specified URL, and setting a default timeout.

    :param browser: An instance of Playwright Browser.

    :return: An instance of Playwright Page after navigation to the given URL.
    """
    context = browser.new_context()
    page = context.new_page()
    page.goto(url)
    page.set_default_timeout(2000)

    yield page

    page.context.close()
