import pytest
import asyncio
import random
import string
from playwright.async_api import async_playwright


# Function to generate a random email and username
def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@pytest.mark.asyncio
async def test_reddit_register():
    async with async_playwright() as p:
        #browser = await p.chromium.launch(headless=False, slow_mo=500)  # Debug mode
        browser = await p.firefox.launch(headless=False, slow_mo=500)  # Debug mode
        context = await browser.new_context()
        page = await context.new_page()

        # Navigate to Reddit sign-up page
        await page.goto("https://ww.reddit.com/register/")

        # Generate random credentials
        random_email = f"{generate_random_string()}@gmail.com"
        random_username = generate_random_string()
        random_password = generate_random_string(12)

        # Wait for the email input field and enter an email
        await page.fill("input[name='email']", random_email)

        # Click continue button 1
        await page.click("button:has-text('Continue')")

        # Wait for username and password fields to appear
        # await page.wait_for_selector("input[name='username']", timeout=5000)
       

        # Click Skip button 1 
        #await page.click("button:has-text('skip')")
        #await page.locator("text='skip'").click()
        await page.get_by_role("button", name="Skip").click()

        # Fill in password field, user field is filled automaticly
        await page.fill("input[name='password']", random_password)
        await page.wait_for_timeout(5000)  # 5000 milliseconds = 5 seconds
        print("print after psw IGOR OIGOR IGOR")

        # Click continue button 2
        #await page.locator('xpath=//*[@id="register"]/faceplate-tabpanel/auth-flow-modal[2]/div[2]/faceplate-tracker/button').click()
        #await page.get_by_role("button", name="Continue").click()
        #await page.click("button:has-text('Continue')")
        await page.locator("#register button.create.button-large").click()
        await page.wait_for_timeout(5000)  # 5000 milliseconds = 5 seconds

        # click Skip button 2
        await page.get_by_role("button", name="Skip").click()
        #await page.click("button:has-text('skip')")
        await page.wait_for_timeout(10000)  # 5000 milliseconds = 5 seconds
        
        await page.locator('button[role="checkbox"].topic').click()
        await page.wait_for_timeout(5000)  # 5000 milliseconds = 5 seconds

        await page.locator("#register button.create.button-large").click()
        print("after interests IGOR OIGOR IGOR")
        # # Click the Sign Up button
        # await page.click("button:has-text('Sign Up')")

        # # Wait for confirmation that the account was created (Reddit may show a CAPTCHA)
        # await page.wait_for_selector("button[aria-label='User menu']", timeout=15000)

        # # Assert registration success by checking for the user menu
        # user_menu = await page.query_selector("button[aria-label='User menu']")
        # assert user_menu is not None, "Registration failed!"
        
        await context.close()
        await browser.close()
