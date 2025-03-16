import pytest
import asyncio
import os
from playwright.async_api import expect
from playwright.async_api import async_playwright
from helper import generate_random_string
from params import BASEURL, EP_REGISTER, EP_COMMUNITY, EP_R, SIGN_UP_PAGE, LEN_PSW, INTERESTS_PAGE
from params import VERIFY_EMAIL_PAGE, CREATE_USERNAME_PSW_PAGE, ABOUT_YOU_PAGE

@pytest.mark.asyncio
async def test_reddit_register():
    async with async_playwright() as p:
        # SETUP
        #browser = await p.chromium.launch(headless=False, slow_mo=500)  # Debug mode
        browser = await p.firefox.launch(headless=False, slow_mo=500)  # Debug mode
        context = await browser.new_context()
        page = await context.new_page()

        # Navigate to Reddit Community page
        community_url = os.path.join(BASEURL, EP_R, EP_COMMUNITY)
                
        #await page.goto(register_url)
        await page.goto(community_url)
        await expect(page).to_have_url(community_url)

        await page.get_by_role("link", name="join", exact=True).click()
        
        ######################################################################################
        ############# Works until here #######################################################
        ######################################################################################
        
        await context.close()
        await browser.close()

