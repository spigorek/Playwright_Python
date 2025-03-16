import logging
import pytest
import requests
import json
import asyncio
import os
from playwright.async_api import async_playwright
import pytest_asyncio
from src.params import BASEURL_API, EP_ACCESS_TOKEN
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

@pytest.fixture(scope="session")
def get_token():
    import logging
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    APP_USERNAME = os.getenv("APP_USERNAME")
    APP_PASSWORD = os.getenv("APP_PASSWORD")
    USER_AGENT = os.getenv("USER_AGENT")
    access_token_url = os.path.join(BASEURL_API, EP_ACCESS_TOKEN)
    logging.info(f'access_token_url = {access_token_url}')

    auth_response = requests.post(
        access_token_url,
        auth=(CLIENT_ID, CLIENT_SECRET),
        data={
            "grant_type": "password",
            "username": APP_USERNAME,
            "password": APP_PASSWORD
        },
        headers={"User-Agent": USER_AGENT}
    )
    
    # Check if we got a valid token
    if auth_response.status_code != 200:
        logging.info(f"Failed to get auth token: {auth_response.text}")
        return
        
    token_data = auth_response.json()
    access_token = token_data.get("access_token")
    
    if not access_token:
        import logging
        logging.info("No access token in response")
        return
    
    BEARER_TOKEN = f'Bearer {access_token}'
    logging.info(f"Got access token: {access_token}")
    return access_token

@pytest_asyncio.fixture(scope="session")
async def launch_logged_in(get_token):
    access_token = get_token
    async with async_playwright() as p:
        # Launch Chromium browser
        browser = await p.chromium.launch(headless=False, slow_mo=500)
        context = await browser.new_context()
        page = await context.new_page()
        
        # First load Reddit
        await page.goto("https://ww.reddit.com")
        
        # Set access token in localStorage
        await page.evaluate(f"""() => {{
            localStorage.setItem('accessToken', '{access_token}');
            // Reddit stores tokens in various forms
            localStorage.setItem('token', '{access_token}');
            localStorage.setItem('reddit_session', '{access_token}');
        }}""")
        
        # Set cookies for Reddit domain
        await context.add_cookies([
            {
                "name": "reddit_session",
                "value": access_token,
                "domain": ".reddit.com",
                "path": "/"
            },
            {
                "name": "token_v2",
                "value": access_token,
                "domain": ".reddit.com",
                "path": "/"
            }
        ])
        
        # Reload the page to apply the session
        await page.reload()
        
        # Wait a bit to ensure login processes
        await page.wait_for_timeout(2000)
        
        # Check if we're logged in by looking for user menu
        try:
            user_menu = page.locator("[data-testid='reddit-user-menu']")
            is_visible = await user_menu.is_visible(timeout=2000)
            if is_visible:
                logging.info("Successfully logged in!")
            else:
                logging.info("Login may have failed - user menu not visible")
        except Exception as e:
            logging.info(f"Error checking login status: {e}")
        
        # Save the browser state for future use
        await context.storage_state(path="reddit_state.json")
        logging.info("Saved browser state to reddit_state.json")
        
        yield page
        
        await context.close()
        await browser.close()