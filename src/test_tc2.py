import pytest
import asyncio
import random
import string
from playwright.async_api import async_playwright, expect
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get credentials
REDDIT_USERNAME = os.getenv("REDDIT_USERNAME")
REDDIT_PASSWORD = os.getenv("REDDIT_PASSWORD")

# Function to generate a random email and username
def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@pytest.mark.asyncio
async def test_reddit_register():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=500)  # Debug mode
        #browser = await p.firefox.launch(headless=False, slow_mo=500)  # Debug mode
        context = await browser.new_context()
        page = await context.new_page()

        # Navigate to Reddit login page
        await page.goto("https://www.reddit.com/login/")

        # Get the login iframe
        
        login_frame = page.frame_locator("xpath=//iframe[contains(@id=login, 'https://www.reddit.com/login'])")
        

        # Fill login form
        await login_frame.locator("input[name='username']").fill(REDDIT_USERNAME)
        await login_frame.locator("input[name='password']").fill(REDDIT_PASSWORD)
        await login_frame.locator("button[type='login']").click()





        