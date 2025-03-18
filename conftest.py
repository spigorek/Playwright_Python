import pytest
import os
from playwright.sync_api import sync_playwright
from src.params import BASEURL, EP_LOGIN

@pytest.fixture(scope="session")
def browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    try:
        yield browser
    finally:
        browser.close()
        playwright.stop()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    try:
        yield page
    finally:
        page.close()
        context.close()

@pytest.fixture
def login_page(page):
    login_url = os.path.join(BASEURL, EP_LOGIN)
    page.goto(login_url)
    return page
