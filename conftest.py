import pytest
import os
from playwright.sync_api import sync_playwright
from src.params import BASEURL, EP_LOGIN

# The fixture browser is used to launch the browser on login page
@pytest.fixture(scope="session")
def browser(): # The browser fixture is used to launch the browser
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    try:
        yield browser
    finally:
        browser.close()
        playwright.stop()

@pytest.fixture
def page(browser): # The page fixture is used to create a new page
    context = browser.new_context()
    page = context.new_page()
    try:
        yield page
    finally:
        page.close()
        context.close()

@pytest.fixture
def login_page(page): # The login_page fixture is used to navigate to the login page
    login_url = os.path.join(BASEURL, EP_LOGIN)
    page.goto(login_url)
    return page
